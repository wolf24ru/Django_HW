import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_first_courses(client, url, course_factory):
    course = course_factory(_quantity=2)
    url += f'{course[0].id}/'

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
                 'name': 'Управление персаналом',
                 'students': []
             }, HTTP_201_CREATED),
            ({
                 'name': 'Теория игр'
             }, HTTP_201_CREATED),
            ({
                 'students': []
             }, HTTP_400_BAD_REQUEST),
            ({
                 'name': ''
             }, HTTP_400_BAD_REQUEST),
            ({}, HTTP_400_BAD_REQUEST),
            ({
                 'name': 'Управление персаналом',
                 'students': [1]
             }, HTTP_400_BAD_REQUEST),
            ({
                 'name': 'курс',
                 'students': 'фыва'
             }, HTTP_400_BAD_REQUEST),
            ({
                 'name': 'Системный анализ',
                 'students': [],
                 'not_use': '123'
             }, HTTP_201_CREATED),
            ({
                 'name': 'Понимание понятного',
                 'students': 1},
             HTTP_400_BAD_REQUEST)
    )
)
@pytest.mark.django_db
def test_create_course(client, url, students_factory, json_data, expected_code):
    student = students_factory(_quantity=2)
    try:
        if type(json_data['students']) == list:
            json_data['students'].append(student[0].id)
    except:
        ...

    response = client.post(url, json_data)

    assert response.status_code == expected_code


@pytest.mark.parametrize(
    ['json_data', 'expected_code'],
    (
            ({
                 'name': 'Управление персаналом',
                 'students': []
             }, HTTP_200_OK),
            ({
                 'name': 'Полигональные граффы'
             }, HTTP_200_OK),
            ({
                 'students': []
             }, HTTP_200_OK),
            ({
                 'name': ''
             }, HTTP_400_BAD_REQUEST),
            ({}, HTTP_200_OK),
            ({
                 'name': 'Управление персаналом',
                 'students': []
             }, HTTP_200_OK),
            ({
                 'name': 'угентение персанала',
                 'students': True
             }, HTTP_400_BAD_REQUEST),
            ({
                 'name': 'Понимание понятного',
                 'students': [],
                 'not_use': '123'
             }, HTTP_200_OK),
            ({
                 'not_use': '123'
             }, HTTP_200_OK),
            ({
                 'name': 'Понимание понятного',
                 'students': 2},
             HTTP_400_BAD_REQUEST)
    )
)
@pytest.mark.django_db
def test_update_course(client, url, course_factory, students_factory, json_data, expected_code):
    col = 5
    student = students_factory(_quantity=2)
    try:
        if type(json_data['students']) == list:
            json_data['students'].append(student[0].id)
    except:
        ...
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
