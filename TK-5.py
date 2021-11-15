import math
def sqrt_list (list_of_data):
    if len(list_of_data)>0:
        for i in range(len(list_of_data)):
            list_of_data[i] = math.sqrt(list_of_data[i])
    return list_of_data


