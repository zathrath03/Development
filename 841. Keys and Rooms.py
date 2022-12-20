"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except
for room 0. Your goal is to visit all the rooms. However, you cannot enter a
locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has
a number on it, denoting which room it unlocks, and you can take all of them
with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if
you visited room i, return true if you can visit all the rooms, or false
otherwise.

Constraints:
n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
"""


import unittest


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        unvisited_rooms = 2 ** len(rooms) - 2
        keys: set[int] = set((0,))

        while keys:
            new_keys = self.get_new_keys(rooms, unvisited_rooms, keys.pop())
            unvisited_rooms = self.handle_new_keys(
                unvisited_rooms, keys, new_keys)
            if not unvisited_rooms:
                return True

        return False

    def handle_new_keys(self, unvisited_rooms, keys, new_keys):
        for key in new_keys:
            key_bit = 1 << key
            keys.add(key)
            unvisited_rooms = unvisited_rooms & ~key_bit
        return unvisited_rooms

    def get_new_keys(self, rooms, unvisited_rooms, curr):
        new_keys = set()
        for key in rooms[curr]:
            key_bit = 1 << key
            if unvisited_rooms & key_bit != 0:
                new_keys.add(key)
        return new_keys


class Test(unittest.TestCase):
    test_cases = (
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
    )

    def test_canVisitAllRooms(self):
        sol = Solution()
        for rooms, expected in self.test_cases:
            assert sol.canVisitAllRooms(rooms) == expected


if __name__ == "__main__":
    unittest.main()
