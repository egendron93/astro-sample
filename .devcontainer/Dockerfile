FROM python:3.12.3-bullseye

ENV PATH="${PATH}:/root/.local/bin"

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    python3-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --user pipx && \
    python3 -m pipx ensurepath && \
    pipx --global ensurepath && \
    pipx install poetry==1.2.0
