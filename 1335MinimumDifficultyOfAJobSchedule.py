"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work
on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job
schedule is the sum of difficulties of each day of the d days. The difficulty
of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty
of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule
for the jobs return -1.
"""

import unittest


def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
    # def find_max_window_difficulty_window():

    length = len(jobDifficulty)
    if d > length:
        return -1
    if d == length:
        return sum(jobDifficulty)

    window = length - d + 1
    max_window_difficulty = window_difficulty = sum(
        jobDifficulty[:window])
    max_window_difficulty_start_index = 0

    for left in range(1, length - window + 1):
        right = left + window - 1
        window_difficulty += jobDifficulty[right] - jobDifficulty[left-1]
        if window_difficulty > max_window_difficulty:
            max_window_difficulty = window_difficulty
            max_window_difficulty_start_index = left

    return (sum(jobDifficulty[:max_window_difficulty_start_index]) +
            max(jobDifficulty[max_window_difficulty_start_index:max_window_difficulty_start_index + window]) +
            sum(jobDifficulty[max_window_difficulty_start_index + window:]))


class Test(unittest.TestCase):
    test_cases = (
        ([6, 5, 4, 3, 2, 1], 2, 7),
        ([9, 9, 9], 4, -1),
        ([1, 1, 1], 3, 3),
        ([186, 398, 479, 206, 885, 423, 805, 112, 925,
         656, 16, 932, 740, 292, 671, 360], 4, 1803)
    )

    def test_minDifficulty(self):
        for difficulties, days, expected in self.test_cases:
            assert minDifficulty(difficulties, days) == expected


if __name__ == "__main__":
    unittest.main()
