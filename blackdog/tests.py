from django.urls import reverse


def test_root_view(client):
    url = reverse('/')
    response = client.get(url)
    assert response.status_code == 200
    assert '<title>Blackdog</title>' in response.content.lower()
