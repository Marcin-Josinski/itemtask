FROM python:3.8.5-slim-buster

ENV POETRY_VERSION=1.0.9 POETRY_VIRTUALENVS_CREATE=false

# This dir will become the mountpoint of development code:
WORKDIR /code

# System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  # Installing poetry dependency manager
  && pip install "poetry==$POETRY_VERSION" && poetry --version

# Copy only requirements, to cache them in docker layer
COPY ./poetry.lock ./pyproject.toml ./

# Install Python deps
RUN poetry install  --no-interaction --no-ansi
