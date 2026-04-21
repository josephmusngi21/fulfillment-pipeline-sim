# fulfillment-pipeline-sim

Real-time simulation scaffold of a warehouse fulfillment and last-mile delivery pipeline, built with Python/FastAPI on the backend and React/TypeScript on the frontend.

## Project Architecture

- `backend/`
  - FastAPI application scaffold under `app/`
  - Simulation domain placeholders under `app/simulation/`
  - API router placeholders under `app/api/routers/`
  - Data model and schema placeholders under `app/models/` and `app/schemas/`
  - Alembic migration scaffold under `alembic/`
- `frontend/`
  - Vite + React + TypeScript scaffold
  - State, hooks, components, services, and type placeholders under `src/`
  - Tailwind CSS setup via `tailwind.config.ts`
- `docker-compose.yml`
  - Local development stack for PostgreSQL, backend API, and frontend app

## Local Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local backend runs outside Docker)
- Node.js 20+ and npm (for local frontend runs outside Docker)

### Run with Docker Compose

```bash
docker compose up --build
```

Services:
- Backend API: `http://localhost:8000`
- Frontend app: `http://localhost:5173`
- Postgres: `localhost:5432`

### Run Backend Locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Run Frontend Locally

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

## Notes

This repository currently contains scaffold-only files with TODO markers. Business logic, simulation algorithms, persistence models, and UI behavior are intentionally not yet implemented.
