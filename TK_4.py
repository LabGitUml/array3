def multiply_by_average(list_of_data):
    mul_aver = list_of_data[:]
    if len(mul_aver) > 0:
        aver = sum(mul_aver)/len(mul_aver)
    for i in range(len(mul_aver)):
        mul_aver[i] = mul_aver[i]*aver
    return mul_aver