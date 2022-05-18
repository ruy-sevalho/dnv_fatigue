from enum import Enum

import numpy as np
from quantities import Quantity


class Environment(str, Enum):
    AIR = 'AIR'
    SEAWATER_WITH_CATHODIC_PROTECTION = "SEAWATER_WITH_CATHODIC_PROTECTION"


class SNCurveType(str, Enum):
    B1 = "B1"
    B2 = "B2"
    C = "C"
    C1 = "C1"
    C2 = "C2"
    D = "D"
    T = "T"
    E = "E"
    F = "F"
    F1 = "F1"
    F3 = "F3"
    G = "G"
    W1 = "W1"
    W2 = "W2"
    W3 = "W3"


WEIBULL_ARRAY = np.array([0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 1.10, 1.20])

TABLE_5_2 = {
    SNCurveType.B1: np.array([1449.3, 1092.2, 861.2, 704.7, 594.1, 512.9, 451.4, 403.6]),
    SNCurveType.B2: np.array([1268.1, 955.7, 753.6, 616.6, 519.7, 448.7, 394.9, 353.1]),
    SNCurveType.C: np.array([1319.3, 919.6, 688.1, 542.8, 445.5, 377.2, 326.9, 289.0]),
    SNCurveType.C1: np.array([1182.0, 824.0, 616.5, 486.2, 399.2, 337.8, 292.9, 258.9]),
    SNCurveType.C2: np.array([1055.3, 735.6, 550.3, 434.1, 356.3, 301.6, 261.5, 231.1]),
    SNCurveType.D: np.array([949.9, 662.1, 495.4, 390.7, 320.8, 271.5, 235.4, 208.1]),
    SNCurveType.T: np.array([949.9, 662.1, 495.4, 390.7, 320.8, 271.5, 235.4, 208.1]),
    SNCurveType.E: np.array([843.9, 588.3, 440.2, 347.2, 284.9, 241.2, 209.2, 184.9]),
    SNCurveType.F: np.array([749.2, 522.3, 390.8, 308.2, 253.0, 214.1, 185.6, 164.1]),
    SNCurveType.F1: np.array([664.8, 463.4, 346.7, 273.5, 224.5, 190.0, 164.7, 145.6]),
    SNCurveType.F3: np.array([591.1, 412.0, 308.3, 243.2, 199.6, 169.0, 146.5, 129.4]),
    SNCurveType.G: np.array([527.6, 367.8, 275.2, 217.1, 178.2, 150.8, 130.8, 115.6]),
    SNCurveType.W1: np.array([475.0, 331.0, 247.8, 195.4, 160.4, 135.8, 117.7, 104.0]),
    SNCurveType.W2: np.array([422.1, 294.1, 220.1, 173.6, 142.5, 120.6, 104.6, 92.5]),
    SNCurveType.W3: np.array([379.9, 264.8, 198.2, 156.0, 128.2, 108.6, 94.2, 83.2]),
}

TABLE_5_3 = {
    SNCurveType.B1: np.array([1309.8, 996.0, 793.0, 655.2, 557.4, 485.3, 430.5, 387.6]),
    SNCurveType.B2: np.array([1146.0, 871.5, 693.9, 573.3, 487.7, 424.7, 376.6, 339.1]),
    SNCurveType.C: np.array([1038.5, 745.5, 573.6, 464.3, 389.8, 336.7, 297.0, 266.5]),
    SNCurveType.C1: np.array([930.5, 668.0, 513.9, 415.8, 349.3, 301.5, 266.1, 238.7]),
    SNCurveType.C2: np.array([830.7, 596.3, 458.7, 371.3, 311.7, 269.2, 237.6, 213.1]),
    SNCurveType.D: np.array([747.8, 536.7, 413.0, 334.2, 280.7, 242.4, 213.9, 191.9]),
    SNCurveType.T: np.array([747.8, 536.7, 413.0, 334.2, 280.7, 242.4, 213.9, 191.9]),
    SNCurveType.E: np.array([664.3, 476.9, 367.0, 297.0, 249.3, 215.3, 190.1, 170.5]),
    SNCurveType.F: np.array([589.8, 423.4, 325.8, 263.6, 221.4, 191.1, 168.6, 151.3]),
    SNCurveType.F1: np.array([523.3, 375.7, 289.0, 233.9, 196.4, 169.6, 149.6, 134.3]),
    SNCurveType.F3: np.array([465.3, 334.0, 257.0, 208.0, 174.6, 150.9, 133.1, 119.3]),
    SNCurveType.G: np.array([415.3, 298.2, 229.4, 185.7, 155.9, 134.6, 118.8, 106.6]),
    SNCurveType.W1: np.array([373.9, 268.3, 206.6, 167.1, 140.3, 121.2, 106.9, 95.9]),
    SNCurveType.W2: np.array([332.3, 238.4, 183.5, 148.5, 124.7, 107.7, 95.0, 85.3]),
    SNCurveType.W3: np.array([299.1, 214.7, 165.2, 133.4, 112.2, 96.9, 85.6, 76.7]),
}

TABLE_5_4 = {
    0.1: np.array([0.57, 0.575, 0.581, 0.587, 0.592, 0.597, 0.602, 0.603]),
    0.2: np.array([0.674, 0.678, 0.682, 0.686, 0.69, 0.694, 0.698, 0.701]),
    0.22: np.array([0.69, 0.693, 0.697, 0.701, 0.705, 0.709, 0.712, 0.715]),
    0.27: np.array([0.725, 0.728, 0.731, 0.735, 0.738, 0.742, 0.745, 0.748]),
    0.3: np.array([0.744, 0.747, 0.75, 0.753, 0.756, 0.759, 0.762, 0.765]),
    0.33: np.array([0.762, 0.764, 0.767, 0.77, 0.773, 0.776, 0.778, 0.781]),
    0.4: np.array([0.798, 0.8, 0.803, 0.805, 0.808, 0.81, 0.812, 0.815]),
    0.5: np.array([0.843, 0.845, 0.846, 0.848, 0.85, 0.852, 0.854, 0.856]),
    0.6: np.array([0.882, 0.883, 0.884, 0.886, 0.887, 0.888, 0.89, 0.891]),
    0.67: np.array([0.906, 0.907, 0.908, 0.909, 0.91, 0.911, 0.912, 0.913]),
    0.7: np.array([0.916, 0.917, 0.917, 0.919, 0.92, 0.92, 0.921, 0.922]),
    0.8: np.array([0.946, 0.947, 0.947, 0.948, 0.949, 0.949, 0.95, 0.95]),
    1.0: np.array([1., 1., 1., 1., 1., 1., 1., 1.])
}

TABLE_5_5 = {
    0.1: np.array([0.497, 0.511, 0.526, 0.54, 0.552, 0.563, 0.573, 0.582]),
    0.2: np.array([0.609, 0.62, 0.632, 0.642, 0.652, 0.661, 0.67, 0.677]),
    0.22: np.array([0.627, 0.638, 0.648, 0.659, 0.668, 0.677, 0.685, 0.692]),
    0.27: np.array([0.661, 0.676, 0.686, 0.695, 0.703, 0.711, 0.719, 0.725]),
    0.3: np.array([0.688, 0.697, 0.706, 0.715, 0.723, 0.73, 0.737, 0.743]),
    0.33: np.array([0.708, 0.717, 0.725, 0.733, 0.741, 0.748, 0.754, 0.76]),
    0.4: np.array([0.751, 0.758, 0.765, 0.772, 0.779, 0.785, 0.79, 0.795]),
    0.5: np.array([0.805, 0.81, 0.816, 0.821, 0.826, 0.831, 0.835, 0.839]),
    0.6: np.array([0.852, 0.856, 0.86, 0.864, 0.868, 0.871, 0.875, 0.878]),
    0.67: np.array([0.882, 0.885, 0.888, 0.891, 0.894, 0.897, 0.9, 0.902]),
    0.7: np.array([0.894, 0.897, 0.9, 0.902, 0.905, 0.908, 0.91, 0.912]),
    0.8: np.array([0.932, 0.934, 0.936, 0.938, 0.939, 0.941, 0.942, 0.944]),
    1.0: np.array([1., 1., 1., 1., 1., 1., 1., 1.])
}

TABLE_5_6 = {
    0.1: np.array([0.583, 0.593, 0.602, 0.61, 0.617, 0.621, 0.625, 0.627]),
    0.2: np.array([0.684, 0.691, 0.699, 0.705, 0.711, 0.715, 0.718, 0.72]),
    0.22: np.array([0.699, 0.706, 0.714, 0.72, 0.725, 0.729, 0.732, 0.735]),
    0.27: np.array([0.733, 0.74, 0.746, 0.752, 0.757, 0.76, 0.763, 0.766]),
    0.3: np.array([0.751, 0.758, 0.764, 0.769, 0.773, 0.777, 0.78, 0.782]),
    0.33: np.array([0.768, 0.774, 0.78, 0.785, 0.789, 0.792, 0.795, 0.792]),
    0.4: np.array([0.804, 0.809, 0.814, 0.818, 0.822, 0.825, 0.827, 0.829]),
    0.5: np.array([0.848, 0.851, 0.855, 0.858, 0.861, 0.864, 0.866, 0.867]),
    0.6: np.array([0.885, 0.888, 0.891, 0.893, 0.896, 0.897, 0.899, 0.9]),
    0.67: np.array([0.909, 0.911, 0.913, 0.915, 0.917, 0.919, 0.92, 0.921]),
    0.7: np.array([0.918, 0.92, 0.922, 0.924, 0.926, 0.927, 0.928, 0.929]),
    0.8: np.array([0.948, 0.949, 0.95, 0.952, 0.953, 0.954, 0.955, 0.955]),
    1.0: np.array([1., 1., 1., 1., 1., 1., 1., 1.])
}
TABLE_5_7 = {
    0.1: np.array([0.535, 0.558, 0.577, 0.593, 0.605, 0.613, 0.619, 0.623]),
    0.2: np.array([0.64, 0.659, 0.676, 0.689, 0.699, 0.707, 0.713, 0.717]),
    0.22: np.array([0.657, 0.675, 0.691, 0.703, 0.713, 0.721, 0.727, 0.731]),
    0.27: np.array([0.694, 0.71, 0.725, 0.736, 0.745, 0.752, 0.758, 0.762]),
    0.3: np.array([0.714, 0.729, 0.743, 0.754, 0.763, 0.769, 0.775, 0.779]),
    0.33: np.array([0.732, 0.747, 0.76, 0.77, 0.779, 0.785, 0.79, 0.794]),
    0.4: np.array([0.772, 0.785, 0.796, 0.805, 0.812, 0.818, 0.822, 0.825]),
    0.5: np.array([0.821, 0.831, 0.84, 0.847, 0.853, 0.858, 0.862, 0.864]),
    0.6: np.array([0.864, 0.872, 0.879, 0.885, 0.889, 0.893, 0.896, 0.898]),
    0.67: np.array([0.892, 0.898, 0.903, 0.908, 0.912, 0.915, 0.917, 0.919]),
    0.7: np.array([0.903, 0.908, 0.913, 0.917, 0.921, 0.924, 0.926, 0.927]),
    0.8: np.array([0.938, 0.941, 0.945, 0.947, 0.949, 0.951, 0.953, 0.954]),
    1.0: np.array([1., 1., 1., 1., 1., 1., 1., 1.])
}
DESIGN_LIFE_ARRAY = np.array([5, 10, 15, 20, 25, 30, 50])
TABLE_5_8 = {
    1: np.array([4.0, 2.0, 1.33, 1.00, 0.80, 0.67, 0.40]),
    2: np.array([2.0, 1.0, 0.67, 0.50, 0.40, 0.33, 0.20]),
    3: np.array([1.33, 0.67, 0.44, 0.33, 0.27, 0.22, 0.13]),
    5: np.array([0.80, 0.40, 0.27, 0.20, 0.16, 0.13, 0.08]),
    10: np.array([0.40, 0.20, 0.13, 0.10, 0.08, 0.07, 0.04])
}
TABLE_2_1 = {
    SNCurveType.B1: 0,
    SNCurveType.B2: 0,
    SNCurveType.C: 0.15,
    SNCurveType.C1: 0.15,
    SNCurveType.C2: 0.15,
    SNCurveType.D: 0.20,
    SNCurveType.T: 0.25,
    SNCurveType.E: 0.25,
    SNCurveType.F: 0.25,
    SNCurveType.F1: 0.25,
    SNCurveType.F3: 0.25,
    SNCurveType.G: 0.25,
    SNCurveType.W1: 0.25,
    SNCurveType.W2: 0.25,
    SNCurveType.W3: 0.25,
}


def allowable_extreme_stress(
        weibull_factor: float,
        sn_curve_type: SNCurveType,
        environment: Environment
):
    table = {
        environment.AIR: TABLE_5_2,
        environment.SEAWATER_WITH_CATHODIC_PROTECTION: TABLE_5_3,
    }
    mag = np.interp(
        x=weibull_factor,
        xp=WEIBULL_ARRAY,
        fp=table[environment][sn_curve_type]
    )
    return Quantity(mag, "MPa")


def utilization_factor(design_fatigue_factor: float, design_life: float):
    if design_fatigue_factor in TABLE_5_8.keys():
        return np.interp(
            x=design_life,
            xp=DESIGN_LIFE_ARRAY,
            fp=TABLE_5_8[design_fatigue_factor],
        )


def reduction_factor(
        weibull_factor: float,
        utilization_factor: float,
        sn_curve_type: SNCurveType,
        environment: Environment
):
    tables_air = {
        SNCurveType.B1: TABLE_5_4,
        SNCurveType.B2: TABLE_5_4,
        SNCurveType.C: TABLE_5_5,
        SNCurveType.C1: TABLE_5_5,
        SNCurveType.C2: TABLE_5_5,
        SNCurveType.D: TABLE_5_5,
        SNCurveType.T: TABLE_5_5,
        SNCurveType.E: TABLE_5_5,
        SNCurveType.F: TABLE_5_5,
        SNCurveType.F1: TABLE_5_5,
        SNCurveType.F3: TABLE_5_5,
        SNCurveType.G: TABLE_5_5,
        SNCurveType.W1: TABLE_5_5,
        SNCurveType.W2: TABLE_5_5,
        SNCurveType.W3: TABLE_5_5,
    }
    tables_sea = {
        SNCurveType.B1: TABLE_5_6,
        SNCurveType.B2: TABLE_5_6,
        SNCurveType.C: TABLE_5_7,
        SNCurveType.C1: TABLE_5_7,
        SNCurveType.C2: TABLE_5_7,
        SNCurveType.D: TABLE_5_7,
        SNCurveType.T: TABLE_5_7,
        SNCurveType.E: TABLE_5_7,
        SNCurveType.F: TABLE_5_7,
        SNCurveType.F1: TABLE_5_7,
        SNCurveType.F3: TABLE_5_7,
        SNCurveType.G: TABLE_5_7,
        SNCurveType.W1: TABLE_5_7,
        SNCurveType.W2: TABLE_5_7,
        SNCurveType.W3: TABLE_5_7,
    }
    tables = {
        Environment.AIR: tables_air,
        Environment.SEAWATER_WITH_CATHODIC_PROTECTION: tables_sea
    }
    if utilization_factor in TABLE_5_4.keys():
        return np.interp(
            x=weibull_factor,
            xp=WEIBULL_ARRAY,
            fp=tables[environment][sn_curve_type][utilization_factor]
        )


def allowable_stress_range(allowable_extreme_stress: Quantity, reduction_factor: float):
    return allowable_extreme_stress * reduction_factor


REFERENCE_THICKNESS = Quantity(25, "mm")


def allowable_stress_range_thickness_corrected(
        thickness: Quantity,
        sn_curve_type: SNCurveType,
        stress_range: Quantity
):
    exponent = TABLE_2_1[sn_curve_type]
    return stress_range * (REFERENCE_THICKNESS / thickness) ** exponent


def fatigue_stress_range(
        thickness: Quantity,
        weibull_factor: float,
        sn_curve_type: SNCurveType,
        environment: Environment,
        design_fatigue_factor: float,
        design_life: float
):
    allowable_extreme_stress_value = allowable_extreme_stress(
        weibull_factor=weibull_factor,
        sn_curve_type=sn_curve_type,
        environment=environment,
    )
    utilization_factor_value = utilization_factor(
        design_fatigue_factor=design_fatigue_factor,
        design_life=design_life
    )
    reduction_factor_value = reduction_factor(
        weibull_factor=weibull_factor,
        utilization_factor=utilization_factor_value,
        sn_curve_type=sn_curve_type,
        environment=environment
    )
    allowable_stress_range_value = allowable_stress_range(
        allowable_extreme_stress=allowable_extreme_stress_value,
        reduction_factor=reduction_factor_value
    )
    return allowable_stress_range_thickness_corrected(
        thickness=thickness,
        sn_curve_type=sn_curve_type,
        stress_range=allowable_stress_range_value
    )
