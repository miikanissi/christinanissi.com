# [christinanissi.com](https://christinanissi.com)

Art/Writing portfolio website for Christina Nissi made in
[Django](https://www.djangoproject.com/) with [Bootstrap](https://getbootstrap.com/).
Deployed with [Poetry](https://python-poetry.org/) and
[Docker](https://www.docker.com/).

## Features

- Create art or writing content posts
- Homepage with masonry grid of latest content
- Contact page with contact form
- About page
- Responsive design for mobile devices
- RSS feed of all contents
- Search Engine Optimized (SEO) with sitemap, image compression etc.
- CI/CD with [pre-commit](https://pre-commit.com/).

## Installation

### Requirements

- Latest release of [Django](https://www.djangoproject.com/).
- Docker engine (tested on version 20.10) and Docker compose (tested on version 2.10)
- Latest release of [Poetry](https://python-poetry.org/docs/).

### Development

```
git clone https://github.com/miikanissi/christinanissi.com.git
cd christinanissi.com
cp .example.env .env
poetry init
docker compose up -d
```

## Demo

View live at [https://christinanissi.com](https://christinanissi.com).
