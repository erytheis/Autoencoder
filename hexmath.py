# Generated code -- http://www.redblobgames.com/grids/hexagons/

from __future__ import division
from __future__ import print_function
import collections
import math

class Hex():

    def Hex(q, r, s = None, v = None):
        self.s = s if s is not None else - q - r
        self.v = v if v is not None else 0
        assert not (round(q + r + s) != 0), "q + r + s must be 0"



def set_neighbours(self):
    neighbors = []
    for direction in hex_directions:
        print(type(direction))
        neighbors.append(hex_neighbor(self, direction))
    return neighbors

hex_directions = [Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]

def hex_direction(direction):
    return hex_directions[direction]


def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)


def hex_subtract(a, b):
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s)


def hex_neighbor(hex, direction):
    return hex_add(hex, direction)


def hex_length(hex):
    return (abs(hex.q) + abs(hex.r) + abs(hex.s)) // 2


def hex_distance(a, b):
    return hex_length(hex_subtract(a, b))
