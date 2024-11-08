# Autogenerated file. Do not modify
from __future__ import annotations

from .abstract import EiDatabase, EiDatabaseCustomType, EiDatabaseTable, EiDatabaseTableRow


class PrintsParams(EiDatabaseCustomType):

    __slots__ = (
        "opacity",
        "lifetime",
        "fadeout",
    )

    def __init__(self):
        self.opacity: float | None = None
        self.lifetime: int | None = None
        self.fadeout: int | None = None
        super().__init__()


class BloodPrint(EiDatabaseTableRow):

    __slots__ = (
        "terrain_type",
        "clear_weather",
        "weather_precipitation",
    )

    def __init__(self):
        self.terrain_type: str | None = None
        self.clear_weather: PrintsParams | None = None
        self.weather_precipitation: PrintsParams | None = None
        super().__init__()

    @property
    def _db_type(self):
        return PrintsDatabase


class FootPrint(EiDatabaseTableRow):

    __slots__ = (
        "terrain_type",
        "clear_weather",
        "weather_precipitation",
        "bloody",
    )

    def __init__(self):
        self.terrain_type: str | None = None
        self.clear_weather: PrintsParams | None = None
        self.weather_precipitation: PrintsParams | None = None
        self.bloody: PrintsParams | None = None
        super().__init__()

    @property
    def _db_type(self):
        return PrintsDatabase


class FirePrint(EiDatabaseTableRow):

    __slots__ = (
        "terrain_type",
        "clear_weather",
        "weather_precipitation",
    )

    def __init__(self):
        self.terrain_type: str | None = None
        self.clear_weather: PrintsParams | None = None
        self.weather_precipitation: PrintsParams | None = None
        super().__init__()

    @property
    def _db_type(self):
        return PrintsDatabase


class BloodPrints(EiDatabaseTable[BloodPrint]):

    _row_type = BloodPrint


class FootPrints(EiDatabaseTable[FootPrint]):

    _row_type = FootPrint


class FirePrints(EiDatabaseTable[FirePrint]):

    _row_type = FirePrint


class PrintsDatabase(EiDatabase):

    __slots__ = (
        "blood_prints",
        "foot_prints",
        "fire_prints",
    )
    _custom_types = {t.__name__: t for t in (PrintsParams,)}

    def __init__(self):
        self.blood_prints = BloodPrints()
        self.foot_prints = FootPrints()
        self.fire_prints = FirePrints()
        super().__init__()
