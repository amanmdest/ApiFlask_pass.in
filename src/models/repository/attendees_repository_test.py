import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "meu-uuid-e-ficha"
    attendees_info = {
        "uuid": "meu-uuid-attendee2",
        "name": "attendee-name2",
        "email": "email2@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="Infos do badge")
def test_get_attendee_badge_by_id():
    attendee_id = "meu-uuid-attendee3"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)

    print(attendee)
    print(attendee.title)