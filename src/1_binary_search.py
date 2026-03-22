import unittest


type number = int | float


def binary_search(nums: list[number], target: number) -> int | None:
    low: int = 0
    high: int = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


class TestBinarySearch(unittest.TestCase):
    def test_result(self):
        nums: list[number] = [-1, 0, 3, 5, 9, 12]
        target: number = 9
        self.assertEqual(binary_search(nums, target), 4)

    def test_none(self):
        nums: list[number] = [-1,0,3,5,9,12]
        target: number = 2
        self.assertEqual(binary_search(nums, target), None)


if __name__ == "__main__":
    unittest.main()
