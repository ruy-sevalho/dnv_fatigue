from enum import Enum

import numpy as np
from quantities import Quantity


def basic_ship_parameter(ship_length: Quantity):
    return 2.21 - 0.54 * np.log10(ship_length.rescale("m").magnitude)


def deck_longitudinal_h(ship_length: Quantity):
    """For deck longitudinals"""

    return basic_ship_parameter(ship_length)


def side_above_waterline_h(
        ship_length: Quantity,
        ship_depth: Quantity,
        ship_draft: Quantity,
        z: Quantity,
        ha: float,
):
    """For ship side above the waterline Tact <z <D"""

    factor: Quantity = (ship_depth - z) / (ship_depth - ship_draft)
    factor = factor.simplified
    factor = factor.magnitude
    return basic_ship_parameter(ship_length) + ha * factor


def side_below_waterline_h(
        ship_length: Quantity,
        ship_draft: Quantity,
        z: Quantity,
        ha: float,
):
    """For ship side above the waterline Tact <z <D"""

    factor1: Quantity = z / ship_draft
    factor1 = factor1.simplified
    factor1 = factor1.magnitude
    factor2: Quantity = 0.005 * (ship_draft - z)
    factor2 = factor2.rescale("m")
    factor2 = factor2.magnitude
    return basic_ship_parameter(ship_length) + ha * factor1 - factor2


def bottom_longitudinals(
        ship_length: Quantity,
        ship_draft: Quantity,
):
    """For bottom longitudinals"""
    return basic_ship_parameter(ship_length) - 0.005 * ship_draft.rescale("m").magnitude


def longitudinal_transverse_bulkheads(
        ship_length: Quantity,
        ha: float,
):
    """For longitudinal and transverse bulkheads"""

    return basic_ship_parameter(ship_length) - ha


if __name__ == '__main__':
    length = Quantity(200, "m")
    print(deck_longitudinal_h(length))
