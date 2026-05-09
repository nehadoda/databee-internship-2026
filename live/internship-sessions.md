# Databee Internship 2026 — Session Notes

> Sessions are ordered **latest first** — most recent session at the top.

---

## Session 8 — May 16, 2026 *(upcoming)*

**Attendees:**

**Agenda:**

**Part 1 — Weekly sync**

1. Week check-in — what did you work on? Blockers? Wins?
2. Deepika — E2E Databricks + Unity Catalog infra deployment demo (Terraform + GitHub Actions) *(committed for this session)*
3. ~~Filip — dbt silver layer demo: quarantine/dead-letter table with reason tags~~ → *(carried over — Filip absent Session 7)*
4. ~~Nikolaos — metadata-driven DQ framework walkthrough~~ → *(carried over — Nikolaos absent Session 7)*
5. Asindu — DQX data quality implementation in silver layer walkthrough
6. Sanjeev — Deepika's MLOps path *(to be defined and shared)*
7. Sanjeev — Spark Definitive Guide: specific chapters for DE interns to focus on

**Part 2 — Technical deep-dives**

8. ~~Elliot — MLflow deep-dive: model logging, feature stores, serving endpoint~~ → *(carried over — Elliot absent Session 7)*

**Notes:**

*(To be filled after session)*

---

## Session 7 — May 9, 2026

**Attendees:** Sanjeev Kumar (mentor), Kousalya, Deepika Elangovan, Neha Doda, Suhash Raja, Asindu Gayangana
**Absent:** Filip Cedermark *(texted unable to join)*, Elliot Eriksson, Nikolaos Biniaris

**Agenda:**

**Part 1 — Weekly sync**

1. Week check-in — what did you work on? Blockers? Wins?
2. Session stream split — confirm DE+DevOps / ML / DA structure and logistics *(carried over)*
3. ~~Filip — dbt silver layer demo: quarantine/dead-letter table with reason tags~~ *(Filip absent — carried over)*
4. Deepika — CI/CD artifact separation: Bundles vs Terraform for catalog, schema & checkpoints *(pros/cons)*
5. ~~Nikolaos — metadata-driven DQ framework walkthrough~~ *(Nikolaos absent — carried over)*

**Part 2 — Technical deep-dives**

6. ~~Elliot — MLflow deep-dive: model logging, feature stores, serving endpoint~~ *(Elliot absent — carried over)*
7. Spark streaming optimization — rate limiting, `maxBytesPerTrigger`, `maxFilesPerTrigger`, partition pruning *(Asindu's `maxBytesPerPartition` issue + broader context)*
8. Spark Definitive Guide walkthrough — group reading/discussion session
   - Reference: [Spark: The Definitive Guide](https://analyticsdata24.wordpress.com/wp-content/uploads/2020/02/spark-the-definitive-guide40www.bigdatabugs.com_.pdf)

**Notes:**

---

### 1. Week Check-in

- **Neha Doda** — Started dbt basics: installation, setup, intro videos, CLI commands. Connected dbt to Microsoft SQL Server locally. Also assigned by Raj to write website content on data platform modernization (separate from internship tasks).
  → **Sanjeev**: Stay on DA track. Primary focus: Power BI (3+ years experience, PL-300 certified) — practice deeply (DAX, time intelligence, KPIs, access control, Power BI Service). dbt is the right tool for SQL-based transformations alongside BI. Also explore **Tableau** and **Looker Studio** — concepts are generic across tools. Raj has upcoming opportunities for dashboarding resources.
- **Deepika Elangovan** — Researched Databricks Asset Bundles (also referred to as Databricks Automation Bundles) + Terraform. Key findings: Terraform handles infrastructure (catalog, storage, permissions); DABs handle pipeline/job deployment via `databricks.yml`. Hitting errors with free edition; iterating with Claude for troubleshooting. Got accepted to **Chalmers Master's in Biomedical Engineering** (starts September) — wants to include ML/MLOps given it's part of her program. Wants to be included in MLOps track.
- **Suhash Raja** — No update (sick all week, now recovering). Revealed he already has **Databricks Associate Data Engineer certification** (taken Feb 2026, studied from Spark Definitive Guide + Raj's PySpark book). Plans to go full throttle on DE tasks this week.
- **Asindu Gayangana** — Updated PySpark pipeline: optimized for both daily incremental runs and backfill using same pipeline. Completed gold layer tables. Currently researching **Databricks DQX** for YAML-based data quality expectations in silver layer.

---

### 2. Stream Specialization — Paths Confirmed

Sanjeev recapped and confirmed specialization paths for each intern:

| Intern | Track | Focus |
|---|---|---|
| **Neha** | DA | Power BI (primary), dbt for transformations, Tableau / Looker Studio |
| **Deepika** | DevOps → MLOps | E2E Databricks infra (Terraform + DABs + Azure); MLOps path TBD |
| **Suhash** | DE (Databricks specialist) | SCD, CDC, incremental ingestion, Unity Catalog, DLT, Lakeflow, DABs; target DE Pro |
| **Asindu** | DE (Databricks + Spark) | DQX, Unity Catalog, AutoLoader, declarative pipelines, Lakeflow; read Spark Definitive Guide |
| **Nikolaos** | DA | Same dashboarding advice as Neha (confirmed by Sanjeev) |
| **Filip** | DE + dbt | dbt silver layer + quarantine table *(absent)* |
| **Elliot** | ML / Snowflake | MLflow, Snowflake Cortex *(absent)* |

**Key point from Sanjeev**: Strong data engineering fundamentals matter more than platform choice — any company will take you if your fundamentals are solid (Spark, CDC, SCD, medallion architecture). Databricks is a strong choice given market growth, but don't limit yourself.

---

### 3. Databricks Asset Bundles (DABs) — Technical Discussion

- DABs = implementation on top of Terraform, managed via `databricks.yml` YAML file
- **State management advantage over plain Terraform**: in a mono-repo with 10 projects, Terraform rebuilds the whole state on any change. DABs treat each sub-project atomically — one project's deployment doesn't affect others.
- DABs renamed to **Databricks Automation Bundles** in recent docs (some older docs still say Asset Bundles)
- Known limitation: inherited Terraform state issues still surface; Databricks actively working on engine changes
- **Deepika's new capstone task**: End-to-end Databricks workspace + Unity Catalog deployment on Azure using Terraform + GitHub Actions. Must include: security (VNet isolation, hub-and-spoke model), proper separation of infra vs pipeline deployments.
- Deepika confirmed she maintained separate infra and code pipelines in previous experience — relevant here.

---

### 4. Spark Streaming Rate Limiting

Deep-dive with Asindu and Suhash:

- **`maxFilesPerTrigger`**: limits files per micro-batch. E.g., 100 new files + `maxFilesPerTrigger=10` → 10 sequential batches of 10 files each
- Within each batch, Spark distributes files across workers in parallel (e.g., 4 workers → ~2.5 files each)
- Batches are **sequential**, processing within each batch is **parallel**
- Rationale: prevents overwhelming compute with massive data volumes in a single micro-batch; matches processing capacity to cluster size
- Asindu confirmed understanding of `maxFilesPerTrigger`; watermarking noted as advanced topic — not required now
- **Partition pruning**: Suhash familiar; `maxBytesPerTrigger` to be read up on

---

### 5. Spark Definitive Guide

- Sanjeev emphasized this book as essential for all DE interns — common interview questions come from it
- Suhash confirmed he has already read it (used it to prep for Databricks Associate certification)
- Suhash shared PDF in Slack; index accessible via Adobe bookmarks panel
- Sanjeev to define specific chapters for Asindu to focus on (too many chapters to read all)

---

### 6. Architecture Diagrams

Sanjeev: all interns should capture their pipeline designs as architecture diagrams.
- Interviewers frequently ask candidates to draw an end-to-end architecture on the spot
- As a DE, you will transition towards solution architecture thinking — knowing which tool fits which layer is essential
- Start now: whenever you design something end-to-end, create a proper diagram alongside it

---

### Action Items

| Task | Owner | Due |
|------|-------|-----|
| Review Power BI interview prep doc; identify areas to practice | Neha | Next session |
| Explore Tableau and Looker Studio | Neha | Ongoing |
| E2E Databricks + Unity Catalog infra deployment on Azure (Terraform + GitHub Actions); research VNet isolation / hub-and-spoke | Deepika | Next session |
| Define Deepika's MLOps path; share with her | Sanjeev | Next session |
| Implement SCD Type 1 & 2, CDC, incremental ingestion in Spark 3; scale with Filip's Faker library; include DABs | Suhash | Next session |
| Define Suhash's Databricks specialization plan (Unity Catalog, DLT, Lakeflow) | Sanjeev | Next session |
| Implement DQX in silver layer using YAML expectations | Asindu | Next session |
| Define Spark Definitive Guide chapters for Asindu | Sanjeev | Next session |
| Draw architecture diagram for current pipeline | All DE interns | Ongoing |

---

## Session 6 — April 25, 2026

**Attendees:** Sanjeev Kumar (mentor), Kousalya, Filip Cedermark, Suhash Raja, Deepika Elangovan, Neha Doda, Nikolaos Biniaris, Elliot Eriksson, Asindu Gayangana

**Agenda:**

**Part 1 — Weekly sync**

1. Week check-in — what did you work on? Blockers? Wins?
2. Meeting schedule — agree on a fixed recurring time going forward *(raised in Apr 22 midweek sync)*
3. Session stream split — confirm structure from Session 5 announcement:
   - DE + DevOps stream: Sanjeev leads
   - ML stream: mentor TBD (acting - Sanjeev)
   - DA stream: mentor TBD (acting - Sanjeev)
4. Neha — dbt vs Databricks focus: which to prioritise first? *(flagged in midweek sync — wants Sanjeev's guidance)*
5. Elliot — ML Use Case 1 demo *(carried over from Session 5)*
6. Intern presentations — carried over from Session 5:
   - Incrementalization & idempotency — pipeline design, backfill handling
   - `infer schema` vs fixed schema — production pros and cons *(Asindu leads)*
   - `AvailableNow` trigger — correct explanation *(Asindu leads)*
   - Scalar UDF vs vectorized / Pandas UDF — when to use each *(Nikolaos leads)*
7. Nikolaos — detailed pipeline code walkthrough *(carried over from Session 5)*

**Part 2 — Based on midweek sync (Apr 22)**

8. Action item check-ins from Session 5:
   - **Suhash** — Databricks CE → Azure ADLS connection attempt
   - **Filip** — Faker data-generation code shared with group? dbt progress?
   - **Deepika** — DQ checks in Silver layer; new PR raised?
   - **Elliot** — ML Use Case 1 PR raised?
9. Admin: Deepika's Slack removal *(free trial expired — Kousalya following up with Raj)*

**Notes:**

---

### 1. Week Check-in

- **Filip Cedermark** — Screenshared Faker-based CDC generator: generates customer records (ID, name, email, phone, city, purchase amount) with configurable row count; first batch always change_type = "insert"; second function updates random rows → change_type = "update" or "delete"; includes nulls for DQ practice. Silver partly done: null email → "unknown@example.com", null phone → "not available". Next: move to dbt; implement quarantine/dead-letter table with reason tagging (Sanjeev recommendation). Will push code to GitHub.
- **Suhash Raja** — No major update this week.
- **Neha Doda** — Started SQL roadmap from GitHub; installed MS SQL Server 2019. Explored dbt and Databricks Academy fundamentals. Has prior Microsoft Fabric experience.
  → **Sanjeev**: Stay on DA track; dbt is the right tool — gives analysts power to do SQL-based transformations (equivalent of what DE does in PySpark). Switching to full DE from zero would be too steep right now. Discuss with Raj if wanting to change track.
- **Elliot Eriksson** — Demoed ML Use Case 1 (see section 2). Also working on Use Case 2. Dropped early.
- **Deepika Elangovan** — Limited progress (volunteering this week). Ingested data into bronze (customers + orders); silver: trimming, normalization, null removal, column renaming. Plans to add advanced functions before next session.
  → **Sanjeev task**: Research CI/CD artifact separation — what belongs in pipeline deployment (Databricks Bundles/API) vs infrastructure deployment (Terraform): specifically catalog, schema, and checkpoint artifacts. Prepare a pros/cons argument.
- **Asindu Gayangana** — No major update (busy last two weeks).
- **Nikolaos Biniaris** — Implemented SCDs, full DQ framework (4 checks: uniqueness, not-null, FK relationships, accepted values), quarantine table with reason column, and business metric APIs (CLV, revenue by product, holiday impact, customer segments, country performance). Detailed walkthrough in section 3.

---

### 2. Elliot — ML Use Case 1 Demo (Counter-Strike round winner predictor)

- **Data & preprocessing**: Game state features (time left, players alive per team, etc.); binary labels (win=1/loss=0); 80/20 train/test split
- **Model**: Gradient Boosting Classifier; ROC AUC used for scoring
- **MLflow**: ~100 model runs via hyperparameter tuning; best model auto-selected. Accuracy improved from ~60% → ~80%
- **Sanjeev walkthrough of Databricks ML UI**: Showed Experiments + Models panel — all runs logged per iteration with metrics (precision, etc.); model can be registered and promoted; Serving section = deploy registered model to an endpoint for inference
- **Next steps for Elliot**: Explore MLflow in depth — model logging, feature stores, model serving. Also explore Snowflake Cortex (since now on Snowflake track).

---

### 3. Nikolaos — Pipeline Walkthrough & DQ Framework

Full pipeline: bronze → silver → dimensions → fact_sales → gold metrics → fact_sales_enriched (+ holidays API)

**DQ framework (modelled after dbt, without Great Expectations):**
- 4 checks: uniqueness of PKs, FK relationships, not-null on key columns, accepted values
- Single parameterized notebook — table name passed as job parameter; same notebook reused across all gold tables
- Quarantine table: broken rows with reason column (test type, failed count, pass rate)

**Sanjeev feedback:**
- Good reusable pattern; `.toPandas().toList()` for metadata table is fine for small metadata but flag as non-scalable if applied to data
- **Key next step — metadata-driven DQ framework**: Hardcoding column checks means every new table requires a code change → testing + deployment window + risk. Production standard: store check configs in a metadata table or JSON file → code reads config dynamically → no code change per new source onboarding
- **at-rest vs in-flight DQ**: current implementation reads data back after writing (at-rest). In-flight DQ (applied during write) is more efficient and lower latency. Research both; plan to migrate.

---

### 4. Technical Discussions

**infer schema vs fixed schema** (Suhash, Deepika, Asindu, Sanjeev):
- `inferSchema=True`: Spark samples a subset to auto-detect column types — risk of wrong inference (e.g., integer inferred but data later contains longs → truncation). Has happened in production.
- **Sanjeev's recommendation — mix and match**:
  - Give **schema hints** for critical columns (IDs, cost, dates) — Spark fixes those, infers the rest
  - In **bronze**: cast all columns to string (accepts everything, nothing dropped) + schema evolution enabled to capture new columns
  - In **silver+**: apply proper typed schema
  - Enable `mergeSchema=True` for schema evolution so new upstream columns are captured rather than silently dropped or failing the job
- **Asindu**: In bronze, schema inference + evolution is needed so new columns aren't lost for auditing. Sanjeev agreed but: risk of wrong type inference → prefer casting everything to string in bronze instead

**Scalar UDF vs Pandas (Vectorized) UDF** (Nikolaos, Suhash, Sanjeev):
- **Scalar UDF**: row-by-row; falls outside JVM → serialization/deserialization overhead; bypasses Catalyst optimizer. In some cases replacing a UDF with a native Spark function gives dramatic performance gains — this is one of the most common Spark optimization wins seen in production.
- **Pandas UDF**: chunk-based (processes batches of rows); stays within Spark execution model; significantly faster
- **Best practice**: Always prefer native Spark functions. Use UDF only when unavoidable. If unavoidable, use Pandas UDF.
- **When unavoidable**: custom ML inference per row (e.g., computer vision on IoT machine images — UDF fires model endpoint per image; switching to Pandas UDF → ~15K images processed in parallel per batch)
- UDFs unavoidable in ~20% of production cases; 80% can be replaced with native Spark functions

**AvailableNow trigger** (Asindu live demo, Sanjeev):
- `spark.readStream` polls source every 500ms by default — runs continuously
- `trigger(availableNow=True)`: converts streaming job to batch — reads all new files since last checkpoint, processes them in parallel, then stops. Checkpoint location handles incrementalization automatically.
- vs `spark.read` (batch): works fine but incrementalization must be handled manually (e.g., date-based directory structure + orchestrator passing current date)
- vs `trigger(once=True)` (deprecated): processes all data in a single batch — not parallel, inefficient for large datasets
- **Asindu's `maxBytesPerPartition` issue**: failing because source table is not partitioned — this option requires a partitioned source. To be covered in a dedicated Spark optimization session.
- Future sessions: dedicated deep-dive on rate limiting, `maxBytesPerTrigger`, `maxFilesPerTrigger`, partition pruning, and Spark optimization.

---

### 5. Logistics & Closing

- **Wednesday sync timing**: uncomfortable for several interns (Deepika: Swedish class; others joining late). To be resolved async via Slack.
- **Session stream split**: delayed due to logistics. Sanjeev handling all tracks for now; update coming via Slack.
- **Next session CANCELLED**: Sanjeev on business trip next weekend (returns Sunday evening). Session resumes in two weeks — **May 9**.

### Action Items

| Task | Owner | Due |
|------|-------|-----|
| Push Faker CDC data generator to GitHub repo | Filip | This week |
| Implement dbt silver layer with quarantine table and reason tags | Filip | Next session |
| Start dbt SQL learning roadmap | Neha | Ongoing |
| Research CI/CD artifact separation (Bundles/API vs Terraform for catalog, schema, checkpoints) — pros/cons | Deepika | Next session |
| Research at-rest vs in-flight DQ checks; build metadata-driven DQ framework | Nikolaos | Next session |
| Explore MLflow: model logging, feature stores, serving endpoint | Elliot | Next session |
| Post Slack poll for Wednesday midweek sync timing | Kousalya | This week |

---

## Session 5 — April 19, 2026

**Attendees:** Sanjeev Kumar (mentor), Kousalya, Filip Cedermark, Suhash Raja, Deepika Elangovan, Neha Doda, Nikolaos Biniaris, Elliot Eriksson
**Absent:** Asindu Gayangana

**Agenda:**

1. Week check-in — what did you work on? Blockers? Wins?
2. Intern Tech Platform & Specialization Map

   | Intern | Track | Specialization Focus | Primary Platform | Key Tools & Tech |
   |---|---|---|---|---|
   | **Suhash Raja** | DE + DevOps | Streaming ingestion, medallion architecture, infra provisioning | Databricks + Azure | Azure ADLS, Azure Data Factory, Terraform, Docker, GitHub Actions, PySpark, PL/SQL |
   | **Filip Cedermark** | DE + dbt | Data products, medallion architecture, CDC | Databricks + dbt | PySpark, Delta tables, Faker, dbt |
   | **Deepika Elangovan** | DE + DevOps | CI/CD pipelines, ETL/ELT, IaC integration | Databricks + Azure DevOps | Terraform, Kubernetes, Jenkins, GitHub Actions, PySpark, PowerShell |
   | **Neha Doda** | DA | BI dashboards, KPIs, SQL fundamentals | Power BI + Databricks (exploring) | Power BI (PL-300 certified), Excel, SQL, HackerRank |
   | **Asindu Gayangana** | DE | Advanced pipelines, CDC, Spark optimization | Databricks | Autoloader, Change Data Feed, PySpark, Kaggle data, Parquet, Azure Synapse (prior) |
   | **Nikolaos Biniaris** | DE | API integration, enriched retail pipelines | Databricks | PySpark, Pandas UDF, Public Holidays API, Weather API, Delta tables, Liquid Clustering |
   | **Elliot Eriksson** | ML | Supervised learning, synthetic data generation | Snowflake | MLflow, Snowflake ML, TensorFlow/PyTorch (exploring), PySpark, VS Code |

   > **Note:** Filip added **dbt** as second specialisation; Elliot switched from Databricks to **Snowflake**.

3. Deepika demo — CI/CD pipeline with GitHub Actions, Docker & Kubernetes *(carried over from Session 4)*
4. Architectural discussion — End-to-end data platform walkthrough *(Azure reference architecture)*
5. *(Carried over to next sessions)* Intern presentations — incrementalization, infer schema, AvailableNow trigger, UDFs; Elliot ML demo

**Notes:**

### 1. Week Check-in

- **Suhash Raja** — Connected Databricks to Azure ADLS using Azure Access Connector (managed identity service). Configured storage container access so Databricks reads ADLS automatically via Spark. Learned that Databricks creates a default Access Connector for Unity Catalog metadata — separate from the user-created one for data access. Sanjeev confirmed this distinction. Will also try connecting Databricks Community Edition (free tier) to ADLS.
- **Filip Cedermark** — Busy week (family matters), slightly behind. Switched to Faker for synthetic customer event data (fields: customer ID, name, email, phone, city, purchase amount, signup date). Planning to add CDC logic simulating email/city/order updates. Sanjeev asked Filip to share the Faker code with the group when ready so others can generate large-scale test data.
- **Deepika Elangovan** — Prepared CI/CD demo (presented in item 3). Working on Silver layer: removing nulls/duplicates, renaming columns. Plans to study window functions and Parquet vs Delta next. Sanjeev reminder: Silver is not done without data quality checks — add DQ before considering it complete.
- **Neha Doda** — Got onboarding guidance from Suhash and Filip during mid-week sync. Starting with SQL via the DA roadmap. Already holds Power BI PL-300 certification. Sanjeev directed her to the DA use case week-by-week plan in the repo.
- **Nikolaos Biniaris** — Implemented full CDC across bronze → silver → gold independently. Bronze: MERGE UPSERT by comparing primary key counts. Silver: watermark-based incremental inserts/updates. Gold: rebuilds dimensions/facts for new data. Raised and merged a PR to the main repo. Sanjeev: great example of the Git flow others should follow.
- **Elliot Eriksson** — Completed ML Use Case 1 in Databricks; needs to connect to GitHub and raise a PR. Watching Stanford ML lectures. Participating in a hackathon building a synthetic data model — plans to tie it into Use Case 2. Will demo if time permits.

---

### 2. Tech Platform Diversification

Sanjeev raised that the cohort is heavily Databricks + Azure focused and that **dbt** and **Snowflake** are widely used in the market with customer demand. Asked for volunteers:

- **Filip** → **dbt** (has prior internship experience with it; familiar with the concepts)
- **Elliot** → **Snowflake** (fully switching; had not progressed far in Databricks)

Others remain on Databricks and can add a second platform later. Sanjeev updated the tech platform table.

---

### 3. Deepika Demo — CI/CD with GitHub Actions, Docker & Kubernetes

**CI/CD overview:**
- CI/CD = Continuous Integration / Continuous Delivery (or Deployment)
- Continuous Delivery = requires manual approval before production deploy
- Continuous Deployment = fully automated all the way to production
- Common practice: auto-deploy to dev/test/staging; manual gate for production

**GitHub Actions:**
- Pipeline config lives in `.github/workflows/` as YAML files
- Triggered on push or PR merge to a configured branch
- Steps: checkout code → set Python version → install dependencies → Docker login → Docker build → Docker push
- Secrets (Docker Hub token, API key) stored as GitHub Secrets — never hardcoded in code

**Docker:**
- Dockerfile layers: base image → set workdir → copy requirements → `pip install` → copy source code → expose port → run command
- Image tagging convention: `<date>.<run-number>` (e.g. `19.4.2026.6`) — human-readable vs default SHA hashes

**Kubernetes:**
- Rolling deployment: new pod is created and verified healthy before old pod is terminated → zero downtime
- Key concepts: pod (runs containers), service (exposes app), deployment (desired state config), node (VM), control plane (cluster management)
- Minikube used locally for demo (GitHub Actions does not support Minikube; it's a local learning tool only)

**Live demo app:** FastAPI Gothenburg Weather app using OpenWeather API (temperature, humidity, wind, 5-day forecast). Showed: Docker pull from Hub, `kubectl apply -f deployment.yaml`, rolling pod update in real time.

**Azure deployment path shown (not live):** Service principal + AKS cluster name + resource group configured as GitHub Secrets, then same YAML apply approach.

**Q&A highlights:**
- *Elliot:* When deploying new code, do you need to restart the running process? → *Sanjeev:* Yes, unless using blue-green deployment. *Deepika:* Kubernetes rolling deployment handles this — new pod runs before old pod is terminated.
- *Sanjeev:* How much of this applies to MLOps? → *Deepika:* Limited MLOps experience, couldn't fully answer. Same CICD principles apply but MLOps has model-specific concerns.

---

### 4. Architectural Discussion — End-to-End Data Platform

Sanjeev walked through a full Azure-based reference architecture of a typical customer data platform — framed as essential interview knowledge for all tracks (DE, DA, ML, DevOps).

**Sources:**
- RDBMS/DWH (SQL Server, Synapse) — JDBC connections, CDC streams
- Sensors & IoT (wind farms, electricity meters, factory machines, Electrolux fridges) — continuous real-time streams
- Files/Logs (JSON, XML, audit logs, cybersecurity logs) — semi-structured
- Media/Unstructured (images, video) — fed to ML models (e.g. Northvolt predictive maintenance)
- Business Apps — structured/aggregated; ML typically consumes at gold/feature store level
- Multi-cloud — common in enterprise; involves egress cost, networking, private links

**Ingest — Batch vs Streaming:**
- Batch: hours/daily cadence, lower cost
- Near real-time: seconds to minutes; Real-time: <1 second (fraud detection, card tap)
- Interview tip: always reason about *why* streaming is needed — cost tradeoff is real; every interviewer will probe this
- Tools: Azure Event Hub / Data Factory, Databricks Structured Streaming, Snowflake Snowpipes, AWS Kinesis

**Orchestration (spans all layers):**
- Manages job dependencies and scheduling end-to-end (ingest → transform → gold → reverse ETL)
- Tools: Databricks Workflows, Azure Data Factory, Apache Airflow, AWS Glue ETL

**Data & AI Governance:**
- Non-negotiable for enterprise production: row/column-level security, access control, lineage
- Databricks: Unity Catalog; Snowflake: Horizon; Azure: Purview; cross-platform: Immuta (referential catalog)
- For ML: AI governance — model access audit, EU AI Act compliance
- Sanjeev: *"Any platform without fine-grained access control will fail enterprise customers"*

**Operational DB & Reverse ETL:**
- Low-latency serving (<100ms): LakeBase (Databricks managed Postgres), Snowflake equivalent
- Reverse ETL: pushing aggregated gold data back to operational DBs for fraud detection, credit checks, in-app real-time dashboards

**Collaboration / Data Sharing:**
- Delta Share (Databricks), Snowflake Marketplace — share data with third parties without copying it

**DevOps across all layers:**
- DevOps/MLOps applies everywhere — CI/CD for code changes, IaC for infrastructure, MLOps for model lifecycle

**GDPR vs Data Governance:**
- Data Governance = who has access to data at rest right now (access control, lineage)
- GDPR = regulatory compliance (right to be forgotten, data residency) — related but distinct

![Data Intelligence Platform Architecture](../images/lakehouse-architecture.png)

---

### 5. Closing & Next Steps

- **Session structure from next week:** Sessions split into specialised streams
  - DE + DevOps: Sanjeev leads
  - ML: separate mentor TBD (Elliot's stream)
  - DA: TBD — Sanjeev or another mentor
- Sanjeev to share the split session plan in the group channel before next week

**Carried over to future sessions:**
- Intern presentations: incrementalization & idempotency, infer schema vs fixed schema, AvailableNow trigger, Scalar vs Pandas UDF
- Elliot ML Use Case 1 demo
- Nikolaos detailed pipeline code walkthrough

### Action Items

| Task | Owner | Due |
|------|-------|-----|
| Try connecting Databricks CE to Azure ADLS | Suhash | Next session |
| Share Faker data-generation code with group | Filip | This week |
| Implement DQ checks in Silver layer | Deepika | Next session |
| Delete & re-upload demo files; raise new PR with latest changes | Deepika | This week |
| Study DA use case plan week-by-week | Neha | Ongoing |
| Raise PR for ML Use Case 1 code | Elliot | This week |
| Explore dbt | Filip | Ongoing |
| Explore Snowflake | Elliot | Ongoing |
| Share next week's split session plan with group | Sanjeev | Before next session |

---

## Session 4 — April 11, 2026

**Attendees:** Sanjeev Kumar (mentor), Elliot Eriksson, Suhash Raja, Deepika Elangovan, Nikolaos Biniaris, Asindu Gayangana

*Note: Filip not present.*

**Agenda:**

**Part 1 — Carried over from Session 3**
1. Week check-in — what did you work on? Blockers? Wins?
2. Parquet deep dive — why is it the backbone of big data?
3. Code sharing — Stage 1 progress; screen share what you have built so far
4. Architectural discussion — table formats (Delta, Iceberg, Hudi) deep dive and comparison; Lakehouse vs Data Lake vs Data Warehouse

   ![Data Intelligence Platform Architecture](../images/lakehouse-architecture.png)
5. ~~Deepika demo — CI/CD pipeline with GitHub Actions + Databricks~~ *(moved to Session 5 — PR raised, demo needs more prep)*

**Part 2 — Based on midweek sync (Apr 8)**
- Git workflow recap — quick walkthrough of feature branch → PR flow
- Data sources Q&A — clarify what datasets to use per stage (Faker, Kaggle, CoinGecko API, Raspberry Pi IoT simulator)
- ~~Catch up with Filip & Nikolaos — hear about their progress and see if there is anything the group can help with~~ *(Filip absent; Nikolaos covered in check-in)*

**Notes:**

### 1. Week Check-in

- **Elliot Eriksson** — Chose Databricks as ML platform. Currently working on a simple supervised learning project to learn how Databricks works. Has Git set up but hasn't pushed code yet — waiting until something is complete.
- **Suhash Raja** — Studied window functions and CTEs. Attempted to set up source data but hit connectivity issues between local machine and Azure. Exploring Kafka + Kubernetes → Databricks as a pipeline topology. Sanjeev flagged to not stay stuck — ask for help early. Will set up Git repo.
- **Deepika Elangovan** — Set up Databricks platform. Generated synthetic data using Faker (orders.csv + customers.csv, ~5,000 rows). Uploaded to Databricks and read using PySpark. Studied Spark architecture, DAG, lazy evaluation, DataFrames, and ELT vs ETL hybrids. Raised a PR for CI/CD work (used fork method instead of direct clone — Sanjeev confirmed both approaches are fine). Will demo CI/CD next session.
- **Nikolaos Biniaris** — Joined CSV sources and enriched with API data. Initially used a weather API for order enrichment but hit rate limits (~900 records/day cap). Switched to a **Public Holidays API** to enrich orders by country — goal is to analyse whether sales correlate with public holidays. Screen-shared pipeline showing parallel ingestion (CSV + API) and Silver join on the date column.
- **Asindu Gayangana** — Parameterized pipeline scripts using Databricks task parameters passed into notebooks. Created a DIM_DATE table directly to Silver (skipped Bronze — justified as a one-time static load). For other sources, used AutoLoader (`readStream` + `cloudFiles`) with schema inference, schema evolution mode, `maxFilesPerTrigger`, and CDC. Screen-shared code. Had a detailed discussion on incrementalization, infer schema, and the AvailableNow trigger (see section 3).

---

### 2. Parquet Deep Dive

Group discussion — interns shared what they researched:

- **Suhash** — Columnar format stores data column-by-column rather than row-by-row. Since values in a column share the same type, compression is very efficient. Only selected columns are read — not the entire row.
- **Nikolaos** — Validated the column pruning behaviour: selecting 2 of 20 columns reads only those 2 columns; the other 18 are skipped entirely by the engine. This can reduce query time from hours to seconds at scale.
- **Asindu** — Added that Parquet is OLAP-optimised. Per-column compression is more effective because each column has a uniform data type. Parquet also stores min/max statistics per column chunk, enabling predicate pushdown and file pruning without reading the data itself.

**Sanjeev expanded:**
- Parquet compression algorithms (Snappy, ZSTD) can compress data 10x or more — a file that is 100 MB on disk could expand to 10 GB in memory.
- In contrast, CSV/text compression is far less efficient because data types are mixed per row.
- **Open table formats (Delta, Iceberg, Hudi)** are not new file formats — they are Parquet underneath, but with an additional **metadata layer** (JSON/Avro sidecar files) that stores: min/max statistics per column, deletion vectors, schema versions, and partition metadata.
- When a query runs against a 1 TB table split across 10,000 Parquet files, the metadata layer allows **data skipping** — the engine reads the metadata first and prunes irrelevant files before touching any data files.
- **Task for next session:** Research what specific problems Delta/Iceberg/Hudi solve that raw Parquet cannot handle on its own.

---

### 3. Code Screen Shares & Technical Discussion

**Nikolaos — API Ingestion & Parallel Pipeline**
- Ingesting CSV and Public Holidays API in parallel Databricks tasks.
- Silver layer joins the two sources on the date column to enrich orders with holiday flags.
- Hit weather API rate limits earlier — good real-world lesson on API ingestion design.
- **Sanjeev's advice on API ingestion in interviews:** Be able to articulate that API ingestion is viable but comes with trade-offs — rate limits, scalability (will the API handle a 10x increase in calls?), and whether batch pull vs event-driven push is the right model.
- **Spark UDFs vs pure Python for APIs:** Nikolaos correctly avoided Spark UDFs for API calls. Key reasons: UDFs fall outside the JVM and lose Catalyst optimiser benefits; they are row-by-row unless vectorized; serialisation/deserialisation overhead.
- **Sanjeev assigned research:** Compare **scalar UDF** vs **vectorized UDF (Pandas UDF)** — why the vectorised variant is faster and when each should be used.

**Asindu — Parameterized AutoLoader Pipeline**
- Task parameters passed from Databricks Workflow into notebook widgets — good production pattern for reusability.
- DIM_DATE created directly to Silver without Bronze — valid for one-time static reference tables.
- For transactional sources, used AutoLoader (`readStream + cloudFiles`) with:
  - `inferSchema = true` — auto-detects column types; if disabled, everything reads as string.
  - `schemaEvolutionMode` — handles upstream schema changes without failing the job.
  - `maxFilesPerTrigger` — limits how many files are processed per micro-batch (scalability control).
- **Sanjeev's questions (to research for next session):**
  - `inferSchema true` vs manually defining a fixed schema — what production problems can each cause?
  - `AvailableNow` trigger — Asindu's explanation was partially correct; Sanjeev clarified: if you use `readStream`, the job would normally run continuously (24/7). `AvailableNow` tells the streaming API to process all available data *now* and then stop — making a streaming job behave like a scheduled batch job.
- AutoLoader handles idempotency automatically via checkpoint locations — it tracks which files have already been processed and only ingests new arrivals.
- **Sanjeev noted:** Even without AutoLoader, incrementalization can be achieved using batch APIs — interns should understand both approaches.

**General points raised by Sanjeev:**
- All interns should push code to Git using the **feature branch → PR** workflow. Treat the internship repo like a production delivery to a customer.
- Asindu's Git invite had expired — Sanjeev to re-add.
- Session time of 1 hour is proving short given the screen-sharing depth. Sanjeev will discuss extending sessions with Kousalya.

---

### 4. Architectural Discussion — Lakehouse Introduction *(partial)*

- **Deepika** summarised: Data Warehouse holds processed/structured data; Data Lake holds raw + semi-structured data; Lakehouse is a combination of both for advanced analytics.
- **Sanjeev** began the evolution narrative: started with traditional Data Warehouses (Oracle, SQL Server) → limitations led to the Data Lake concept → *(transcript cut off here)*
- The group discussed the key differences between the three paradigms — Data Warehouse, Data Lake, and Lakehouse — and how the Lakehouse addresses the weaknesses of both predecessors.
- Discussion touched on how the Lakehouse architecture is **scalable** (built on object stores like S3/ADLS, compute and storage scale independently) and **ACID compliant** (enabled by open table formats like Delta Lake, Iceberg, and Hudi, which bring transactional guarantees on top of Parquet). *(Full discussion not captured in transcript — to be continued in Session 5.)*

---

### Action Items for Next Session

| # | Task | Who |
|---|------|-----|
| 1 | Research incrementalization patterns — simulate incremental data arrival and test that pipeline only ingests new files; research idempotency and backfill handling | All interns |
| 2 | Research what problems Delta / Iceberg / Hudi solve on top of raw Parquet — come ready to discuss | All interns |
| 3 | Push code to Git repo using feature branch → PR workflow | All interns |
| 4 | Understand Lakehouse architecture — differences between Data Warehouse, Data Lake, and Lakehouse; how Lakehouse achieves scalability and ACID compliance | All interns |
| 5 | Research `infer schema true` vs fixed schema — what production issues can each cause? | Asindu |
| 6 | Research `AvailableNow` trigger — explain correctly next session | Asindu |
| 7 | Research scalar UDF vs vectorized / Pandas UDF — explain the difference and when to use each | Nikolaos |
| 8 | Prepare CI/CD demo (GitHub Actions + Databricks) for Session 5 | Deepika |
| 9 | Resolve Azure connectivity issue; implement incremental ingestion pipeline | Suhash |
| 10 | Continue supervised learning project in Databricks; push code to Git | Elliot |
| 11 | Re-add Asindu to repo (invite expired); discuss session time extension with Kousalya | Sanjeev |

---

## Session 3 — April 4, 2026

**Attendees:** Sanjeev Kumar (mentor), Kousalya (organizer), Suhash Raja, Filip Cedermark, Asindu Gayangana, Elliot Eriksson, Deepika Elangovan, Nikolaos Biniaris

*Note: Easter weekend — some interns had limited availability; Filip left early.*

**Agenda:**
1. Repo walkthrough — structure, CLAUDE.md, branching strategy
2. Week check-in & platform check-in
3. Use case progress & live demos
4. Architectural discussion — file formats & table formats

**Notes:**

### 1. Repo Walkthrough

Sanjeev walked through the repo structure for interns who had just cloned it:

- `raw/` — raw inputs including meeting transcripts. Interns can commit their own midweek sync transcripts here as a progress tracker.
- `live/` — living documents (session notes, use cases, topics list). All interns have read/write access; suggest edits via PRs.
- `action/` — intern work artifacts. Each intern creates their own subfolder under their stream (e.g. `action/DE-DevOps/your-name/`). Treat it as a monorepo.
- `CLAUDE.md` — key config file for AI-assisted workflows. Changes should go through PRs, not direct commits to main.
- Branching strategy: `feature/*` → `dev` → `staging` → `main` (GitFlow lite). All interns should create feature branches and submit PRs.

---

### 2. Week Check-in & Platform Check-in

- **Suhash Raja** — Started SQL basics (DDL) in Databricks. Chose **Databricks** (free enterprise edition). Has not cloned the repo yet; plans to do so post-session.
- **Filip Cedermark** — Getting set up on Databricks; file structure setup was trickier than expected. Used ChatGPT to generate sample data and landed it in Databricks. Planning to look at Stage 2 (CDC) next. Sanjeev recommended switching to the **Faker library** for reusable, scalable data generation in Databricks.
- **Asindu Gayangana** — Built a pipeline in Databricks using a 5M-row Kaggle dataset. Used **Autoloader** for Bronze ingestion. Set up **Change Data Feed (CDF)** on the Bronze table — manually modified data via SQL, then extracted changed records using version history (max version). Loaded dimension tables; still needs to join the fact table for Silver. Also researched Spark internals: worker nodes, partitions, ideal partition sizes, on-heap memory (execution + storage). Could not fully understand off-heap memory.
- **Elliot Eriksson** — Read about Spark and PySpark; drew diagrams of how it works. Confirmed he's on the **ML track**. Planning to use VS Code + PySpark. Sanjeev pointed out ML platform options: Databricks (MLflow), Snowflake (Cortex), AWS (SageMaker), Azure ML.
- **Deepika Elangovan** — Created Databricks account (Azure free trial exhausted). Watching YouTube tutorials on data ingestion. Has an existing GitHub CI/CD repo. Sanjeev asked her to demo CI/CD pipeline to the group using GitHub Actions + Databricks integration. Also mentioned **Databricks Asset Bundles** and **Terraform** as tools to explore.
- **Nikolaos Biniaris** — Shared screen showing Databricks. Ingested CRM/ERP data (customers, products, sales + dimension data — 6 tables) using both Python and SQL notebooks. Chose not to partition at Bronze (no date columns; dates stored as strings). Researched partitioning in Databricks vs standard Spark. Asked about handling multiple source types (CSV + API) — Sanjeev showed how to build parallel Databricks workflow tasks for independent sources. Also asked about API ingestion; Sanjeev directed him to research **Spark UDFs** and their trade-offs.

---

### 3. Architectural Discussion — File Formats & Table Formats

**Structured vs Semi-structured vs Unstructured data:**
- **Unstructured** (images, binary blobs) — no schema, slowest to process.
- **Semi-structured** (JSON, XML) — schema loosely coupled (xsd for XML); can be processed without schema.
- **Structured** (tabular, Parquet, Delta) — schema tightly bound; fastest for engines to process.

**Open Source vs Proprietary formats:**
- Proprietary: Oracle, Teradata, Snowflake's internal formats — require licenses.
- OSS: Parquet, Delta, Iceberg, Hudi, Avro, ORC — free to use; any engine or platform can adopt them.
- Interview tip: being able to reference OSS technologies (Apache Spark, MLflow, Iceberg) rather than only vendor tools shows platform-agnostic depth.

**Object stores:** S3, ADLS, GCS — where all data lives as files (called "objects"). Bronze/Silver/Gold data all lives here.

**Parquet:**
- The bread and butter of the big data world. Columnar format. Foundation of almost every modern data platform.
- **Task for interns:** research *why* Parquet is so important and what problem it solves. Discuss in midweek sync.

**Open Table Formats — Delta, Iceberg, Hudi:**
- All three are built on top of Parquet but add a metadata layer.
- Key features added: ACID transactions, time travel, schema enforcement, versioning, upsert/merge support.
- Delta Lake: created by Databricks engineers, then open sourced. Liquid clustering is a Delta innovation, also open sourced.
- Iceberg and Hudi: alternative open table formats with similar capabilities.
- Discussion to continue next session with deeper comparison.

**Streaming source tip (for Suhash's question):**
- **Raspberry Pi Azure IoT Web Simulator** — free, browser-based tool that generates IoT data and writes to Azure IoT Hub. Can be pointed at Databricks Structured Streaming or ADF for practice with real streaming ingestion.

---

### Action Items for Next Session

| # | Task | Who |
|---|------|-----|
| 1 | Research why Parquet is the backbone of big data — come ready to discuss in midweek sync and Session 4 | All interns |
| 2 | Clone the repo; create your own folder under `action/` for your stream | All interns |
| 3 | Start Stage 1 (batch ingestion) in Databricks | Suhash |
| 4 | Switch data generation to Faker library; explore Stage 2 (CDC) | Filip |
| 5 | Complete Silver fact table join; commit code to `action/` folder | Asindu |
| 6 | Choose ML platform (Databricks / SageMaker / Azure ML); start ML use case | Elliot |
| 7 | Commit CI/CD demo (GitHub Actions + Databricks) to internship repo; explore Databricks Asset Bundles and Terraform | Deepika |
| 8 | Build parallel Databricks workflow (CSV + API sources); read about Spark UDFs and their trade-offs | Nikolaos |

---

## Session 2 — March 28, 2026

**Attendees:** Suhash Raja, Filip Cedermark, Deepika Elangovan, Neha Doda, Kousalya (organizer), Sanjeev Kumar (mentor), Vivek Prasad (mentor), Vinod (mentor), Asindu Gayangana, Nikolaos Biniaris, Elliot Eriksson

**Agenda:**
1. Week check-in — what did you work on? Anything to share?
2. Platform — use and registration
3. Use cases defined per stream
4. Architectural discussion



**Notes:**

### 1. Week Check-in

Interns shared what they worked on since Session 1:

- **Suhash + group** — Reviewed the shared presentation slides; had a midweek check-in among themselves to compare tools and skills.
- **Filip Cedermark** — Refreshed SQL fundamentals on HackerRank (basic and advanced queries). Also attended a Snowflake AI/agentic event (got in last-minute via a colleague's spare spot).
- **Deepika Elangovan** — Recapped SQL basics; had not used SQL since joining Accenture, so focused on getting back up to speed with small queries.
- **Asindu Gayangana** — Worked on SQL and PySpark; focused on window functions and complex joins. Subscribed to a Spark Playground for hands-on practice.
- **Nikolaos Biniaris** — Practised SQL heavily (window functions, joins). Asked a good question: *how much do we need to manage clustering ourselves in Snowflake vs Databricks?* Sanjeev explained predictive optimization — both platforms can auto-manage clustering, but Databricks gives manual control if needed.
- **Elliot Eriksson** — Limited prior experience with data lifecycle; had done minor data cleaning projects (null/duplicate removal) including a cancer-identification ML project.

Sanjeev's advice to the group: attend platform meetups (Databricks, AWS, Microsoft, Snowflake) beyond big paid events — look up smaller user groups and meetups on meetup.com.

---

### 2. Platform — Use and Registration

Sanjeev walked through how to choose a platform to implement the use cases:

- All major cloud platforms offer free/trial accounts: **Azure (ADF)**, **AWS (Glue)**, **Databricks (Lakeflow Designer / Serverless SQL — now unlimited free tier)**, **Snowflake**.
- Recommended approach — start easy, then go deeper:
  - **Phase 1:** Drag-and-drop tools (ADF, Glue, Lakeflow Designer) — implement the use case with minimal code to understand the concepts.
  - **Phase 2:** Re-implement the same use case in **pure PySpark** — this is the target skill for data engineers.
- Failures/errors encountered along the way will surface important Spark internals worth discussing in sessions.
- **Task:** Each intern to pick a platform, spin up a trial account, and report back next session which platform they chose.

---

### 3. Architectural Discussion

#### 1. Data Lifecycle
The journey every piece of data takes through a modern data platform:

- **Ingestion** — Pull raw data from source systems (databases, APIs, flat files, streams) and land it as-is into storage (Bronze layer). No transformation yet.
- **Cleaning** — Remove nulls, duplicates, invalid records. Standardize formats (dates, currency, casing). This produces a trusted, queryable Silver layer.
- **Transformation** — Apply business logic: joins, aggregations, KPI calculations, data modelling (Star Schema). This is the Gold layer — ready for consumption. dbt owns this step.
- **Serving** — Expose the clean, modelled data to end consumers: dashboards (Power BI / Tableau), APIs, ML models, or self-serve querying (Databricks Genie).

#### 2. Distributed Systems
Why we can't just use a single machine for large data:

- A single machine has limits on CPU, RAM, and disk — at scale, data doesn't fit
- Distributed systems split work across many nodes (computers) that work in parallel
- Key concepts: partitioning (splitting data), fault tolerance (handling node failures), coordination (who does what)
- Examples in the wild: Hadoop (HDFS), Kafka (streaming), Cassandra (NoSQL), and the Spark cluster itself
- The trade-off: more complexity, but linear scalability

#### 3. Distributed Engines
The processing layer that runs on top of distributed systems:

- **Apache Spark / PySpark** — The dominant batch + streaming engine. Processes data in-memory across a cluster. Used for Silver → Gold transformations at scale.
- **Apache Flink** — Real-time stream processing. Lower latency than Spark Streaming.
- **Databricks** — Managed Spark platform with optimizations (Delta Engine, Photon). What most enterprises run today.
- **dbt** — Not distributed itself, but pushes transformation logic down into the warehouse engine (Snowflake, BigQuery, Redshift) which is distributed underneath.

#### 4. File Formats
How data is physically stored on disk — this matters for performance:

| Format | Type | Pros | Best For |
|---|---|---|---|
| CSV | Row-based | Human readable, universal | Small files, quick sharing |
| JSON | Row-based | Flexible schema, API native | Raw ingestion, semi-structured data |
| Parquet | Columnar | Fast reads, great compression | Analytics, data warehouses |
| Avro | Row-based | Schema evolution, compact | Kafka streaming, Hadoop |
| Delta | Columnar + ACID | Versioning, time travel, ACID | Production pipelines (Databricks) |
| ORC | Columnar | Optimized for Hive/Hadoop | Legacy Hadoop stacks |

Key takeaway: **use Parquet or Delta for anything going into a pipeline**. CSV/JSON only at the ingestion boundary.

---

### 4. Use Cases Defined per Stream

Each intern now has a defined use case that will be their north star through the internship. These are end-to-end projects that build progressively each month.

**Sanjeev - DE**

**Use Case: Smart Retail Analytics & AI-Powered Recommendation Engine**

A retail company operates both online and offline stores. They receive raw data from multiple sources — transactional databases, REST APIs, and flat files — and need an end-to-end data platform to power business reporting, customer intelligence, and an AI-assisted product recommendation system.

**Data Sources:**
- Customer & Orders DB → PostgreSQL (OLTP) — ingested via Python + SQLAlchemy
- Product catalog → REST API (paginated JSON) — ingested via Python Requests
- Store inventory & suppliers → CSV files (daily drops) — processed via Pandas / PySpark
- User clickstream / behavior → JSON logs — processed via PySpark

**Pipeline Stages:**

- **Stage 1 — Extract (Bronze):** Ingest from all sources into cloud storage (S3/Azure Blob), partitioned by ingestion date. Raw data stored as-is.
- **Stage 2 — Silver (Cleaning & Enrichment):** Remove nulls, duplicates, invalid records. Standardize timestamps and currency. Join orders → customers → products. Deduplicate using SQL Window Functions (ROW_NUMBER). Use CTEs for readable transformation logic.
- **Stage 3 — Data Modeling:** Design a Star Schema (fact_orders + dim_customer, dim_product, dim_date, dim_store). Load into a cloud warehouse (Snowflake / BigQuery / Redshift).
- **Stage 4 — Gold Layer with dbt:** Build dbt models for business metrics — revenue by product, customer lifetime value, customer segments (High/Mid/Low), store performance, inventory health. Add dbt tests (not_null, unique, custom SQL).
- **Stage 5 — Scale with PySpark:** Re-implement Silver → Gold transformations in PySpark. Handle millions of rows with partitioning, caching. Compare Pandas vs PySpark for scale.
- **Stage 6 — Orchestration with Airflow:** Daily DAG at 10 AM — extract → silver → gold → dbt run → notify. Add retry logic, failure alerts, backfill support, data quality sensor tasks.
- **Stage 7 — AI Layer (RAG + Vector DB):** Embed product descriptions → store in Pinecone or pgvector. Build a RAG pipeline for semantic product search and personalized recommendations using purchase history.
- **Stage 8 — CI/CD & Production Hardening:** GitHub Actions pipeline (lint → test → staging → prod). Environment-based dbt profiles. Bash scripts for health checks and backfills. Full documentation and architecture diagram.


**Approach 1 — Cloud Native:** Python → S3/Azure Blob → Snowflake/BigQuery → dbt → Airflow → pgvector/Pinecone → GitHub Actions

**Approach 2 — PySpark Stack:** Python + PySpark → Parquet/HDFS → PostgreSQL or Databricks → dbt → Airflow (local) → pgvector → GitHub Actions


**Vinod - DA**

SQL Internship - Setup and Week 1 Tasks

1. SQL Setup Steps
   - Install Microsoft SQL Server 2019 Developer Edition.
   - Install SQL Server Management Studio (SSMS).
   - Download the AdventureWorks sample database backup file (.bak).
   - Open SSMS and connect to the SQL Server instance.
   - Right click on Databases and select Restore Database.
   - Choose Device and select the downloaded .bak file.
   - Complete the restore process and create the database.
   - Run a sample query to confirm the setup is working.

2. Week 1 SQL Practice Questions
   - Get all records where FirstName starts with A and ends with n
   - Find people whose LastName length is more than 6 characters
   - Get records where FirstName contains ar but not at the start
   - Fetch records where FirstName is exactly 5 characters long
   - Find people where FirstName is equal to LastName
   - Get records where FirstName has no vowels
   - Find people whose LastName starts with same letter as FirstName
   - Get records where FirstName starts with M and LastName ends with r
   - Find people where FirstName starts with J or LastName starts with S but BusinessEntityID is less than 100
   - Get records where FirstName contains a and does not contain e
   - Find people where FirstName starts with A or B and LastName contains son
   - Find names where second letter is a
   - Find names where third letter is r
   - Get names where FirstName starts and ends with same letter
   - Find names that contain exactly one a
   - Get names that contain at least two a characters
   - Find records where FirstName is in John, David, Mary and BusinessEntityID is between 50 and 200
   - Get records where FirstName is not in James, Robert and LastName starts with B
   - Find people where BusinessEntityID is between 10 and 100 and FirstName starts with a vowel
   - Get records where ID is between 1 and 300 but exclude even numbers
   - Find people where FirstName starts with S and LastName ends with n or contains ar
   - Get records where FirstName starts with a vowel and LastName does not start with a vowel
   - Find people where FirstName length is greater than 5 and LastName length is less than 5
   - Get records where FirstName contains a and LastName contains e and BusinessEntityID is less than 150
   - Find people where FirstName starts with A or LastName ends with e and FirstName does not contain z and BusinessEntityID is between 10 and 200
   - Find people where FirstName has exactly two vowels and LastName starts with same letter as FirstName and ID is not between 50 and 100
   - Find people where FirstName contains ar only once and LastName length is greater than FirstName length


**Vivek - ML**
TBU

---

### Action Items for Next Session

| # | Task | Who |
|---|------|-----|
| 1 | Read about distributed systems, distributed engines, and file formats. Prepare an architecture diagram of how Spark works (driver, workers, partitioning, fault tolerance) — explain it to the group. | All interns |
| 2 | Sign up for a trial platform of your choice (Azure/AWS/Databricks/Snowflake). Report back which platform you chose. | All interns |
| 3 | Start on Stage 1 of your assigned use case using the chosen platform. | DE / DevOps interns |
| 4 | Sanjeev to refine the use case document and share the repo with the group. | Sanjeev |
| 5 | Sanjeev to update DevOps and ML use case sections. | Sanjeev |
| 6 | Continue midweek check-in among yourselves. Drop blockers/questions in Slack. | All interns |

---

## Session 1 — March 21, 2026

**Attendees:** Sanjeev Kumar (mentor), Suhash Raja, Filip Cedermark, Deepika Elangovan, Neha Doda, Kousalya (organizer)

**Agenda:**
1. Introductions (experience, expectations, fun fact)
2. Structure of sessions — discussion
3. Common session plan for all streams

**Notes:**

Session structure agreed:
- Saturday 1-hour sessions (mentors unavailable on weekdays)
- First month: common sessions for all streams covering foundational topics
- 4 streams planned: DA, DE, DevOps/Infra, ML/Analytics

Intern introductions & stream assignments:

- **Suhash Raja** — Major: DE + DevOps. 10 yrs IT (PL/SQL, Splunk, Docker, Terraform, GitHub Actions). Databricks Associate certified.
- **Filip Cedermark** — Major: Data Engineering. Vocational AI/ML school, 17-week internship at Postnode (PySpark/Databricks), consulting bootcamp.
- **Deepika Elangovan** — Major: DE + DevOps. 4 yrs DevOps at Accenture (Azure, CI/CD, Terraform, Kubernetes). Wants to expand into DE.
- **Neha Doda** — Major: DA (primary), interested in DA + DE combo. Power BI, PL-300 certified (Jan 2026), end-to-end BI background.

Key discussion points:
- AI philosophy: build foundational knowledge first, use AI as a companion — not vibe-coding from day one
- AI impact on DA roles discussed (Databricks Genie/AI BI); Neha's DA + DE combo recommended as a strong skillset
- Vinod (mentor) intro not completed — transcript cut off
