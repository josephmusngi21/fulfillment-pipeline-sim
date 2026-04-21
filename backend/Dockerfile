# TODO: Optimize backend image layers and production settings.
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy[asyncio] asyncpg alembic pydantic-settings websockets

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
