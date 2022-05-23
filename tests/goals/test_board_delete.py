import pytest
from freezegun import freeze_time

from goals.models import BoardParticipant, Board
from goals.serializers import BoardParticipantSerializer


@pytest.mark.django_db
def test_board_delete(client, logged_in_user, board_participant_1):

    response = client.delete(
        f"/goals/board/{board_participant_1.board.id}"
    )

    assert response.status_code == 204
    assert Board.objects.get(pk=board_participant_1.board.id).is_deleted
