"""
Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane, return the maximum number of points that lie on the same straight
line.
"""

from collections import defaultdict
from math import inf


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) < 3:
            return len(points)
        line_point_map = self.getLines(points)
        self.distributePointsToLines(points, line_point_map)
        return self.findMaxPoints(line_point_map)

    def getLines(
        self, points: list[list[int]]
    ) -> dict[tuple[float, float], set[tuple[int, int]]]:
        line_point_map: dict[
            tuple[float, float], set[tuple[int, int]]
        ] = defaultdict(set)
        for pt1 in points:
            for pt2 in points:
                if pt1 == pt2:
                    continue
                self.addEquationsToMap(pt1, pt2, line_point_map)
        return line_point_map

    def distributePointsToLines(
        self,
        points: list[list[int]],
        line_point_map: dict[tuple[float, float], set[tuple[int, int]]],
    ) -> None:
        for point in points:
            for line in line_point_map.keys():
                self.addPointToLine(point, line, line_point_map)

    def addPointToLine(
        self,
        point: list[int],
        line: tuple[float, float],
        line_point_map: dict[tuple[float, float], set[tuple[int, int]]],
    ) -> None:
        if self.isOnVerticalLine(point[0], line) or self.isOnLine(point, line):
            line_point_map[line].add(tuple(point))

    def isOnLine(self, point: list[int], line: tuple[float, float]) -> bool:
        m, b = line
        x, y = point
        return y == m * x + b

    def isOnVerticalLine(self, x: int, line: tuple[float, float]) -> bool:
        m, b = line
        return m == float(inf) and b == x

    def findMaxPoints(
        self, line_point_map: dict[tuple[float, float], set[tuple[int, int]]]
    ) -> int:
        most_points = 0
        for pts in line_point_map.values():
            most_points = max(most_points, len(pts))
        return most_points

    def addEquationsToMap(
        self,
        pt1: list[int],
        pt2: list[int],
        line_point_map: dict[tuple[float, float], set[tuple[int, int]]],
    ) -> None:
        equation = self.getEquation(pt1, pt2)
        line_point_map[equation].add(tuple(pt1))
        line_point_map[equation].add(tuple(pt2))

    def getEquation(self, p1: list[int], p2: list[int]) -> tuple[float, float]:
        if self.isVerticalLine(p1, p2):
            return float(inf), p1[0]
        m = self.getSlope(p1, p2)
        b = self.getYIntercept(p1, m)
        return m, b

    def isVerticalLine(self, p1: list[int], p2: list[int]) -> bool:
        return p1[0] == p2[0]

    def getYIntercept(self, p1: list[int], m: float) -> float:
        return p1[1] - m * p1[0]

    def getSlope(self, p1: list[int], p2: list[int]) -> float:
        x1, y1 = p1
        x2, y2 = p2
        return (y2 - y1) / (x2 - x1)
