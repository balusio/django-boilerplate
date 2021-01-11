# Django-boilerplate

This is a DJango boilerplate to run a basic django rest API, built with :
Django, Django rest framework
Postgres
Nginx
Docker and Docker compose

# ENVIRONMENTS:

*Variables:*
- SECRET_KEY 
secret_key (create it and use it on your local)
```python3 -c "import secrets; print(secrets.token_urlsafe())"```

- DEBUG (will be used for django to debug)

- ALLOWED_HOSTS host allowed to use on your environment

you can check more about enviroment and how to prepare this app to deploy [here](https://www.youtube.com/watch?v=nh1ynJGJuT8)
# running local:
```- docker-compose --env-file .env up``` will use the local docker-compose.yml

in order to save or apply db changes and migrations or demo data create a file called
```dbvolumes```

it will be assigned to the DB (uses posgres for all environments)

# deploy:

Check [here](https://www.youtube.com/watch?v=IoxHUrbiqUo) a few possibilites to deploy your app , there's already a proxy with nginx and a docker-compose.yml defined as a boilerplate.
