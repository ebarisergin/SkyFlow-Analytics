✈️ SkyFlow-Analytics: End-to-End Airline Operations & Delay Optimization

This project delivers a comprehensive, data-driven analysis of airline flight operations and delay patterns. Developed with an Industrial Engineering perspective, the system integrates a layered business intelligence and analytics pipeline: SQL for relational data architecture, Excel for structural verification, Power BI for dynamic executive dashboards, and Python for descriptive data profiling and risk categorization.

🛠️ Project Architecture & Workflow
The project ensures a seamless data flow from raw data extraction to programmatic decision support:

Relational Data Layer (SQL): Structured queries designed under a Star Schema design to extract operational KPIs and isolate bottlenecks.

Data Management & Verification (Excel): Normalized datasets (Flights, Airlines, Airports, Delays) utilizing Pivot Tables to validate seasonal performance metrics.

Programmatic Analytics (Python): Native looping, math tracking, and conditional structures applied to isolate and score critical operational risks.

Interactive BI Layer (Power BI): An executive dashboard monitoring operational health, route combinations, and delay categories.

🔍 1. SQL Layer (Relational Queries)
The SQL layer architecture structures the database using explicit entity-relationship linkages (INNER JOIN) and multi-level aggregations (GROUP BY, ORDER BY DESC) to address key business logic requirements:

Volume Tracking: Counts total global operations.

Status Distribution: Segregates flight execution across Completed and Delayed states.

Bottleneck Discovery: Isolates top-tier average delay times by specific commercial carriers and exact airport-to-airport routes.

💻 2. Python Analytics Layer
Using core Python constructs and foundational libraries, the Delay_Reasons_Data subset was programmatically evaluated. The logic computes descriptive baselines and loops through operational thresholds to isolate critical bottlenecks:

Descriptive Data Profiling: Computes the mathematical count, mean, minimum, and maximum boundaries of operational delays using describe().

Dynamic Threshold Logic: Utilizes a custom structural loop (for) embedded with conditional logic (if-elif-else) to classify delay risk metrics into granular severity bands:

Kritik Rötar: Delays exceeding 30 minutes.

Orta Derece Rötar: Delays spanning 15 to 30 minutes.

Normal / Zamanında: Delays under 15 minutes.

Operational Risk Indexing: Leverages counting logic variables to track severe performance anomalies, establishing that %75.76 of the delayed flights qualify as a Kritik Rötar.

# Segment of the threshold analysis script
for rotar_dakikasi in df["Delay_Minutes"]:
    if rotar_dakikasi > 30:
        kritik_rotarlar.append("Kritik Rötar")
    elif rotar_dakikasi > 15:
        kritik_rotarlar.append("Orta Derece Rötar")
    else:
        kritik_rotarlar.append("Normal / Zamanında")


📊 3. Power BI Executive Dashboard
The visual presentation environment translates data tables into high-impact operational visibility:

Strategic KPI Matrix: Instantly highlights global operational volume alongside average delay timelines.

Root-Cause Categorization: Employs precise visual grouping (Donut and Bar visuals) to break down performance statuses and primary delay causes (Weather, Air Traffic, Technical Issues).

Network & Node Intelligence: Implements matrix views mapping exact departure-to-arrival airport points to isolate systemic, chronic route delays for rapid continuous improvement (Kaizen) initiatives.