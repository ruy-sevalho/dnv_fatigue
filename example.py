# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from quantities import Quantity

from dnv_fatigue.model import fatigue_stress_range, SNCurveType, Environment

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for h in range(1, 11):
        stress = fatigue_stress_range(
            Quantity(35, "mm"),
            h / 10,
            SNCurveType.F3,
            Environment.AIR,
            2,
            25,
        )
        print(f"h: {h / 10}  -  stress: {stress}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
