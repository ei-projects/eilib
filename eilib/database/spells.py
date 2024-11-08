# Autogenerated file. Do not modify
from __future__ import annotations

from .abstract import EiDatabase, EiDatabaseCustomType, EiDatabaseTable, EiDatabaseTableRow


class SpellMods(EiDatabaseCustomType):

    __slots__ = (
        "range",
        "targets",
        "area",
        "effect",
        "duration",
    )

    def __init__(self):
        self.range: int | None = None
        self.targets: int | None = None
        self.area: int | None = None
        self.effect: int | None = None
        self.duration: int | None = None
        super().__init__()


class SpellPrototype(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "code",
        "subtype",
        "price",
        "type",
        "mana",
        "slots",
        "speed",
        "range",
        "area",
        "effect",
        "target",
        "targets",
        "duration",
        "actions",
        "require_trace",
        "builtin_mods",
        "special_mods",
        "texture_type_index",
        "subtypecode",
        "available_mods",
        "complex",
        "shops",
        "light_red",
        "light_green",
        "light_blue",
        "light_raduis",
        "fadeout_time",
    )

    def __init__(self):
        self.name: str | None = None
        self.code: str | None = None
        self.subtype: str | None = None
        self.price: float | None = None
        self.type: int | None = None
        self.mana: float | None = None
        self.slots: int | None = None
        self.speed: float | None = None
        self.range: float | None = None
        self.area: float | None = None
        self.effect: float | None = None
        self.target: int | None = None
        self.targets: int | None = None
        self.duration: int | None = None
        self.actions: int | None = None
        self.require_trace: int | None = None
        self.builtin_mods: list[int] | None = None
        self.special_mods: list[int] | None = None
        self.texture_type_index: int | None = None
        self.subtypecode: int | None = None
        self.available_mods: SpellMods | None = None
        self.complex: int | None = None
        self.shops: int | None = None
        self.light_red: float | None = None
        self.light_green: float | None = None
        self.light_blue: float | None = None
        self.light_raduis: float | None = None
        self.fadeout_time: float | None = None
        super().__init__()

    @property
    def _db_type(self):
        return SpellsDatabase


class SpellModifier(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "code",
        "price",
        "type",
        "mana",
        "value",
        "complex",
        "allod",
        "shops",
    )

    def __init__(self):
        self.name: str | None = None
        self.code: int | None = None
        self.price: float | None = None
        self.type: int | None = None
        self.mana: float | None = None
        self.value: float | None = None
        self.complex: int | None = None
        self.allod: str | None = None
        self.shops: int | None = None
        super().__init__()

    @property
    def _db_type(self):
        return SpellsDatabase


class SpellTemplate(EiDatabaseTableRow):

    __slots__ = (
        "prototype",
        "required",
        "optional",
        "power",
        "shops",
    )

    def __init__(self):
        self.prototype: str | None = None
        self.required: list[str] | None = None
        self.optional: list[str] | None = None
        self.power: str | None = None
        self.shops: int | None = None
        super().__init__()

    @property
    def _db_type(self):
        return SpellsDatabase


class ArmorSpellTemplate(EiDatabaseTableRow):

    __slots__ = (
        "prototype",
        "required",
        "optional",
        "power",
        "shops",
    )

    def __init__(self):
        self.prototype: str | None = None
        self.required: list[str] | None = None
        self.optional: list[str] | None = None
        self.power: str | None = None
        self.shops: int | None = None
        super().__init__()

    @property
    def _db_type(self):
        return SpellsDatabase


class WeaponSpellTemplate(EiDatabaseTableRow):

    __slots__ = (
        "prototype",
        "required",
        "optional",
        "power",
        "shops",
    )

    def __init__(self):
        self.prototype: str | None = None
        self.required: list[str] | None = None
        self.optional: list[str] | None = None
        self.power: str | None = None
        self.shops: int | None = None
        super().__init__()

    @property
    def _db_type(self):
        return SpellsDatabase


class SpellPrototypes(EiDatabaseTable[SpellPrototype]):

    _row_type = SpellPrototype


class SpellModifiers(EiDatabaseTable[SpellModifier]):

    _row_type = SpellModifier


class SpellTemplates(EiDatabaseTable[SpellTemplate]):

    _row_type = SpellTemplate


class ArmorSpellTemplates(EiDatabaseTable[ArmorSpellTemplate]):

    _row_type = ArmorSpellTemplate


class WeaponSpellTemplates(EiDatabaseTable[WeaponSpellTemplate]):

    _row_type = WeaponSpellTemplate


class SpellsDatabase(EiDatabase):

    __slots__ = (
        "spell_prototypes",
        "spell_modifiers",
        "spell_templates",
        "armor_spell_templates",
        "weapon_spell_templates",
    )
    _custom_types = {t.__name__: t for t in (SpellMods,)}

    def __init__(self):
        self.spell_prototypes = SpellPrototypes()
        self.spell_modifiers = SpellModifiers()
        self.spell_templates = SpellTemplates()
        self.armor_spell_templates = ArmorSpellTemplates()
        self.weapon_spell_templates = WeaponSpellTemplates()
        super().__init__()
