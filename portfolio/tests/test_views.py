import pytest

from portfolio.views import home
from django.test import RequestFactory


@pytest.mark.django_db
def test_go_to_home__should_pass():
    rf = RequestFactory()
    request = rf.get('')
    response = home(request)
    assert response.status_code == 200
