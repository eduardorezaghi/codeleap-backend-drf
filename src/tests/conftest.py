import pytest
from rest_framework.test import APIClient

from api.models import Post


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def post():
    return Post.objects.create(title="Test Post", content="Test Content")
