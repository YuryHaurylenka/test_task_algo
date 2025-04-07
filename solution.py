def can_jump(nums: list[int]) -> bool:
    """
    Determines if it is possible to reach the last index of the list.

    Each element in the list represents the maximum jump length from that position.

    Parameters:
    nums (list[int]): A list of non-negative integers.

    Returns:
    bool: True if the last index can be reached, otherwise False.
    """
    max_reachable = 0
    n = len(nums)

    # Iterate through each index in the list
    for i in range(n):
        # If the current index is beyond the furthest reachable index, return False
        if i > max_reachable:
            return False

        # Update the maximum reachable index with the furthest jump possible from index i
        max_reachable = max(max_reachable, i + nums[i])

        # If we can reach or surpass the last index, return True immediately
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
