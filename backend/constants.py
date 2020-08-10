from enum import Enum


class SHAPE_TYPES(Enum):
    SPHERE = 1
    CUBE = 2


SHAPE_CHOICES = [
    (SHAPE_TYPES.SPHERE, 'Sphere'),
    (SHAPE_TYPES.CUBE, 'Cube'),
]