

def average(nums: list[int]) -> float:
    """
    Gives the average value of given list of numbers

    Args:
        nums (list[int]): List of numbers

    Returns:
        float: average value of given list of numbers

    """
    return sum(nums) / len(nums)


def median(nums: list[int]) -> float:
    """
    Gives the median value of given list of numbers

    Args:
        nums (list[int]): List of numbers

    Returns:
        float: median value of given list of numbers

    """
    return sorted(nums)[len(nums) // 2] 

def mode(nums: list[int]) -> int:
    """
    Gives the mode value of given list of numbers

    Args:
        nums (list[int]): List of numbers

    Returns:
        int: mode value of given list of numbers

    """
    return max(set(nums), key=nums.count)