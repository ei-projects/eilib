# Autogenerated file. Do not modify
from __future__ import annotations

from .abstract import EiDatabase, EiDatabaseCustomType, EiDatabaseTable, EiDatabaseTableRow


class HlParams(EiDatabaseCustomType):

    __slots__ = (
        "type",
        "unk",
        "weight",
        "vitality",
    )

    def __init__(self):
        self.type: str | None = None
        self.unk: int | None = None
        self.weight: float | None = None
        self.vitality: float | None = None
        super().__init__()


class LootParams(EiDatabaseCustomType):

    __slots__ = (
        "probability",
        "mask",
        "min",
        "max",
    )

    def __init__(self):
        self.probability: float | None = None
        self.mask: float | None = None
        self.min: float | None = None
        self.max: float | None = None
        super().__init__()


class HitLocation(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "other_general",
        "other_general2",
        "unk3",
        "unk4",
    )

    def __init__(self):
        self.name: str | None = None
        self.other_general: list[float] | None = None
        self.other_general2: list[float] | None = None
        self.unk3: int | None = None
        self.unk4: int | None = None
        super().__init__()

    @property
    def _db_type(self):
        return UnitsDatabase


class RaceModel(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "typeid",
        "regenerate_health",
        "regenerate_mana",
        "secondary_language",
        "secondary_locomotion",
        "secondary_vision_arc",
        "speed_crawl",
        "attack_distance",
        "ai_class_stay",
        "ai_class_lie",
        "attack_general",
        "hl_head",
        "hl_torso",
        "hl_right_arm",
        "hl_left_arm",
        "hl_right_leg",
        "hl_left_leg",
        "graphics_data_mask_name",
        "graphics_data_primary_textures",
        "graphics_data_secondary_textures",
        "graphics_data_model_shift",
        "sounds_data_sfx_path",
        "sounds_data_steps",
        "animation_speed_special",
        "sounds_probability_idle",
        "sounds_probability_attack",
        "defence_general",
        "graphics_data_blood_type",
        "graphics_data_cast_type",
        "graphics_data_footprint_type",
        "graphics_data_leg_segments",
        "graphics_data_skin_type",
        "graphics_data_first_step_right",
        "graphics_data_head_height",
        "unk47",
        "unk48",
        "unk49",
        "unk50",
    )

    def __init__(self):
        self.name: str | None = None
        self.typeid: int | None = None
        self.regenerate_health: float | None = None
        self.regenerate_mana: float | None = None
        self.secondary_language: int | None = None
        self.secondary_locomotion: int | None = None
        self.secondary_vision_arc: float | None = None
        self.speed_crawl: list[float] | None = None
        self.attack_distance: float | None = None
        self.ai_class_stay: int | None = None
        self.ai_class_lie: int | None = None
        self.attack_general: list[float] | None = None
        self.hl_head: HlParams | None = None
        self.hl_torso: HlParams | None = None
        self.hl_right_arm: HlParams | None = None
        self.hl_left_arm: HlParams | None = None
        self.hl_right_leg: HlParams | None = None
        self.hl_left_leg: HlParams | None = None
        self.graphics_data_mask_name: str | None = None
        self.graphics_data_primary_textures: list[str] | None = None
        self.graphics_data_secondary_textures: list[str] | None = None
        self.graphics_data_model_shift: float | None = None
        self.sounds_data_sfx_path: str | None = None
        self.sounds_data_steps: list[str] | None = None
        self.animation_speed_special: list[float] | None = None
        self.sounds_probability_idle: int | None = None
        self.sounds_probability_attack: int | None = None
        self.defence_general: list[float] | None = None
        self.graphics_data_blood_type: int | None = None
        self.graphics_data_cast_type: int | None = None
        self.graphics_data_footprint_type: int | None = None
        self.graphics_data_leg_segments: int | None = None
        self.graphics_data_skin_type: str | None = None
        self.graphics_data_first_step_right: int | None = None
        self.graphics_data_head_height: float | None = None
        self.unk47: int | None = None
        self.unk48: int | None = None
        self.unk49: int | None = None
        self.unk50: int | None = None
        super().__init__()

    @property
    def _db_type(self):
        return UnitsDatabase


class MonsterPrototype(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "base_race",
        "unk2",
        "graphics_data_skin_index",
        "graphics_data_hair",
        "graphics_data_complection_x",
        "graphics_data_complection_y",
        "graphics_data_complection_z",
        "unk8",
        "stats_health",
        "stats_mana",
        "stats_absorbtion",
        "tuning_actions",
        "tuning_move",
        "attack_range",
        "stats_to_hit",
        "stats_parry",
        "tuning_weapon_weight",
        "attack_weapon_type_id",
        "stats_danage_nub",
        "stats_damage_max",
        "skills_general",
        "skills_steal",
        "skills_tame",
        "skills_peripheral",
        "senses_tracking",
        "detections_tracking",
        "common_loot",
        "rare_loot",
        "items",
        "skills_astral",
        "spells",
        "equipment_wears",
        "equipment_weapon_1",
        "graphics_data_info_window_scale",
        "graphics_data_altitude",
        "tuning_to_hit_random",
        "graphics_data_dialog_camera_distance",
        "graphics_data_dialog_camera_height",
        "attack_real_weapon_type_id",
        "graphics_data_detonation",
        "base_level",
        "equipment_weapon_2",
        "stats_exp",
    )

    def __init__(self):
        self.name: str | None = None
        self.base_race: str | None = None
        self.unk2: int | None = None
        self.graphics_data_skin_index: int | None = None
        self.graphics_data_hair: int | None = None
        self.graphics_data_complection_x: float | None = None
        self.graphics_data_complection_y: float | None = None
        self.graphics_data_complection_z: float | None = None
        self.unk8: str | None = None
        self.stats_health: float | None = None
        self.stats_mana: float | None = None
        self.stats_absorbtion: float | None = None
        self.tuning_actions: float | None = None
        self.tuning_move: float | None = None
        self.attack_range: float | None = None
        self.stats_to_hit: float | None = None
        self.stats_parry: float | None = None
        self.tuning_weapon_weight: float | None = None
        self.attack_weapon_type_id: int | None = None
        self.stats_danage_nub: float | None = None
        self.stats_damage_max: float | None = None
        self.skills_general: float | None = None
        self.skills_steal: float | None = None
        self.skills_tame: float | None = None
        self.skills_peripheral: float | None = None
        self.senses_tracking: list[float] | None = None
        self.detections_tracking: list[float] | None = None
        self.common_loot: LootParams | None = None
        self.rare_loot: LootParams | None = None
        self.items: list[str] | None = None
        self.skills_astral: list[float] | None = None
        self.spells: list[str] | None = None
        self.equipment_wears: list[str] | None = None
        self.equipment_weapon_1: str | None = None
        self.graphics_data_info_window_scale: float | None = None
        self.graphics_data_altitude: float | None = None
        self.tuning_to_hit_random: float | None = None
        self.graphics_data_dialog_camera_distance: float | None = None
        self.graphics_data_dialog_camera_height: float | None = None
        self.attack_real_weapon_type_id: int | None = None
        self.graphics_data_detonation: float | None = None
        self.base_level: int | None = None
        self.equipment_weapon_2: str | None = None
        self.stats_exp: float | None = None
        super().__init__()

    @property
    def _db_type(self):
        return UnitsDatabase


class Npc(EiDatabaseTableRow):

    __slots__ = (
        "name",
        "unk1",
        "exp",
        "strength",
        "dexterity",
        "intelligence",
        "tame",
        "awareness",
        "perks",
        "weapons",
        "quest_items",
        "spells",
        "exp_to_distribute",
        "money",
        "using_voice",
    )

    def __init__(self):
        self.name: str | None = None
        self.unk1: int | None = None
        self.exp: float | None = None
        self.strength: float | None = None
        self.dexterity: float | None = None
        self.intelligence: float | None = None
        self.tame: list[int] | None = None
        self.awareness: list[int] | None = None
        self.perks: list[str] | None = None
        self.weapons: list[str] | None = None
        self.quest_items: list[str] | None = None
        self.spells: list[str] | None = None
        self.exp_to_distribute: float | None = None
        self.money: int | None = None
        self.using_voice: int | None = None
        super().__init__()

    @property
    def _db_type(self):
        return UnitsDatabase


class HitLocations(EiDatabaseTable[HitLocation]):

    _row_type = HitLocation


class RaceModels(EiDatabaseTable[RaceModel]):

    _row_type = RaceModel


class MonsterPrototypes(EiDatabaseTable[MonsterPrototype]):

    _row_type = MonsterPrototype


class Npcs(EiDatabaseTable[Npc]):

    _row_type = Npc


class UnitsDatabase(EiDatabase):

    __slots__ = (
        "hit_locations",
        "race_models",
        "monster_prototypes",
        "npcs",
    )
    _custom_types = {t.__name__: t for t in (HlParams, LootParams,)}

    def __init__(self):
        self.hit_locations = HitLocations()
        self.race_models = RaceModels()
        self.monster_prototypes = MonsterPrototypes()
        self.npcs = Npcs()
        super().__init__()
