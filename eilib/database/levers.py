# Autogenerated file. Do not modify
from __future__ import annotations

from .abstract import EiDatabase, EiDatabaseCustomType, EiDatabaseTable, EiDatabaseTableRow


class PlaceType(EiDatabaseCustomType):

    __slots__ = (
        "p1_x",
        "p1_y",
        "p2_x",
        "p2_y",
    )

    def __init__(self):
        self.p1_x: float | None = None
        self.p1_y: float | None = None
        self.p2_x: float | None = None
        self.p2_y: float | None = None
        super().__init__()


class LeverPrototype(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "places",
        "placesnum",
        "scale",
        "switch_time",
        "material",
        "switch_sound",
        "lever_text",
    )

    def __init__(self):
        self.name: str | None = None
        self.places: PlaceType | None = None
        self.placesnum: int | None = None
        self.scale: float | None = None
        self.switch_time: int | None = None
        self.material: str | None = None
        self.switch_sound: str | None = None
        self.lever_text: str | None = None
        super().__init__()

    @property
    def _db_type(self):
        return LeversDatabase


class LeverPrototypes(EiDatabaseTable[LeverPrototype]):

    _row_type = LeverPrototype


class LeversDatabase(EiDatabase):

    __slots__ = (
        "lever_prototypes",
    )
    _custom_types = {t.__name__: t for t in (PlaceType,)}

    def __init__(self):
        self.lever_prototypes = LeverPrototypes()
        super().__init__()
