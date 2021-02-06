from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_root_view(client):
    response = client.get('/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')
