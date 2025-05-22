# Database Schema

This document details the database schema for the Synergy Tutor pilot, hosted on Supabase (PostgreSQL).

## Tables

### `StudentChats`
*   **Description**: Stores every turn of conversation between students and the AI tutor.
*   **Columns**:
    *   `student_id` (TEXT, Foreign Key to Students/Users table, Not Null) - Identifier from SSO.
    *   `session_id` (UUID, Not Null) - Unique identifier for a chat session.
    *   `timestamp` (TIMESTAMPTZ, Not Null, Default: `now()`) - Timestamp of the chat turn.
    *   `actor` (TEXT, Not Null) - Indicates who generated the message (e.g., 'user', 'ai').
    *   `message_text` (TEXT) - The actual content of the chat message (PII-stripped for AI turns if necessary before sending to OpenAI).
    *   `original_message_text` (TEXT, Nullable) - Optional: Stores the original user message before PII stripping, accessible only under strict RLS.
    *   `token_count` (INTEGER, Nullable) - Number of tokens in the message (user or AI).
    *   `reading_level` (FLOAT, Nullable) - Calculated reading level for the session/turn.
    *   `topic_code` (TEXT, Nullable) - Code or tag for the primary topic of discussion.
    *   `other_analytics_tags` (JSONB, Nullable) - For any other structured analytics data.
*   **Row-Level Security (RLS)**:
    *   Students can only access their own chat history.
    *   Teachers can only access chat histories of students in their assigned classes.
    *   PII-stripped data might have different access rules if sent to external services.

### `TeacherNotes`
*   **Description**: Stores notes or feedback teachers make, potentially linked to students or sessions.
*   **Columns**:
    *   `note_id` (UUID, Primary Key, Default: `gen_random_uuid()`)
    *   `teacher_id` (TEXT, Foreign Key to Teachers/Users table, Not Null) - Identifier from SSO.
    *   `student_id` (TEXT, Foreign Key to Students/Users table, Nullable) - If the note is about a specific student.
    *   `session_id` (UUID, Foreign Key to `StudentChats.session_id`, Nullable) - If the note is about a specific chat session.
    *   `timestamp` (TIMESTAMPTZ, Not Null, Default: `now()`)
    *   `note_text` (TEXT, Not Null)
*   **Row-Level Security (RLS)**:
    *   Teachers can only access/edit their own notes.
    *   School administrators might have broader access for oversight.

*(Other tables like `Students`, `Teachers`, `Classes`, `ClassEnrollments` would be needed to support the RLS and application logic, typically managed by the SSO integration or Supabase Auth.)*
