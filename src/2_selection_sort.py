import unittest


type number = int | float


def minimum_index(nums: list[number]) -> int:
    """This function returns the index of smallest element in nums list"""
    minimum = float("+inf")
    result = -1

    for index, num in enumerate(nums):
        if num < minimum:
            minimum = num
            result = index

    return result


def selection_sort(nums: list[number]) -> list[number]:
    "This function returns sorted copy of nums, sorted with selection sort algorithm"
    result: list[number] = []
    nums_copy = nums.copy()

    for _ in range(len(nums_copy)):
        smallest = minimum_index(nums_copy)
        result.append(nums_copy.pop(smallest))

    return result


class TestSelectionSort(unittest.TestCase):
    def test_minimum_index(self):
        nums = [8, 2, 99, -10.2, -44, 22]
        result = minimum_index(nums)
        self.assertEqual(nums[result], -44)

    def test_selection_sort(self):
        nums = [8, 2, 99, -10.2, -44, 22]
        sorted_nums = sorted(nums)
        selection_sorted_nums = selection_sort(nums)

        self.assertEqual(selection_sorted_nums, sorted_nums)


if __name__ == "__main__":
    unittest.main()
