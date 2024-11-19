FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apk update && \
  pip install --upgrade pip

WORKDIR /cook_inventory_app

# Copy the project into the image
COPY /src /cook_inventory_app/
COPY pyproject.toml uv.lock /cook_inventory_app/

# Sync the project
RUN uv sync --no-dev
RUN uv add gunicorn

EXPOSE 5000

CMD uv run gunicorn -b 0.0.0.0:5000 main:app