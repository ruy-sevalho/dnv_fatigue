# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from quantities import Quantity
from dnv_fatigue.model import fatigue_stress_range, SNCurveType, Environment

# Press the green button in the gutter to run the script.
from dnv_fatigue.weibull import side_above_waterline_h

if __name__ == '__main__':
    ship_length = Quantity(316, "m")
    ship_depth = Quantity(31.5, "m")
    ship_draft = Quantity(23.416, "m")
    z = Quantity(28, "m")
    ha = 0.005
    h = side_above_waterline_h(
        ship_length=ship_length,
        ship_depth=ship_depth,
        ship_draft=ship_draft,
        z=z,
        ha=ha
    )
    print(f"")
    print(f"ship_length: {ship_length}")
    print(f"ship_depth: {ship_depth}")
    print(f"ship_depth: {ship_draft}")
    print(f"z: {z}")
    print(f"ha: {ha}")
    print(f"h: {h}")
    thickness = Quantity(12.7, "mm")
    sn = SNCurveType.F
    env = Environment.AIR
    DFF = 1
    life = 25
    # print(f"thickness: {thickness}")
    # print(f"SN curve type: {sn}")
    # print(f"env: {env}")
    # print(f"DFF: {DFF}")
    # print(f"Design life: {life}")
    # for h in range(5, 12):
    #     stress = fatigue_stress_range(
    #         thickness=thickness,
    #         weibull_factor=h / 10,
    #         sn_curve_type=sn,
    #         environment=env,
    #         design_fatigue_factor=1,
    #         design_life=25,
    #     )
    #     print(f"h: {h / 10}  -  stress: {stress}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
