# Setup Instructions

This document provides instructions for setting up the Synergy Tutor pilot project.

## Prerequisites

*   **Node.js**: version 18.x or higher
*   **Python**: version 3.10 or higher
*   **Supabase**: active account with a new project

## Backend Setup

1. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies (example FastAPI stack):
   ```bash
   pip install fastapi uvicorn openai supabase
   ```
3. Start the API server:
   ```bash
   uvicorn main:app --reload
   ```

## Frontend Setup (Prototyping - Bubble/React)

*Option 1: Bubble*

1. Create a new Bubble app and connect it to the backend API endpoints.

*Option 2: React*

1. Bootstrap the project and install packages:
   ```bash
   npx create-react-app frontend
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm start
   ```

## Database Setup (Supabase)

1. In the Supabase dashboard, create a new project.
2. Enable Row-Level Security (RLS) on your tables.
3. Create the `StudentChats` and `TeacherNotes` tables as described in
   [`docs/DATABASE.md`](DATABASE.md).
4. Copy your project URL and API keys from **Project Settings → API** for use in
   environment variables.

## Environment Variables

Set the following variables in a `.env` file (see `.env.example`):

* `OPENAI_API_KEY` – API key for OpenAI requests.
* `SUPABASE_URL` – URL of your Supabase project.
* `SUPABASE_SERVICE_ROLE_KEY` – service role key used by the backend.
* `NEXT_PUBLIC_SUPABASE_URL` – same as `SUPABASE_URL` but exposed to the
  frontend.
* `NEXT_PUBLIC_SUPABASE_ANON_KEY` – Supabase anon key for client-side requests.
