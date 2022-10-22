"""
The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.

For example, "#15c" is shorthand for the color "#1155cc".
The similarity between the two colors "#ABCDEF" and "#UVWXYZ" is
 -(AB - UV)2 - (CD - WX)2 - (EF - YZ)2.

Given a string color that follows the format "#ABCDEF", return a string
represents the color that is most similar to the given color and has a
shorthand (i.e., it can be represented as some "#XYZ").

Any answer which has the same highest similarity as the best answer will be
accepted.
"""


import unittest
from typing import Iterator


def similarRGB(color: str) -> str:
    def separate_colors(color: str) -> Iterator[str]:
        for i in range(1, 6, 2):
            yield color[i:i+2]

    def find_nearest_double_color(color: str) -> str:
        doubles = {0: "00", 17: "11", 34: "22", 51: "33", 68: "44",
                   85: "55", 102: "66", 119: "77", 136: "88", 153: "99",
                   170: "aa", 187: "bb", 204: "cc", 221: "dd", 238: "ee",
                   255: "ff"}
        color_int = int("0x" + color, 16)
        delta = {abs(k-color_int): v for k, v in doubles.items()}

        return delta[min(delta)]

    output = "#"

    for c in separate_colors(color):
        output += find_nearest_double_color(c)

    return output


class Test(unittest.TestCase):
    test_cases = [
        ("#09f166", "#11ee66"),
        ("#4e3fe1", "#5544dd")
    ]

    def test_similarRGB(self):
        for color, expected in self.test_cases:
            assert similarRGB(color) == expected


if __name__ == "__main__":
    unittest.main()
    # similarRGB("#09f166")
