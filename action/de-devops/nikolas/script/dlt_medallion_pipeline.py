import dlt
from pyspark.sql.functions import col, current_timestamp

# --- CONFIGURATION & METADATA ---
# Note: In a real scenario, you might pass these via DLT pipeline settings
RULES_TABLE = "workspace.metadata.quality_rules"

def get_rules(table_name):
    """
    Fetches data quality rules from a metadata table.
    If the table doesn't exist yet, returns an empty dict to prevent failure.
    """
    try:
        rules_df = spark.read.table(RULES_TABLE).where(col("table_name") == table_name)
        return {row.rule_name: row.condition for row in rules_df.collect()}
    except Exception as e:
        print(f"Warning: Could not load rules for {table_name}: {e}")
        return {}

# --- BRONZE LAYER: Auto Loader ---
# Simplifies ingestion by automatically tracking new files
@dlt.table(
    name="bronze_customers",
    comment="Raw customers data ingested via Auto Loader from CSV"
)
def bronze_customers():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("cloudFiles.header", "true")
        .option("cloudFiles.inferColumnTypes", "true")
        # Schema location is critical for Auto Loader to track changes
        .option("cloudFiles.schemaLocation", "/Volumes/workspace/bronze/schemas/customers_dlt")
        .load("/Volumes/workspace/bronze/raw_sources/source_crm/cust_info.csv")
        .withColumn("ingestion_timestamp", current_timestamp())
    )

# --- SILVER LAYER: CDC (Change Data Capture) ---
# apply_changes handles Inserts, Updates, and Deletes automatically
dlt.create_streaming_table(
    name="silver_customers",
    comment="Cleaned and merged customer records (SCD Type 1)"
)

dlt.apply_changes(
    target="silver_customers",
    source="bronze_customers",
    keys=["cst_id"],
    sequence_by=col("ingestion_timestamp"),
    stored_as_scd_type=1  # SCD Type 1 = Overwrite on change
)

# --- GOLD LAYER: Metadata-Based Quality Checks ---
# We use Python to dynamically apply expectations from our metadata table
cust_rules = get_rules("silver_customers")

@dlt.table(
    name="gold_customers_vetted",
    comment="Final customer table with quality checks applied from metadata"
)
# If cust_rules is empty, this decorator does nothing
@dlt.expect_all_or_drop(cust_rules)
def gold_customers_vetted():
    return dlt.read("silver_customers")

@dlt.table(
    name="gold_sales_summary",
    comment="Aggregated sales metrics with its own metadata rules"
)
@dlt.expect_all(get_rules("gold_sales_summary"))
def gold_sales_summary():
    # Example join/aggregation
    return (
        dlt.read("silver_customers")
        .groupBy("country")
        .count()
        .withColumnRenamed("count", "customer_count")
    )
