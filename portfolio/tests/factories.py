import factory

from portfolio.models import Project


class ProjectFactory(factory.Factory):
    class Meta:
        model = Project

    title = "Sample project title"
    description = "Sample description"
