#!/usr/bin/env python3

from app.db import models

def test_get_courses(client, test_course, test_superuser, superuser_token_headers):
    response = client.get(
        f"api/v1/curso",
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_one_course(client, test_course, test_superuser, superuser_token_headers):
    response = client.get(
        f"api/v1/curso/{test_course.id}",
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert response.json()['id'] == test_course.id

def test_create_course(client, test_superuser, superuser_token_headers):
    new_course = {
        "owner_id": test_superuser.owner_id,
        "name": "Música 2",
        "id_sigaa": 284,
        "course_type":models.CourseType.masters,
        "institutional_repository_url": 'https://repositorio.ufrn.br/handle/123456789/12031'
    }
    response = client.post(
        f"api/v1/curso",
        json=new_course,
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert all(item in response.json().items() for item in new_course.items())

def test_edit_course(client, test_superuser, test_course, superuser_token_headers):
    new_course = {
        "owner_id": test_superuser.owner_id,
        "name": "Música 3",
        "id_sigaa": 285,
        "institutional_repository_url": 'https://repositorio.ufrn.br/handle/123456789/12031',
        "course_type":models.CourseType.masters
    }
    response = client.put(
        f"api/v1/curso/{test_course.id}",
        json=new_course,
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    new_course["id"] = test_course.id
    assert response.json() == new_course

def test_delete_course(client, test_superuser, test_course, superuser_token_headers, test_db):
    response = client.delete(
        f"api/v1/curso/{test_course.id}",
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Course).filter(models.Course.deleted == False)) == []
