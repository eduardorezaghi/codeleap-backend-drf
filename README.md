# CodeLeap Backend test using DRF

## Summary
This document provides instructions for setting up and using the CodeLeap backend with Django Rest Framework (DRF).

## API Specification
- [Original API spec](https://dev.codeleap.co.uk/careers/)

## Database Migrations
Generate migrations after database changes:
```bash
$ python manage.py makemigrations api
```

Apply migrations to the database:
```bash
$ python manage.py migrate
```

## Running Unit Tests
```bash
$ cd src; pytest
```

## API Endpoints

### Create a Post
```bash
curl -X POST http://localhost:8000/careers/ -d '{"username": "Testing user", "title": "Testing Title", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus nec nunc ultricies ultricies. Nullam nec purus nec nunc ultricies ultricies. Nullam nec purus nec nunc ultricies ultricies. Nullam nec purus nec nunc ultricies ultricies. Nullam nec purus nec nunc"}' -H "Content-Type: application/json" | jq
```

### Get All Posts
```bash
curl -X GET http://localhost:8000/careers/ | jq
```

### Update a Post
```bash
curl -X PATCH http://localhost:8000/careers/<id>/ -d '{"username": "Updated user.", "title": "Updated title.", "content": "Updated content."}' -H "Content-Type: application/json" | jq
```

### Delete a Post
```bash
curl -X DELETE http://localhost:8000/careers/48/ | jq
```

### Pagination
Next page:
```bash
curl -X GET http://localhost:8000/careers/?page=2 | jq
```

Next page, count 5:
```bash
curl -X GET http://localhost:8000/careers/?page=2&count=5 | jq
```