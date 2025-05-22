# Synergy Tutor - Pilot Blueprint

This document outlines the blueprint for a 30-student "Synergy Tutor" pilot program, designed to be practical and FERPA-safe.

## 1. Account & Chat-History Setup (Student Side)

### Identity
*   **Requirement**: Utilize the school’s existing Single Sign-On (SSO) solution (e.g., Google Workspace for Education or Microsoft Entra).
*   **Rationale**: Avoids storing raw passwords, enhancing security and simplifying user management.

### Conversation Store
*   **Requirement**: Every turn of the conversation (user input + AI response) must be written to a `StudentChats` table.
*   **Key Fields**: `student_id`, `session_id`, `timestamp`.
*   **Anonymization**: Data should be stripped of Personally Identifiable Information (PII) before being forwarded to the OpenAI Chat Completions API.

### Analytics Tags
*   **Requirement**: Implement a background worker to process chat sessions.
*   **Generated Data**: Columns such as `reading_level`, `topic_code`, `token_count`.
*   **Method**: Summarize each session using a cost-effective, one-shot GPT-4o call.

### Privacy Gate
*   **Requirement**: Store logs in a FERPA-compliant PostgreSQL database (e.g., Supabase or AWS RDS).
*   **Security**: Implement Row-Level Security (RLS) to ensure only teachers associated with a specific class can read the logs for their students.
*   **References/Inspiration**: Edutopia, jlpp.org.
*   **Outcome**: Each student maintains a complete chat history that their teacher can review and grade. OpenAI interactions are anonymized, protecting student privacy.

## 2. Teacher Dashboard

(This component can be developed separately, prioritizing a low-code Minimum Viable Product initially.)

### Backend API
*   **Technology Options**: FastAPI (Python) or Node.js (with tRPC).
*   **Example Endpoint**: `/summary/{student_id}` should return highlights from the last week and corresponding rubric scores.

### Database
*   **Technology**: Supabase (leveraging its auth, PostgreSQL, and row-level security features).
*   **Purpose**: Centralized storage for chat logs, analytical metrics, and lesson plans.

### Dashboard UI
*   **MVP Approach**: Retool or Appsmith.
*   **Long-term Vision**: Transition to React/Next.js once the pilot demonstrates value.
*   **Functionality**:
    *   Display a list of classes.
    *   Allow selection of a student from a class.
    *   Show a detailed view including:
        *   Chat timeline.
        *   Reading-level graph.
        *   Empathy-score trend.
*   **Development Strategy**: Start with low-code tools for rapid deployment and validation, then harden the solution with a custom React frontend hosted on a platform like Vercel.

## 3. API-Driven vs. "Platform" Dependency

### Pure API Stack (OpenAI API + Supabase + Custom UI)
*   **Pros**:
    *   Full control over the technology stack.
    *   White-label branding opportunities.
    *   Extensible to other "Doctrine Layers" and subjects.
*   **Cons**:
    *   Requires self-management of infrastructure and compliance.
*   **When to Choose**: When maximum control, customization, and extensibility are primary goals.

### Automation Tools
*   **Usage**: Keep automation tools like n8n or Zapier at the periphery of the core system.
*   **Examples**:
    *   Nightly export of grades to the school's Student Information System (SIS).
    *   Email alerts to teachers when a student's comprehension level drops below a predefined threshold.

## Roll-out Checklist (7 Sprint Tasks)

1.  **Create Supabase Project**:
    *   Enable Row-Level Security (RLS).
    *   Define `StudentChats` and `TeacherNotes` tables.
2.  **Prototype Chat UI**:
    *   Use React or Bubble.
    *   Hook into an `/api/chat` endpoint that streams responses from the OpenAI API.
3.  **Develop Background Worker**:
    *   Use Python.
    *   Summarize each chat session and update relevant metrics in the database.
4.  **Build Retool Dashboard**:
    *   Connect to the Supabase data store.
    *   Implement "Class List → Student Selection → Detail View" user flow.
5.  **Create FERPA Policy Document**:
    *   Share with the school administration.
    *   Detail data retention policies, encryption methods, and parent access rights.
6.  **Load Test Accounts**:
    *   Add 30 test student accounts via SSO.
    *   Run a mock lesson to verify that logs are generated and metrics are calculated correctly.
7.  **Conduct Teacher Training**:
    *   Schedule a 60-minute Zoom session.
    *   Cover dashboard usage and best practices for prompt hygiene.

## Setup

For installation and configuration, see [docs/SETUP.md](docs/SETUP.md).

## Contributing

Guidelines for contributing can be found in [CONTRIBUTING.md](CONTRIBUTING.md).

## Additional Documentation

* API reference: [docs/API.md](docs/API.md)
* Database schema: [docs/DATABASE.md](docs/DATABASE.md)

## License

This project is licensed under the [Apache 2.0](LICENSE) license.
