#Introduction
Python count app with redis cache backend

# Run the application

```
docker-compose up --build


Go to http://localhost/

# Test
Run the tests inside the container
```
docker exec -it hello-api-test pytest --ignore=tests/ --cov=app tests/
```


