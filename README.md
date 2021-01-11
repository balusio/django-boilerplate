# choozieCRM
choozie starting point

# ENVIRONMENTS:

build docker:
```- docker-compose --env-file .env up```

secret_key: 
```python3 -c "import secrets; print(secrets.token_urlsafe())"```

in order to save or apply db changes and migrations or demo data create a file called
```dbvolumes```

it will be assigned to the DB container
