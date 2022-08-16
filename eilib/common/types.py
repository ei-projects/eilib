import math
from dataclasses import dataclass

@dataclass(frozen=True)
class Point2D:
    x: float = 0.0
    y: float = 0.0

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return str(self)

    def __eq__(self, point2):
        return (
            math.isclose(self.x, point2.x) and
            math.isclose(self.y, point2.y)
        )


@dataclass(frozen=True)
class Point3D:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self):
        return str(self)

    def __eq__(self, point2):
        return (
            math.isclose(self.x, point2.x) and
            math.isclose(self.y, point2.y) and
            math.isclose(self.z, point2.z)
        )


@dataclass(frozen=True)
class Vector3D:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self):
        return str(self)

    def __eq__(self, vector2):
        return (
            math.isclose(self.x, vector2.x) and
            math.isclose(self.y, vector2.y) and
            math.isclose(self.z, vector2.z)
        )

    def __add__(self, vector2):
        return Vector3D(self.x + vector2.x, self.y + vector2.y, self.z + vector2.z)

    def __sub__(self, vector2):
        return Vector3D(self.x - vector2.x, self.y - vector2.y, self.z - vector2.z)

    def __mul__(self, num):
        return Vector3D(self.x * num, self.y * num, self.z * num)

    def __div__(self, num):
        return Vector3D(self.x / num, self.y / num, self.z / num)

    @property
    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2

    @property
    def length(self):
        return math.sqrt(self.length_squared)

    @property
    def normalized(self):
        length = self.length
        return Vector3D(self.x / length, self.y / length, self.z / length)

    def distance_to(self, vector2):
        return math.sqrt((self.x - vector2.x)**2 + (self.y - vector2.y)**2 + (self.z + vector2.z)**2)


def calc_normal_my(vec1, vec2):
    return Vector3D(
        vec1.y * vec2.z - vec1.z * vec2.y,
        vec1.z * vec2.x - vec1.x * vec2.z,
        vec1.x * vec2.y - vec1.y * vec2.x,
    ).normalized


# FIXME: Remove
def calc_normal_ei(vec1, vec2):
    p1 = Point3D(0, 0, 0)
    p2 = Point3D(vec1.x, vec1.y, vec1.z)
    p3 = Point3D(vec2.x, vec2.y, vec2.z)

    e1 = p2.x - p1.x
    e2 = p2.y - p1.y
    e4 = p3.x - p1.x
    e5 = p3.y - p1.y

    c = e1 * e5 - e2 * e4

    e3 = p2.z - p1.z
    e6 = p3.z - p1.z

    a = e2 * e6 - e3 * e5
    b = e3 * e4 - e1 * e6

    length = math.sqrt(a*a + b*b + c*c)
    return Vector3D(
        a / length,
        b / length,
        c / length,
    )
