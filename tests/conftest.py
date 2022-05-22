from pytest_factoryboy import register

from tests.factory import UserFactory, BoardFactory, ParticipantFactory

# fixtures
pytest_plugins = "tests.fixtures"

# factories
register(UserFactory)
register(BoardFactory)
register(ParticipantFactory)
