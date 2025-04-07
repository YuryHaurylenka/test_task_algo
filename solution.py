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
    # Iterate through each index in the list using '_' as the loop variable
    for _ in range(n):
        # If the current index is beyond the furthest reachable index, return False
        if _ > max_reachable:
            return False
        # Update the maximum reachable index with the furthest jump possible from the current index
        max_reachable = max(max_reachable, _ + nums[_])
        # If we can reach or surpass the last index, return True immediately
        if max_reachable >= n - 1:
            return True
    return False
