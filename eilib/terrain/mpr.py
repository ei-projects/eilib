import enum
import math
import os
import struct

from eilib.common.types import Point3D, Vector3D
from eilib.res.resfile import ResFile

MP_FILE_SIGNATURE = 0xCE4AF672
MP_HEADER_FORMAT = '<LfLLLLLLHL'
MP_HEADER_SIZE = struct.calcsize(MP_HEADER_FORMAT)
MP_MATERIAL_FORMAT = '<Lffffffffff'
MP_MATERIAL_SIZE = struct.calcsize(MP_MATERIAL_FORMAT)
MP_ANIMATED_TILE_FORMAT = '<HH'
MP_ANIMATED_TILE_SIZE = struct.calcsize(MP_ANIMATED_TILE_FORMAT)

SEC_FILE_SIGNATURE = 0xCF4BF774
SEC_HEADER_FORMAT = '<LB'
SEC_HEADER_SIZE = struct.calcsize(SEC_HEADER_FORMAT)
SEC_VERTEX_FORMAT = '<bbHL'
SEC_VERTEX_SIZE = struct.calcsize(SEC_VERTEX_FORMAT)
SEC_VERTICES_SIDE_LEN = 33
SEC_VERTICES_SIDE_LAST = SEC_VERTICES_SIDE_LEN - 1
SEC_TILES_SIDE_LEN = 16


class InvalidMprFile(Exception):
    pass


class MpMaterialType(enum.IntEnum):
    UNDEFINED = 0
    TERRAIN = 1
    LIQUID_WITHOUT_TEXTURE = 2
    LIQUID = 3
    GRASS = 4


class MpMaterial:

    def __init__(self):
        self.type = MpMaterialType.UNDEFINED
        self.rgba = [0, 0, 0, 0]
        self.self_illum = 0
        self.wave_multiplier = 0
        self.warp_speed = 0
        self.reserved1 = 0
        self.reserved2 = 0
        self.reserved3 = 0

    def read(self, file):
        data = file.read(MP_MATERIAL_SIZE)
        (
            self.type,
            *self.rgba,
            self.self_illum,
            self.wave_multiplier,
            self.warp_speed,
            self.reserved1,
            self.reserved2,
            self.reserved3,
        ) = struct.unpack(MP_MATERIAL_FORMAT, data)
        self.type = MpMaterialType(self.type)

    def write(self, file):
        data = struct.pack(
            MP_MATERIAL_FORMAT,
            self.type,
            *self.rgba,
            self.self_illum,
            self.wave_multiplier,
            self.warp_speed,
            self.reserved1,
            self.reserved2,
            self.reserved3,
        )
        file.write(data)


class MpTileType(enum.IntEnum):
    GRASS = 0
    GROUND = 1
    STONE = 2
    SAND = 3
    ROCK = 4
    FIELD = 5
    LIQUID = 6
    ROAD = 7
    UNDEFINED = 8
    SNOW = 9
    ICE = 10
    DRYGRASS = 11
    SNOWBALLS = 12
    LAVA = 13
    SWAMP = 14
    HIGHROCK = 15
    LAST = 16


class MpAnimTile:

    def __init__(self):
        self.tile_index = 0
        self.phases_count = 0

    def read(self, file):
        data = file.read(MP_ANIMATED_TILE_SIZE)
        (
            self.tile_index,
            self.phases_count,
        ) = struct.unpack(MP_ANIMATED_TILE_FORMAT, data)

    def write(self, file):
        data = struct.pack(
            MP_ANIMATED_TILE_FORMAT,
            self.tile_index,
            self.phases_count,
        )
        file.write(data)


class MpFile:

    def __init__(self):
        self.max_z = 10
        self.sectors_x_count = 0
        self.sectors_y_count = 0
        self.textures_count = 0
        self.texture_size = 512
        self.tile_size = 64
        self.materials = []
        self.tiles = []
        self.anim_tiles = []

    def read(self, file):
        data = file.read(MP_HEADER_SIZE)
        (
            signature,
            self.max_z,
            self.sectors_x_count,
            self.sectors_y_count,
            self.textures_count,
            self.texture_size,
            tiles_count,
            self.tile_size,
            materials_count,
            anim_tiles_count,
        ) = struct.unpack(MP_HEADER_FORMAT, data)

        if signature != MP_FILE_SIGNATURE:
            raise InvalidMprFile('mp file signature is invalid')

        self.materials = [MpMaterial() for _ in range(materials_count)]
        for material in self.materials:
            material.read(file)

        self.tiles = [MpTileType(*struct.unpack('<L', file.read(4))) for _ in range(tiles_count)]

        self.anim_tiles = [MpAnimTile() for _ in range(anim_tiles_count)]
        for anim_tile in self.anim_tiles:
            anim_tile.read(file)

    def write(self, file):
        data = struct.pack(
            MP_HEADER_FORMAT,
            MP_FILE_SIGNATURE,
            self.max_z,
            self.sectors_x_count,
            self.sectors_y_count,
            self.textures_count,
            self.texture_size,
            len(self.tiles),
            self.tile_size,
            len(self.materials),
            len(self.anim_tiles),
        )
        file.write(data)

        for material in self.materials:
            material.write(file)

        for tile in self.tiles:
            file.write(struct.pack('<L', tile))

        for anim_tile in self.anim_tiles:
            anim_tile.write(file)


class SecVertex:

    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0
        self.z = 0
        self.normal = Vector3D()

    def read(self, file):
        data = file.read(SEC_VERTEX_SIZE)
        (
            self.offset_x,
            self.offset_y,
            self.z,
            packed_normal,
        ) = struct.unpack(SEC_VERTEX_FORMAT, data)
        self.normal = self.unpack_normal(packed_normal)

    def write(self, file):
        data = struct.pack(
            SEC_VERTEX_FORMAT,
            self.offset_x,
            self.offset_y,
            self.z,
            self.pack_normal(self.normal),
        )
        file.write(data)

    def pack_normal(self, normal):
        assert normal.x >= -1.0 and normal.x <= 1.0
        assert normal.y >= -1.0 and normal.y <= 1.0
        assert normal.z >= 0.0 and normal.z <= 1.0
        return (
            (int(math.floor(normal.z * 1000.0)) << 22)
            | (int(math.floor(normal.x * 1000.0 + 1000.0)) << 11)
            | (int(math.floor(normal.y * 1000.0 + 1000.0)))
        )

    def unpack_normal(self, packed_norm):
        z = float(packed_norm >> 22) / 1000.0
        x = float(((packed_norm >> 11) & 0x7FF) - 1000.0 ) / 1000.0
        y = float((packed_norm & 0x7FF) - 1000.0) / 1000.0
        return Vector3D(x, y, z)


class SecFile:

    def __init__(self):
        self.land_vertices = [[SecVertex() for _ in range(SEC_VERTICES_SIDE_LEN)]
                              for _ in range(SEC_VERTICES_SIDE_LEN)]
        self.land_tiles = [[0 for _ in range(SEC_TILES_SIDE_LEN)]
                           for _ in range(SEC_TILES_SIDE_LEN)]
        self.liquid_vertices = None
        self.liquid_tiles = None
        self.liquid_tile_materials = None

    def read(self, file):
        data = file.read(SEC_HEADER_SIZE)
        (
            signature,
            has_liquid,
        ) = struct.unpack(SEC_HEADER_FORMAT, data)
        if signature != SEC_FILE_SIGNATURE:
            raise InvalidMprFile('sec file signature is invalid')

        for row in self.land_vertices:
            for vertex in row:
                vertex.read(file)

        if has_liquid:
            self.liquid_vertices = [[SecVertex() for _ in range(SEC_VERTICES_SIDE_LEN)]
                                    for _ in range(SEC_VERTICES_SIDE_LEN)]
            self.liquid_tiles = [[0 for _ in range(SEC_TILES_SIDE_LEN)]
                                 for _ in range(SEC_TILES_SIDE_LEN)]
            self.liquid_tile_materials = [[0 for _ in range(SEC_TILES_SIDE_LEN)]
                                          for _ in range(SEC_TILES_SIDE_LEN)]
            for row in self.liquid_vertices:
                for vertex in row:
                    vertex.read(file)
        else:
            self.liquid_vertices = None
            self.liquid_tiles = None
            self.liquid_tile_materials = None

        self.land_tiles = [
            [tile[0] for tile in struct.iter_unpack('<H', file.read(2 * SEC_TILES_SIDE_LEN))]
            for _ in range(SEC_TILES_SIDE_LEN)
        ]

        if has_liquid:
            self.liquid_tiles = [
                [tile[0] for tile in struct.iter_unpack('<H', file.read(2 * SEC_TILES_SIDE_LEN))]
                for _ in range(SEC_TILES_SIDE_LEN)
            ]
            self.liquid_tile_materials = [
                [tile[0] for tile in struct.iter_unpack('<H', file.read(2 * SEC_TILES_SIDE_LEN))]
                for _ in range(SEC_TILES_SIDE_LEN)
            ]

    def write(self, file):
        data = struct.pack(
            SEC_HEADER_FORMAT,
            SEC_FILE_SIGNATURE,
            3 if self.liquid_vertices else 0,
        )
        file.write(data)

        for row in self.land_vertices:
            for vertex in row:
                vertex.write(file)

        if self.liquid_vertices:
            for row in self.liquid_vertices:
                for vertex in row:
                    vertex.write(file)

        for row in self.land_tiles:
            for tile in row:
                file.write(struct.pack('<H', tile))

        if self.liquid_vertices:
            for row in self.liquid_tiles:
                for tile in row:
                    file.write(struct.pack('<H', tile))
            for row in self.liquid_tile_materials:
                for tile in row:
                    file.write(struct.pack('<H', tile))


class MprFile:

    def __init__(self):
        self.mp = None
        self.sectors = None

    def read(self, path):
        mp = None
        with ResFile(path) as res:
            mp_name = ''
            for info in res.iter_files():
                if info.name.lower().endswith('.mp'):
                    with res.open(info.name) as file:
                        mp = MpFile()
                        mp.read(file)
                        mp_name = info.name
                        break
            else:
                raise InvalidMprFile(".mpr file doesn't have .mp file")

            sectors = [
                [SecFile() for _ in range(mp.sectors_x_count)]
                for _ in range(mp.sectors_y_count)
            ]
            sec_format = f'{os.path.splitext(mp_name)[0]}{{:03d}}{{:03d}}.sec'
            for y in range(mp.sectors_y_count):
                for x in range(mp.sectors_x_count):
                    with res.open(sec_format.format(x, y)) as file:
                        sectors[y][x].read(file)

            self.mp = mp
            self.sectors = sectors

    def get_vertex(self, x, y):
        if (
            x < 0 or x > self.mp.sectors_x_count * SEC_VERTICES_SIDE_LAST or
            y < 0 or y > self.mp.sectors_y_count * SEC_VERTICES_SIDE_LAST
        ):
            raise ValueError('invalid coordinates')

        sector_x, rel_x = divmod(x, SEC_VERTICES_SIDE_LAST)
        sector_y, rel_y = divmod(y, SEC_VERTICES_SIDE_LAST)
        if sector_x >= self.mp.sectors_x_count:
            sector_x, rel_x = self.mp.sectors_x_count - 1, SEC_VERTICES_SIDE_LAST
        if sector_y >= self.mp.sectors_y_count:
            sector_y, rel_y = self.mp.sectors_y_count - 1, SEC_VERTICES_SIDE_LAST

        vertex: SecVertex = self.sectors[sector_y][sector_x].land_vertices[rel_y][rel_x]
        return Point3D(
            x + vertex.offset_x / 254,
            y + vertex.offset_y / 254,
            vertex.z * self.mp.max_z / 65534
        )


def main():
    mpr = MprFile()
    mpr.read(r'D:\Soft\EI\Maps\zone3obr.mpr')
    with open('zone3obr.obj', 'w') as file:

        height = mpr.mp.sectors_y_count * SEC_VERTICES_SIDE_LAST + 1
        width = mpr.mp.sectors_x_count * SEC_VERTICES_SIDE_LAST + 1
        for y in range(height):
            for x in range(width):
                p = mpr.get_vertex(x, height - y - 1)
                file.write(f'v {p.x} {p.y} {p.z}\n')

        for y in range(height - 1):
            for x in range(width - 1):
                verts = [
                    x+1 + y*width,
                    x+2 + y*width,
                    x+2 + (y+1)*width,
                    x+1 + (y+1)*width,
                ]
                file.write(f'f {" ".join(str(v) for v in verts)}\n')

if __name__ == '__main__':
    main()
