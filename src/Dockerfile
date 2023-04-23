# Pull python image
FROM python:3.10-alpine

# Set work directory
WORKDIR /usr/src/app

# Set python env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install pip package dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev g++ cargo

# Install dependencies with poetry
RUN pip install -U --pre pip poetry
ADD poetry.lock .
ADD pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root

# Copy and set entrypoint as executable
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy project
COPY . .

# Run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
