import sys


def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = float(-sys.maxsize)
    current_sum = 0
    for x in numbers:
        # Either continue the subarray or start a new one from this element
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


print(max_subarray([10, -15, -15, -15, 5]))
