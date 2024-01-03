FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml /app/

RUN poetry install --no-cache

COPY . .
ENV PYTHONPATH=/app.

CMD ["python", "-m", "main"]
