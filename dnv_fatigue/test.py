import pytest as pt
from quantities import Quantity

from dnv_fatigue.model import (
    SNCurveType, Environment, allowable_extreme_stress, utilization_factor, reduction_factor,
    allowable_stress_range_thickness_corrected, fatigue_stress_range
)


def same_units_simplify(q1: Quantity, q2: Quantity):
    q1 = q1.simplified
    q2 = q2.simplified
    if not q1.units == q2.units:
        raise ValueError("q1 and q2 don't have the same units")
    return q1, q2


@pt.mark.parametrize(
    ("weibull_factor", "sn_curve_type", "environment", "expected_value"),
    ((0.97, SNCurveType.F3, Environment.AIR, Quantity(178.18, "MPa")),)
)
def test_allowable_extreme_stress(
        weibull_factor: float,
        sn_curve_type: SNCurveType,
        environment: Environment,
        expected_value: Quantity
):
    calculated = allowable_extreme_stress(
        weibull_factor=weibull_factor,
        sn_curve_type=sn_curve_type,
        environment=environment
    )
    calculated, expected = same_units_simplify(calculated, expected_value)
    assert calculated == pt.approx(expected, rel=0.01)


@pt.mark.parametrize(
    ("design_fatigue_factor", "design_life", "expected_value"),
    ((2, 25, 0.4,),)
)
def test_utilization_factor(
        design_fatigue_factor: float,
        design_life: float,
        expected_value: float
):
    calculated = utilization_factor(
        design_fatigue_factor=design_fatigue_factor, design_life=design_life
    )
    assert calculated == pt.approx(expected_value, rel=0.01)


@pt.mark.parametrize(
    ("weibull_factor", "utilization_factor", "sn_curve_type", "environment", "expected_value"),
    ((0.97, 0.4, SNCurveType.F3, Environment.AIR, 0.783,),)
)
def test_reduction_factor(
        weibull_factor: float,
        utilization_factor: float,
        sn_curve_type: SNCurveType,
        environment: Environment,
        expected_value: float
):
    calculated = reduction_factor(
        weibull_factor=weibull_factor,
        utilization_factor=utilization_factor,
        sn_curve_type=sn_curve_type,
        environment=environment
    )
    assert calculated == pt.approx(expected_value, rel=0.01)


@pt.mark.parametrize(
    ("thickness", "sn_curve_type", "stress_range", "expected_value"),
    ((Quantity(35, "mm"), SNCurveType.F3, Quantity(139.55, "MPa"), Quantity(128.29, "MPa")),)
)
def test_allowable_stress_range_thickness_corrected(
        thickness: Quantity,
        sn_curve_type: SNCurveType,
        stress_range: Quantity,
        expected_value: Quantity
):
    calculated = allowable_stress_range_thickness_corrected(
        thickness=thickness,
        sn_curve_type=sn_curve_type,
        stress_range=stress_range,
    )
    assert calculated == pt.approx(expected_value, rel=0.01)


@pt.mark.parametrize(
    (
            "thickness",
            "weibull_factor",
            "sn_curve_type",
            "environment",
            "design_fatigue_factor",
            "design_life",
            "expected_value"),
    (
            (
                    Quantity(35, "mm"),
                    0.97,
                    SNCurveType.F3,
                    Environment.AIR,
                    2,
                    25,
                    Quantity(128.29, "MPa")
            ),
    )
)
def test_fatigue_stress_range(
        thickness: Quantity,
        weibull_factor: float,
        sn_curve_type: SNCurveType,
        environment: Environment,
        design_fatigue_factor: float,
        design_life: float,
        expected_value: Quantity
):
    calculated = fatigue_stress_range(
        thickness=thickness,
        weibull_factor=weibull_factor,
        sn_curve_type=sn_curve_type,
        environment=environment,
        design_fatigue_factor=design_fatigue_factor,
        design_life=design_life
    )
    calculated, expected_value = same_units_simplify(calculated, expected_value)
    assert calculated == pt.approx(expected_value, rel=0.01)
