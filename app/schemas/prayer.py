from pydantic import BaseModel


class PrayerBase(BaseModel):
    title: str
    text: str
    category: str | None = None


class PrayerCreate(PrayerBase):
    pass


class PrayerResponse(PrayerBase):
    id: int
