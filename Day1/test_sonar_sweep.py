import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from helper.helpers import parse, answer
from sonar_sweep import count_depth_measurement


val1 = parse(1, int)
print(count_depth_measurement(val1))
print(answer(1.1, count_depth_measurement(val1), 1429))

