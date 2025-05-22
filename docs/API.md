# API Documentation

This document outlines the API endpoints for the Synergy Tutor pilot.

## Authentication and Authorization

All endpoints require authentication via the school's Single Sign-On (SSO) system, managed through Supabase Auth. Each request must include an `Authorization: Bearer <token>` header. Row-Level Security (RLS) enforces the following rules:

* Students may only access their own chat sessions and summaries.
* Teachers may access data for students in their assigned classes.
* Service accounts performing background jobs may authenticate via API keys.

## Endpoints

### Chat API

* **POST /api/chat**
  * **Description**: Streams responses from the OpenAI API after PII stripping.
  * **Request Body**:

    ```json
    {
      "student_id": "abc123",
      "session_id": "95e723b0-0e27-4e3c-89bd-b4a609a111e4",
      "prompt": "Explain the water cycle."
    }
    ```
  * **Response**: Stream of chat completion tokens. When assembled, the final payload resembles:

    ```json
    {
      "session_id": "95e723b0-0e27-4e3c-89bd-b4a609a111e4",
      "message": "The water cycle describes ..."
    }
    ```
  * **Error Codes**:
    * `400 Bad Request` – malformed or missing fields in the request body.
    * `401 Unauthorized` – missing or invalid bearer token.
    * `403 Forbidden` – user is not allowed to access the specified session.
    * `500 Internal Server Error` – unexpected failure during processing.
    * `503 Service Unavailable` – OpenAI API or downstream service unavailable.

### Summary API

* **GET /summary/{student_id}**
  * **Description**: Returns last-week highlights and rubric scores for a given student.
  * **Path Parameters**: `student_id` (string, required)
  * **Response Body**:

    ```json
    {
      "student_id": "abc123",
      "week": "2024-05-13",
      "highlights": [
        "Completed multiplication practice session.",
        "Participated actively in group chat."
      ],
      "scores": {
        "reading_level": 4.2,
        "engagement": 7,
        "empathy": 8
      }
    }
    ```
  * **Error Codes**:
    * `401 Unauthorized` – missing or invalid token.
    * `403 Forbidden` – requester does not have permission to view this student.
    * `404 Not Found` – summary data for the given student ID is unavailable.
    * `500 Internal Server Error` – failure retrieving summary.

*(Further endpoints to be added as developed)*
