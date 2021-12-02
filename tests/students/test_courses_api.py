from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

import pytest

from django.contrib.auth.models import User
from django.template.base import Token
from rest_framework.test import APIClient


from students.models import Student
from pprint import pprint


@pytest.mark.django_db
def test_first_courses(client, url, course_factory):

    course_factory(_quantity=1)
    url += '1/'

    response = client.get(url)

    assert response.status_code == HTTP_200_OK
    assert response.json()['name']


@pytest.mark.django_db
def test_courses_list(client, url, course_factory):
    col = 10
    course_factory(_quantity=col)
    response = client.get(url)

    assert response.status_code == HTTP_200_OK
    assert len(response.data) == col


@pytest.mark.django_db
def test_filter_id(client, url, course_factory):
    col = 5
    course = course_factory(_quantity=col)
    url += f'?id={course[0].id}'
    response = client.get(url)

    assert response.status_code == HTTP_200_OK
    assert response.json()[0]['id'] == course[0].id



@pytest.mark.django_db
def test_filter_name(client, url, course_factory):
    col = 5
    course = course_factory(_quantity=col)
    url += f'?name={course[0].name}'
    response = client.get(url)

    assert response.status_code == HTTP_200_OK
    assert response.json()[0]['name'] == course[0].name


@pytest.mark.parametrize(
    ['json_data', 'expected_code'],
    (
            ({
                 'name': 'Валентин',
                 'birth_date': '20-12-2000'
             }, HTTP_201_CREATED),
            ({
                 'name': 'Игорь'
            }, HTTP_201_CREATED),
            ({
                'birth_date': '20-12-2000'
            }, HTTP_400_BAD_REQUEST),
            ({
                'name': None
             }, HTTP_400_BAD_REQUEST),
            ({
                'id': 1,
                'name': 'Василий',
                'birth_date': '02-03-1994'
            }, HTTP_201_CREATED),
            ({}, HTTP_400_BAD_REQUEST),
            ({
                 'name': 'Валентин',
                 'birth_date': '20-12-2000'
             }, HTTP_201_CREATED),
            ({
                'name': 'Мария',
                'birth_date': '28.02.1985'
            }, HTTP_201_CREATED),
            ({
                'name': 'Константин',
                'birth_date': '40-40-3800'
            }, HTTP_201_CREATED),
            ({
                'name': 'Марк',
                'birth_date': '12-03-1960',
                'not_use': '123'
            }, HTTP_400_BAD_REQUEST)
    )
)
@pytest.mark.django_db
def test_create_course(client, url, json_data, expected_code):

    response = client.post(url, json_data)
    assert response.status_code == expected_code


@pytest.mark.parametrize(
    ['json_data', 'expected_code'],
    (
            ({
                 'name': 'Валентин',
                 'birth_date': '20-12-2000'
             }, HTTP_200_OK),
            ({
                 'name': 'Игорь'
            }, HTTP_200_OK),
            ({
                'birth_date': '20-12-2000'
            }, HTTP_200_OK),
            ({
                'name': None
             }, HTTP_400_BAD_REQUEST),
            ({
                'id': 1,
                'name': 'Василий',
                'birth_date': '02-03-1994'
            }, HTTP_400_BAD_REQUEST),
            ({}, HTTP_200_OK),
            ({
                 'name': 'Валентин',
                 'birth_date': '20-12-2000'
             }, HTTP_200_OK),
            ({
                'name': 'Константин',
                'birth_date': '40-40-3800'
            }, HTTP_200_OK),
            ({
                'name': 'Человек',
                'birth_date': '12-03-1960',
                'not_use': '123'
            }, HTTP_400_BAD_REQUEST),
            ({
                'not_use': '123'
            }, HTTP_400_BAD_REQUEST)
    )
)
@pytest.mark.django_db
def test_update_course(client, url, course_factory, json_data, expected_code):
    col = 5
    course = course_factory(_quantity=col)
    url += f'{course[2].id}/'
    response = client.patch(url, json_data)

    assert response.status_code == expected_code

@pytest.mark.django_db
def test_delete_course(client, url, course_factory):
    col = 10
    course = course_factory(_quantity=col)
    url += f'{course[3].id}/'

    response = client.delete(url)

    assert response.status_code == HTTP_204_NO_CONTENT

#
# @pytest.mark.django_db
# def test_student_list():
#     Student.objects.create(name='Иван', birth_date='10.12.1994')
#     Student.objects.bulk_create(
#         [
#             Student(name='Петр', birth_date='15.10.1990'),
#             Student(name='Мария', birth_date='20.03.1984'),
#             Student(name='Валентин', birth_date='03.08.1960'),
#         ]
#     )
#     client = APIClient()
#     url = 'http://localhost:8000/api/v1/courses'
#     expected_result = ''
#
#     response = client.get(url)
#
#     assert response.status_code == 201
#     assert len(response.data) == 4
#
# @pytest.mark.django_db
# def test_crate():
#     student_data = {'name': 'Петр', 'birth_date': '15.10.1990'}
#     client = APIClient()
#     url = url = 'http://localhost:8000/api/v1/courses'
#     response = client.post(url, student_data)
#     assert response.status_code == 401
#
# @pytest.mark.django_db
# def test_crate_user(client, url):
#     student_data = {'name': 'Петр', 'birth_date': '15.10.1990'}
#     user1 = User.objects.create_user('siml', password='12345678', is_active=True)
#     token = Token.objects.crate(user=user1)
#     client.credentials(HTTP_AUTHORIZATION=f'Token{token.key}')
#
#     response = client.post(url, student_data)
#
#     assert response.status_code == 403
