import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper.helpers import quantify


def count_depth_measurement(nums: list[int]) -> int:
    """How many measurements are larger than the previous measurement? 

    Args:
        depth: an list of values from the sonar reader
    returns:
        number: the number of measurements that are larger than the previous
                measurement
    """
    return quantify(nums[i] > nums[i - 1]
                    for i in range(1, len(nums)))

