# API Documentation

This document outlines the API endpoints for the Synergy Tutor pilot.

## Authentication

*   Details on how API authentication is handled (e.g., SSO token passthrough, API keys for service accounts).

## Endpoints

### Chat API

*   **POST /api/chat**
    *   **Description**: Streams responses from the OpenAI API, after PII stripping.
    *   **Request Body**: [Details of the request payload, e.g., `{ "student_id": "...", "session_id": "...", "prompt": "..." }`]
    *   **Response**: Streamed response from OpenAI.
    *   **Error Codes**: [List potential error codes and their meanings]

### Summary API

*   **GET /summary/{student_id}**
    *   **Description**: Returns last-week highlights and rubric scores for a given student.
    *   **Path Parameters**: `student_id` (string, required)
    *   **Response Body**: [Details of the response payload, e.g., `{ "highlights": [...], "scores": [...] }`]
    *   **Error Codes**: [List potential error codes]

*(Further endpoints to be added as developed)*
