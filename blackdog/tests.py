from django.urls import reverse


def test_root_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    content = response.content.decode().lower()
    assert '<title>blackdog</title>' in content
    assert content.startswith('<html>')
    assert content.endswith('</html>')
