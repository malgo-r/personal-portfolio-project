import pytest


@pytest.mark.django_db
def test_string_representation(project) -> None:
    assert str(project) == "Sample project title"


@pytest.mark.django_db
def test_project_creation(project) -> None:
    assert project.title == "Sample project title"
    assert project.description == "Sample description"
