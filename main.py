import sys
import importlib
from TK_1 import list_of_values
from TK_2 import cortege
from TK_3 import divide_by_average
from TK_4 import multiply_by_average

def main():
    TK_5 = importlib.import_module("TK_5")
    count_values = int(input('Get count data: '))
    list_data = input_values_list(count_values)
    print('list: ' + str(list_data))
    print('Min max values: ' + str(cortege(list_of_values)))
    print('Divide by average elements: ' + str(divide_by_average(list_of_data)))
    print('Myltiply by average elements: ' + str(multiply_by_average(list_of_data)))
    print('List of sqrt elements: ' + str(TK_5.sqrt_list(list_of_data)))
    return 0