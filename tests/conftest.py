from pytest_factoryboy import register

from tests.factory import UserFactory

# fixtures
pytest_plugins = "tests.fixtures"

# factories
register(UserFactory)
