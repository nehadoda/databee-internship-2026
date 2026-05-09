# Use Case — Data Analytics

**Track Lead:** Vinod

---

## SQL Internship — Setup and Week 1 Tasks

---

## Setup Steps

1. Install Microsoft SQL Server 2019 Developer Edition.
2. Install SQL Server Management Studio (SSMS).
3. Download the AdventureWorks sample database backup file (`.bak`).
4. Open SSMS and connect to the SQL Server instance.
5. Right-click on Databases and select **Restore Database**.
6. Choose **Device** and select the downloaded `.bak` file.
7. Complete the restore process and create the database.
8. Run a sample query to confirm the setup is working.

---

## Week 1 — SQL Practice Questions

Work against the **AdventureWorks** database (`Person.Person` table).

1. Get all records where `FirstName` starts with `A` and ends with `n`
2. Find people whose `LastName` length is more than 6 characters
3. Get records where `FirstName` contains `ar` but not at the start
4. Fetch records where `FirstName` is exactly 5 characters long
5. Find people where `FirstName` is equal to `LastName`
6. Get records where `FirstName` has no vowels
7. Find people whose `LastName` starts with same letter as `FirstName`
8. Get records where `FirstName` starts with `M` and `LastName` ends with `r`
9. Find people where `FirstName` starts with `J` or `LastName` starts with `S` but `BusinessEntityID` is less than 100
10. Get records where `FirstName` contains `a` and does not contain `e`
11. Find people where `FirstName` starts with `A` or `B` and `LastName` contains `son`
12. Find names where second letter is `a`
13. Find names where third letter is `r`
14. Get names where `FirstName` starts and ends with same letter
15. Find names that contain exactly one `a`
16. Get names that contain at least two `a` characters
17. Find records where `FirstName` is in `John`, `David`, `Mary` and `BusinessEntityID` is between 50 and 200
18. Get records where `FirstName` is not in `James`, `Robert` and `LastName` starts with `B`
19. Find people where `BusinessEntityID` is between 10 and 100 and `FirstName` starts with a vowel
20. Get records where ID is between 1 and 300 but exclude even numbers
21. Find people where `FirstName` starts with `S` and `LastName` ends with `n` or contains `ar`
22. Get records where `FirstName` starts with a vowel and `LastName` does not start with a vowel
23. Find people where `FirstName` length is greater than 5 and `LastName` length is less than 5
24. Get records where `FirstName` contains `a` and `LastName` contains `e` and `BusinessEntityID` is less than 150
25. Find people where `FirstName` starts with `A` or `LastName` ends with `e` and `FirstName` does not contain `z` and `BusinessEntityID` is between 10 and 200
26. Find people where `FirstName` has exactly two vowels and `LastName` starts with same letter as `FirstName` and ID is not between 50 and 100
27. Find people where `FirstName` contains `ar` only once and `LastName` length is greater than `FirstName` length

---

## Week 2 — Dashboarding (Mid-Advanced)

> Assumes interns are already comfortable connecting to data sources and building basic visuals. Each exercise is framed as a concept — implement using whichever tool you use (Power BI, Tableau, or Looker Studio).

---

### Concept 1 — Building Calculated Metrics (not just aggregations)

*Real dashboards don't just sum columns — they compute business KPIs that mean something to the stakeholder.*

- Define 3–4 metrics in your tool's calculation layer:
  - Total Sales, Average Order Value, Sales per Customer
  - YoY % change, MoM % change
- The point: understand the difference between a raw field and a *defined metric* — and why centralising metric definitions matters (one source of truth, not per-report recalculations)

| Tool | How |
|------|-----|
| Power BI | DAX measures in the model |
| Tableau | Calculated fields in the data pane |
| Looker Studio | Calculated fields in the data source |

---

### Concept 2 — Time Intelligence

*"Show me this month vs last month vs same period last year" — every customer asks this.*

- Build a date-aware trend visual showing current year vs prior year on the same axis
- Add period selectors (month / quarter / year) that update all visuals simultaneously
- Key question to answer: how does your tool handle a missing date dimension?

| Tool | How |
|------|-----|
| Power BI | `SAMEPERIODLASTYEAR`, `TOTALYTD` DAX functions + Date table |
| Tableau | Built-in date parts + table calculations (`LOOKUP`, `WINDOW_SUM`) |
| Looker Studio | Date range controls + `SAME_PERIOD_LAST_YEAR` comparison |

---

### Concept 3 — Actual vs Target / Variance

*Every ops, sales, and finance team tracks performance against a plan.*

- Create a small target table manually (one target per territory or month) and join it to the sales data
- Build a visual showing actual, target, and variance % side by side
- Add a status indicator — green/amber/red based on a variance threshold

| Tool | How |
|------|-----|
| Power BI | Blend via data model relationship + DAX variance measure + KPI visual |
| Tableau | Data blending or union + reference lines + calculated field for variance |
| Looker Studio | Blend data sources + scorecard with comparison |

---

### Concept 4 — Audience-Layered Design (Summary → Detail)

*A single report must serve an exec and an analyst. Drill-through is the pattern.*

- Build a 2-page report:
  - Page 1: Executive summary — 3–4 KPI cards, one trend, one ranking
  - Page 2: Detail view — full table, filters, breakdowns
- Wire up navigation so clicking a dimension on Page 1 takes you to filtered detail on Page 2
- Discuss: when to use drill-through vs tooltips vs separate reports

| Tool | How |
|------|-----|
| Power BI | Drill-through pages + back button |
| Tableau | Dashboard actions (filter action between sheets) |
| Looker Studio | Page navigation + report-level filter passing |

---

### Concept 5 — Access Control (who sees what)

*Non-negotiable in enterprise. Data teams get asked this before go-live on every project.*

- Define at least 2 roles with different data visibility (e.g. by territory or region)
- Test that each role sees only its own data
- Discuss: static roles vs dynamic (username-based) — when each applies

| Tool | How |
|------|-----|
| Power BI | Manage Roles (static) or `USERPRINCIPALNAME()` (dynamic) |
| Tableau | Row-level security via user filters or entitlement tables |
| Looker Studio | No native RLS — discuss as a limitation; workaround via separate reports or data source filters |
