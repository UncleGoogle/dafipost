from unittest.mock import patch
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
import pytest

from . import views


def test_root_view(client):
    url = reverse('blackdog:index')
    response = client.get(url)
    assertTemplateUsed(response, 'index.html')


def test_new_view(client, django_user_model):
    url = reverse('blackdog:new')
    response = client.get(url)
    assertTemplateUsed(response, 'new.html')


def test_new_commited(client, django_user_model):
    user = django_user_model.objects.create(username='someone', password='password')
    client.force_login(user)
    url = reverse('blackdog:new')
    response = client.post(url, data={'content': 'bark content'})
    assert response.status_code == 302


@pytest.mark.parametrize("content, form_passed", [
    pytest.param("simple bark", True, id='simple message'),
    pytest.param("13 characters" * 10, True, id='130 chars msg'),
    pytest.param("13 characters" * 13, False, id='169 chars msg'),
])
def test_new_created(client, django_user_model, content, form_passed):
    user = django_user_model.objects.create(username='someone', password='password')
    client.force_login(user)
    url = reverse('blackdog:new')
    response = client.post(url, data={
        "content": content
    })
    if form_passed:
        assert response.status_code == 302
    else:
        assert response.status_code == 200  # form reloaded
    # TODO test displaying errors