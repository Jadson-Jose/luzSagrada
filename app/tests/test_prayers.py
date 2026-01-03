from app.models.prayer import Prayer
from app.schemas.prayer import PrayerCreate


def test_create_prayer_object():
    # Dados de exmplo para uma oração
    prayer_data = {
        "title": "Ave Maria",
        "text": "Ave Maria, cheia de graça",
        "category": "Maria",
    }

    prayer_schema = PrayerCreate(**prayer_data)

    prayer_model = Prayer(**prayer_schema.model_dump())

    assert prayer_model.title == "Ave Maria"
    assert prayer_model.category == "Maria"
    assert prayer_model.id is None
