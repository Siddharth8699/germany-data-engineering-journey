# 🎓 Student Application Tracking & Analytics Engine

A production-grade Relational Database Management System (RDBMS) and Python Command-Line Interface (CLI) built to track, monitor, and analyze student job application lifecycles. 

This project is built following a structured, long-term engineering blueprint to master backend architectures, clean relational schema designs, complex SQL analytics, and data pipeline workflows.

---

## 🗺️ Project Architecture & Evolution Roadmap

This system is designed to grow in architectural depth over time rather than remaining a static codebase. 

📖 **[Click here to view the complete, detailed Project Blueprint PDF](./docs/Roadmap.pdf)**

### 📍 Phase Timeline Summary:
* **Phase 1: Relational Foundation & CLI Engine** (Current Milestone Met)
  * Implemented a normalized 4-table database layout, raw transactional queries, modular file branching, and a interactive terminal control dashboard.
* **Phase 2: Relational Analytics Layer** (In Progress)
  * Integrated 22 business intelligence metrics, complex multi-table joins, subqueries, and macroeconomic industry-level data aggregations.
* **Phase 3: Object-Relational Mapping (ORM) & Robust Migrations**
  * Transitioning raw SQL strings into maintainable SQLAlchemy/SQLModel structures paired with Alembic schema version tracking.
* **Phase 4: Programmatic ETL & Clean Ingestion Pipelines**
  * Automated external CSV parsing, data scrub rules, and batch-loading validation workflows utilizing Pandas.
* **Phase 5: RESTful API Layer & Service Containerization**
  * Migrating business logic into a high-performance FastAPI web framework and containerizing core services using Docker.

---

## 🚀 Quick Start & Database Replication

To spin up this entire ecosystem locally in less than 5 seconds, follow these steps:

### 1. Initialize the Database
* Open your PostgreSQL query tool (e.g., pgAdmin 4).
* Open and copy the contents of the master initialization script: **[`init.sql`](./init.sql)**.
* Execute the entire file. It will automatically sweep old tables, construct the normalized 4-table layout, ingest the custom seed dataset matrix, and evaluate all analytical reporting views.

### 2. Launch the Control Application
* Ensure your local database connection parameters match your configuration driver.
* Run the interactive CLI menu interface inside your terminal:
  ```bash
  python main.py