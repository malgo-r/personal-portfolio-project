import pytest
import datetime


@pytest.mark.django_db
def test_string_representation(blog):
    assert str(blog) == "Sample blog title"


def test_blog_fields(blog):
    assert blog.title == "Sample blog title"
    assert blog.date == datetime.datetime.now()
    assert blog.text == "Sample blog text"

