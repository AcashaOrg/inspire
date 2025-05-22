# Backend

This folder contains the server-side code for the Synergy Tutor pilot. The current setup uses a minimal [FastAPI](https://fastapi.tiangolo.com/) app as a starting point.

## Running Locally

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

This will serve the API at `http://localhost:8000/`.
