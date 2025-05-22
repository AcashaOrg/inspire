# Potential Dependencies

This document lists potential technologies, libraries, and services that may be used in the Synergy Tutor pilot project, based on the initial blueprint. This is not an exhaustive list and will evolve as development progresses.

## Core Application Stack

*   **Frontend (Prototyping & Production)**:
    *   **Prototyping**:
        *   [Bubble](https://bubble.io/): For rapid UI/UX validation.
    *   **Production**:
        *   [React](https://reactjs.org/): JavaScript library for building user interfaces.
        *   [Next.js](https://nextjs.org/): React framework for production (SSR, SSG, routing, etc.).
*   **Backend API**:
    *   **Option 1 (Python)**:
        *   [FastAPI](https://fastapi.tiangolo.com/): Modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
    *   **Option 2 (Node.js)**:
        *   [Node.js](https://nodejs.org/): JavaScript runtime environment.
        *   [tRPC](https://trpc.io/): End-to-end typesafe APIs made easy. (Often used with Next.js)
        *   [Express.js](https://expressjs.com/) (Alternative if not using tRPC): Minimal and flexible Node.js web application framework.
*   **Database & BaaS**:
    *   [Supabase](https://supabase.com/): Open source Firebase alternative. Provides:
        *   PostgreSQL database
        *   Authentication (for SSO integration)
        *   Row-Level Security
        *   Storage
        *   Realtime capabilities
    *   [AWS RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/) (Alternative): If more direct control over the PostgreSQL instance is needed and Supabase's BaaS features are less critical.

## AI & Machine Learning

*   **LLM Provider**:
    *   [OpenAI API](https://beta.openai.com/docs): For chat completions (e.g., GPT-4o, GPT-3.5-turbo).
        *   `openai` (Python/Node.js client libraries).
*   **Background Worker (Python)**:
    *   [Celery](https://docs.celeryq.dev/): Distributed task queue (if complex background processing is needed).
    *   Simpler Python script with `requests` or `httpx` for API calls, potentially run as a scheduled job (e.g., cron, serverless function).

## Identity & Authentication

*   **Single Sign-On (SSO)**:
    *   Libraries/SDKs for Google Workspace for Education integration.
    *   Libraries/SDKs for Microsoft Entra (formerly Azure AD) integration.
    *   Supabase Auth can facilitate these integrations.

## Teacher Dashboard (Low-Code MVP)

*   **Option 1**: [Retool](https://retool.com/): Build internal tools, remarkably fast.
*   **Option 2**: [Appsmith](https://www.appsmith.com/): Open-source framework to build internal tools.

## Automation & Integration (Peripheral)

*   [n8n](https://n8n.io/): Extendable workflow automation.
*   [Zapier](https://zapier.com/): Easy automation for busy people.

## Development & Operations

*   **Version Control**: [Git](https://git-scm.com/)
*   **Hosting (Frontend/Full-stack)**:
    *   [Vercel](https://vercel.com/): Platform for frontend frameworks and static sites (good synergy with Next.js).
    *   [Netlify](https://www.netlify.com/): Alternative for frontend/full-stack hosting.
*   **Hosting (Backend API - if separate)**:
    *   Serverless functions (e.g., AWS Lambda, Google Cloud Functions, Vercel Functions).
    *   Containerization (e.g., Docker) on platforms like AWS ECS, Google Cloud Run, or DigitalOcean App Platform.
*   **Containerization (Optional)**:
    *   [Docker](https://www.docker.com/): For consistent development and deployment environments.

## Compliance & Security

*   Consider libraries or tools for PII detection/stripping if not handled manually or by an external service.

This list should be reviewed and refined as technical decisions are made for each component of the project.
