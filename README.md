# Audio and Video Intelligence Platform

![Data Engineer](https://github.com/AtharvaGitProfile/Databricks-ML-Platform/blob/main/DB.png)

---

## The Problem

Organizations are sitting on thousands of hours of recorded content. Sales calls, training videos, lectures, meetings. Almost none of it is searchable. Almost none of it is analyzed. It exists as files on a server, delivering no value after the moment it was recorded.

The people who need answers have to watch entire videos to find a single insight. Analytics teams have no reliable way to understand which content performs, which topics generate the most questions, or where audiences drop off. And when someone new joins the team, the institutional knowledge locked in that content library is effectively invisible to them.

This platform changes that.

---

## What It Delivers

Demonstrated using YouTube video content, this platform automatically ingests video, transcribes it using AI, and processes it into clean structured data that powers two things:

**A content analytics mart** so teams can understand video performance, engagement patterns, and content gaps through reliable, always-fresh data.

**An AI assistant trained on the actual content** so users can ask questions in plain language and get answers sourced directly from the video library rather than generic internet results.

The same architecture works for any organization with audio or video content: training libraries, recorded calls, lectures, or meeting archives.

---

## Architecture Diagram

![Pipeline](./diagram.png)

Data flows through three progressively cleaner layers before reaching end users.

**Bronze** is raw ingestion. Video metadata and AI-generated transcriptions land in S3 exactly as received, nothing discarded, with a full audit trail preserved.

**Silver** is where Databricks and Spark go to work. Formats are standardized, duplicates resolved, schemas enforced, and data quality validated before anything moves forward.

**Gold** is the business-ready layer. dbt transforms clean data into a structured analytics mart with normalized tables, business metrics, and content dimensions that analysts and the AI model can trust and query directly.

---

## The Data Journey

An Airflow pipeline runs automatically on a schedule, hitting the YouTube API to collect video metadata including titles, descriptions, view counts, likes, comments, and engagement timestamps. At the same time, OpenAI Whisper transcribes the video audio into text. Both land in S3, metadata as JSON and transcriptions as Parquet files.

The moment new data arrives in S3, an AWS Lambda trigger fires automatically and kicks off the Databricks processing layer. Spark jobs clean the raw data by flattening nested JSON structures, removing duplicates, enforcing consistent schemas, and running quality checks. No manual intervention needed.

Clean data then flows into dbt Cloud where it is modeled into a Snowflake schema with facts and dimensions normalized to 3NF. Automated dbt tests catch data freshness issues, broken relationships, and unexpected nulls before anything reaches end users.

Finally, the processed transcriptions are used to fine-tune a Large Language Model on the specific content in the video library. A Django application deployed on AWS ECS serves as the inference layer, letting users ask questions and get answers grounded in the actual content rather than generic responses.

---

## Key Engineering Decisions

**Why dbt for the transformation layer instead of continuing with Spark?**
Spark transformations live in code that only engineers can read or modify. dbt models are SQL that any analyst can audit, every transformation is version controlled, and tests run automatically on every deployment. For the analytics mart where business users need to trust the data, dbt's transparency and built-in testing made it the right choice.

**Why event-driven ingestion with S3 triggers instead of scheduled polling?**
A scheduled job that checks for new data wastes compute and introduces unnecessary latency. S3 event triggers mean the pipeline reacts the moment data arrives, which means faster processing, lower cost, and no wasted cycles checking an empty bucket.

**Why build a custom dataset instead of using a public one?**
Pre-cleaned public datasets do not reflect real engineering challenges. Building from raw YouTube API responses meant dealing with nested dictionaries, inconsistent formats, missing fields, and schema drift. These are the actual problems data engineers face in production environments.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Infrastructure as Code | Terraform, Ansible |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Orchestration | Apache Airflow |
| Cloud Storage and Eventing | AWS S3, Lambda, Kinesis, API Gateway |
| Data Processing | Databricks, PySpark, Spark SQL |
| Transformation and Modeling | dbt Cloud |
| AI Transcription | OpenAI Whisper |
| LLM Fine-tuning | LangChain, Hugging Face |
| Application Layer | Django on AWS ECS |
| Analytics | AWS Athena |

---

## Project Structure

```
├── handlers-airflow/     # Terraform, Ansible, Airflow DAGs, Docker Compose
├── databricks/           # PySpark and Spark SQL transformation jobs
├── app_dbt/              # dbt Cloud models, tests, and documentation
├── aws/                  # Lambda functions, Kinesis config, Glue jobs
├── application/          # Django app, ECS Terraform, Docker setup
├── data/                 # Sample data across Bronze, Silver, and Gold layers
└── samples/              # Output samples from each pipeline stage
```

---

## Roadmap

- Deploy LLM inference via AWS SageMaker with Hugging Face PEFT techniques
- Add Streamlit front-end for the user-facing Q&A interface
- Integrate Power BI or Looker for content analytics dashboards
- Enable real-time streaming with Spark Structured Streaming and Kafka
- Explore data contracts for schema enforcement at the ingestion boundary

---

## About

Built by **Atharva Patil**, a data engineer with experience across financial data, healthcare claims processing, and edtech platforms. This project reflects a production-minded approach to data engineering: reliable pipelines, tested transformations, and data that business users can trust.

[LinkedIn](#) · [GitHub](https://github.com/AtharvaGitProfile)
