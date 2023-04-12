import pytest

from tests.utils import (
    SingleHtmlFileExtension,
    configure_django,
)


def pytest_sessionstart(session):
    configure_django()


@pytest.fixture()
def snapshot_html(snapshot):
    return snapshot.use_extension(SingleHtmlFileExtension)
