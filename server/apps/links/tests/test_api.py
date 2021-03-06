import random
import uuid

import pytest
from django.core.cache import cache
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture(scope='module')
def api_client():
    """Module-level fixture for APIClient."""
    return APIClient()


@pytest.fixture(scope='module')
def domain():
    """Module-level fixture for saved to cache domains."""
    primary_key = cache.incr('domains-id')
    pattern = f'domain:{primary_key}:'
    name = f'{uuid.uuid4()}.com'
    timestamp = random.randint(1, 10000000)
    data = {
        f'{pattern}name': name,
        f'{pattern}visited_at': timestamp
    }
    cache.set_many(data)
    return {'name': name, 'timestamp': timestamp}


@pytest.mark.parametrize('data', [
    {'links': ['https://google.com/doodles', 'https://vk.com/']},
    {'links': ['https://www.nytimes.com/section/world']},
    {'links': ['https://github.com/django/channels', 'https://twitter.com/']},
])
def test_visited_links_creation(api_client, data):
    """Test POST request creates links."""
    url = reverse('api:visited-links-list')
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200
    assert response.data['status'] == 'ok'


def test_visited_domains_fetching(api_client, domain):
    """Test GET request returns created domains."""
    url = reverse('api:visited-domains-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert domain['name'] in response.data['domains']
    assert response.data['status'] == 'ok'


def test_visited_domains_filtering(api_client, domain):
    """Test visited domains Query param filtering with `from` and `to`."""
    timestamp = domain['timestamp']
    response = api_client.get(
        reverse('api:visited-domains-list'),
        {'from': timestamp - 1, 'to': timestamp + 1}
    )
    assert response.status_code == 200
    assert domain['name'] in response.data['domains']
