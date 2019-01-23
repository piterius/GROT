import unittest
from GROT import grot


class GROTTest(unittest.TestCase):

    def test_grot_first_matrix(self):
        sample = [
            ['u', 'd', 'u', 'u'],  # ↑ ↓ ↑ ↑
            ['u', 'r', 'l', 'l'],  # ↑ → ← ←
            ['u', 'u', 'l', 'u'],  # ↑ ↑ ← ↑
            ['l', 'd', 'u', 'l'],  # ← ↓ ↑ ←
        ]
        position = [3, 3]
        self.assertEqual(grot(sample), position)

    def test_grot_second_matrix(self):
        sample = [
            ['d', 'l', 'r', 'l'],  # ↓ ← → ←
            ['u', 'l', 'l', 'd'],  # ↑ ← ← ↓
            ['r', 'l', 'd', 'u'],  # → ← ↓ ↑
            ['d', 'l', 'u', 'd'],  # ↓ ← ↑ ↓
        ]
        position = [2, 1]
        self.assertEqual(grot(sample), position)

    def test_grot_third_matrix(self):
        sample = [
            ['u', 'd', 'u', 'd'],  # ↑ ↓ ↑ ↓
            ['u', 'r', 'l', 'd'],  # ↑ → ← ↓
            ['d', 'd', 'd', 'd'],  # ↓ ↓ ↓ ↓
            ['d', 'd', 'd', 'd'],  # ↓ ↓ ↓ ↓
        ]
        position = [0, 1]
        self.assertEqual(grot(sample), position)


if __name__ == '__main__':
    unittest.main()
