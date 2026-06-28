```markdown
# Technical Specification for SQL Reporter

## Stack
- **Language**: Python
- **Framework**: FastAPI
- **Runtime**: Docker

## Hosting
- **Free Tier**: Yes
- **Specific Platforms**: 
  - Heroku (for initial deployment)
  - AWS (for scaling)
  - DigitalOcean (as an alternative)

## Data Model
### Tables/Collections
1. **Users**
   - **Key Fields**:
     - `id`: UUID (Primary Key)
     - `username`: String (Unique)
     - `email`: String (Unique)
     - `password_hash`: String
     - `created_at`: Timestamp
     - `updated_at`: Timestamp

2. **Queries**
   - **Key Fields**:
     - `id`: UUID (Primary Key)
     - `user_id`: UUID (Foreign Key to Users)
     - `query_text`: String
     - `created_at`: Timestamp
     - `updated_at`: Timestamp

3. **Reports**
   - **Key Fields**:
     - `id`: UUID (Primary Key)
     - `query_id`: UUID (Foreign Key to Queries)
     - `report_data`: JSON
     - `created_at`: Timestamp
     - `updated_at`: Timestamp

## API Surface
1. **POST /api/users**
   - **Purpose**: Create a new user account.

2. **POST /api/users/login**
   - **Purpose**: Authenticate a user and return a session token.

3. **GET /api/users/{id}**
   - **Purpose**: Retrieve user profile information.

4. **POST /api/queries**
   - **Purpose**: Submit a new SQL query for processing.

5. **GET /api/queries/{id}**
   - **Purpose**: Retrieve the details of a submitted query.

6. **POST /api/reports**
   - **Purpose**: Generate a report from a submitted query.

7. **GET /api/reports/{id}**
   - **Purpose**: Retrieve a generated report.

8. **DELETE /api/queries/{id}**
   - **Purpose**: Delete a submitted query.

## Security Model
- **Authentication**: JWT (JSON Web Tokens) for user sessions.
- **Secrets Management**: Use AWS Secrets Manager for storing sensitive information (e.g., database credentials).
- **IAM**: Role-based access control (RBAC) for user permissions.

## Observability
- **Logs**: Implement structured logging using Python's `logging` module, with logs sent to AWS CloudWatch.
- **Metrics**: Use Prometheus for collecting metrics on API usage and performance.
- **Traces**: Integrate OpenTelemetry for distributed tracing of requests.

## Build/CI
- **CI/CD Pipeline**: 
  - Use GitHub Actions for continuous integration and deployment.
  - Automated tests for each pull request.
  - Deploy to Heroku on successful merges to the main branch.
```
