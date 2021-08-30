import pytest

from ..api.serializers import VisitedLinksSerializer


@pytest.mark.parametrize('links, domains', [
    (
        ('https://google.com/doodles', 'https://www.coursera.org/'),
        ('google.com', 'coursera.org'),
    ),
    (
        ('https://docs.pytest.org/en/6.2.x/', 'https://vk.com/feed'),
        ('pytest.org', 'vk.com'),
    )
])
def test_serializer_create_return_domains(links, domains):
    """Test serializers create() saves domains of provided urls."""
    serializer = VisitedLinksSerializer(data={'links': links})
    serializer.is_valid()
    data = serializer.save()
    assert domains == data['links']
