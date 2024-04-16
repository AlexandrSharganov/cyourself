# Cyourself(Pet-project)

## social platform

### A social platform where users can register, customize their profile, create and edit posts, leave comments, like posts, follow other users, bookmark favorite content to their storage, and browse a feed of new articles. The platform is designed as a resource where you can store materials and articles you like in your storage, allowing you to access them anytime. Users themselves create the articles and materials.
---
### Technical stack

- celery
- Django
- Docker
- gunicorn
- nginx
- postgresql
- redis
---
### If you want to deploy

- After you clone repo to your machine, first of all you need is <.env> file in root catalog with next content:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY="django-insecure-6z^$^=vwy0+87!d0d2eosg5n@-nhl+09&tt*e+szgo7yy&%c6t"
REDIS_URL="redis://redis:6379/"
```

- To set up the project with Docker, all you need to do is execute the command:
```
docker compose up -d --build
```

_**Don't forget, you need to install Docker for this kind of magic.**_

During project build, meaningless fixtures will be automatically generated. These include several users, a few posts, and comments on them. Additionally, an admin will be automatically created. To access the admin panel, use:  

login: admin@admin.admin  
password: admin

- To shut down this one you need to execute the command:

```
docker compose down
```
---

## Developer
- Alexandr Sharganov
