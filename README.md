# [christinanissi.com](https://christinanissi.com)

Art / Writing portfolio website for Christina Nissi made in
[Django](https://www.djangoproject.com/) with [Bootstrap](https://getbootstrap.com/).
Deployed in production with [Docker](https://www.docker.com/),
[Gunicorn](https://gunicorn.org/), [PostgreSQL](https://www.postgresql.org/) and
[NGINX](https://www.nginx.com/). Project dependencies managed with
[Poetry](https://python-poetry.org/).

## Features

- Create art or writing content posts
- Homepage with masonry grid of latest content
- Contact page with contact form
- About page
- Responsive design for mobile devices
- RSS feed of all contents
- Search Engine Optimized (SEO) with sitemap, image compression etc.
- CI/CD with [pre-commit](https://pre-commit.com/) checks.
- Gunigorn WSGI server running inside a docker container and served behind an NGINX
  reverse proxy
- Dependencies managed with Poetry

## Installation

Requirements are automatically installed by building the docker image. Docker engine and
docker compose required. In order to install dependencies and run the server outside of
docker container the requirements can be installed using `poetry install` inside the
`src/` directory.

To deploy in production a running NGINX service is required on the host server.

### Development

1. Clone the repository and navigate inside the project root.
2. Copy `.example.env.dev` to `.env.dev` and `.example.env.dev.db` to `.env.dev.db`.
   Update the desired environment variables.
3. Build the images and run the containers:

```sh
docker compose up -d --build
```

Navigate to [http://localhost:8000](http://localhost:8000). The `src` directory is
mounted into the container and code changes will apply automatically.

### Production

1. Clone the repository and navigate inside the project root.
2. Copy `.example.env.prod` to `.env.prod` and `.example.env.prod.db` to `.env.prod.db`.
   Update the desired environment variables.
3. Build the images and run the containers:

```sh
docker compose -f docker-compose.prod.yml up -d --build
```

4. Setup NGINX reverse proxy by adding a new configuration file to
   `/etc/nginx/sites-available/`. Example configuration (replace variables inside _<>_):

```
server {
    listen 80;
    listen [::]:80;

    server_name <host_name>;

    location / {
        proxy_pass http://localhost:8005;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    location /static/ {
        alias <path_to_project_dir>/src/staticfiles;
    }

    location /media/ {
        alias <path_to_project_dir>/src/mediafiles;
    }
}
```

5. Install [Certbot](https://certbot.eff.org/). Then create HTTPS certificates:

```sh
certbot --nginx
```

## Live Website

View the project live at [https://christinanissi.com](https://christinanissi.com).
