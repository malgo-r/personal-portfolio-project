import pytest

from portfolio.models import Project


@pytest.mark.django_db
def test_string_representation() -> None:
    test_project = Project.objects.create(title="My test project", description="sdf")
    assert str(test_project) == "My test project"
    assert test_project.title == "My test project"
