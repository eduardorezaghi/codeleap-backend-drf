import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_get_all_posts(api_client, post):
    url = reverse("post-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    assert response.data["count"] == 1
    assert response.data["results"][0]["id"] == post.id
    assert response.data["results"][0]["title"] == post.title
    assert response.data["results"][0]["username"] == post.username
    assert response.data["results"][0]["content"] == post.content
    assert response.data["results"][0][
        "created_datetime"
    ] == post.created_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


@pytest.mark.django_db
def test_create_post(api_client):
    url = reverse("post-list")

    data = {"title": "Title", "username": "user1", "content": "Content"}
    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED

    assert response.data["title"] == data["title"]
    assert response.data["username"] == data["username"]
    assert response.data["content"] == data["content"]


@pytest.mark.django_db
def test_edit_post(api_client, post):
    url = reverse("post-detail", args=[post.id])

    data = {"title": "Updated Title", "content": "Updated Content"}
    response = api_client.patch(url, data, format="json")

    assert response.status_code == status.HTTP_200_OK

    post.refresh_from_db()
    assert post.title == data["title"]
    assert post.content == data["content"]


@pytest.mark.django_db
def test_delete_post(api_client, post):
    url = reverse("post-detail", args=[post.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT

    assert response.data is None


@pytest.mark.django_db
def test_put_method_not_allowed(api_client, post):
    url = reverse("post-detail", args=[post.id])

    data = {"title": "Updated Title", "content": "Updated Content"}
    response = api_client.put(url, data, format="json")

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response.data["detail"] == 'Method "PUT" not allowed.'
