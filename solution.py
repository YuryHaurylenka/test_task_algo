def can_jump(nums: list[int]) -> bool:
    max_reachable = 0
    n = len(nums)
    for i in range(n):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])
        if max_reachable >= n - 1:
            return True
    return False


if __name__ == "__main__":
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False)
    ]
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = can_jump(nums)
        print(f"Test case {i}: Input: {nums} -> Output: {result} (Expected: {expected})")
