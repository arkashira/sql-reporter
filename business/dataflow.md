# Dataflow
## Overview
The sql-reporter dataflow architecture is designed to provide a scalable and secure platform for business users to generate reports and insights from various data sources.

## Architecture
```markdown
                                      +---------------+
                                      |  External    |
                                      |  Data Sources  |
                                      +---------------+
                                             |
                                             |
                                             v
                                      +---------------+
                                      |  Ingestion    |
                                      |  Layer        |
                                      |  (API Gateway,|
                                      |   AWS Glue,    |
                                      |   Apache Beam) |
                                      +---------------+
                                             |
                                             |
                                             v
                                      +---------------+
                                      | Processing/  |
                                      | Transform     |
                                      | Layer         |
                                      | (Apache Spark,|
                                      |  AWS Lambda)  |
                                      +---------------+
                                             |
                                             |
                                             v
                                      +---------------+
                                      |  Storage Tier  |
                                      |  (Data Warehouse|
                                      |   AWS Redshift, |
                                      |   Apache Cassandra|
                                      |   Auth: IAM Roles)|
                                      +---------------+
                                             |
                                             |
                                             v
                                      +---------------+
                                      | Query/Serving |
                                      | Layer          |
                                      | (SQL Engine,   |
                                      |  Apache Presto, |
                                      |  AWS Athena)    |
                                      |  Auth: JWT Tokens|
                                      +---------------+
                                             |
                                             |
                                             v
                                      +---------------+
                                      |  Egress to User |
                                      |  (Web Application|
                                      |   API Gateway,  |
                                      |   Auth: OAuth 2.0)|
                                      +---------------+
```

## Components
* **External Data Sources**
  + Relational databases (e.g., MySQL, PostgreSQL)
  + NoSQL databases (e.g., MongoDB, Cassandra)
  + Cloud storage (e.g., AWS S3, Google Cloud Storage)
* **Ingestion Layer**
  + API Gateway (e.g., AWS API Gateway, Google Cloud Endpoints)
  + Data ingestion tools (e.g., AWS Glue, Apache Beam)
  + Authentication: API keys, OAuth 2.0
* **Processing/Transform Layer**
  + Data processing engines (e.g., Apache Spark, AWS Lambda)
  + Data transformation tools (e.g., Apache NiFi, AWS Glue)
  + Authentication: IAM Roles, Service Accounts
* **Storage Tier**
  + Data warehouses (e.g., AWS Redshift, Google BigQuery)
  + NoSQL databases (e.g., Apache Cassandra, MongoDB)
  + Authentication: IAM Roles, Service Accounts
* **Query/Serving Layer**
  + SQL engines (e.g., Apache Presto, AWS Athena)
  + Query optimization tools (e.g., Apache Calcite, AWS Lake Formation)
  + Authentication: JWT Tokens, OAuth 2.0
* **Egress to User**
  + Web applications (e.g., React, Angular)
  + API Gateways (e.g., AWS API Gateway, Google Cloud Endpoints)
  + Authentication: OAuth 2.0, OpenID Connect

## Auth Boundaries
* Ingestion Layer: API keys, OAuth 2.0
* Processing/Transform Layer: IAM Roles, Service Accounts
* Storage Tier: IAM Roles, Service Accounts
* Query/Serving Layer: JWT Tokens, OAuth 2.0
* Egress to User: OAuth 2.0, OpenID Connect

Note: The auth boundaries are designed to provide a secure and scalable architecture, with clear separation of concerns and minimal attack surface.