#Introduction
Python count app with redis cache backend

# Run the application

```
docker-compose up --build


Go to http://localhost/

# Test
Run the container sh
```
docker exec -it hello-api-test sh
```

```
pytest --cov=app tests/
```

