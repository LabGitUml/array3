def divide_by_average(list_of_data):
    div_aver = list_of_data[:]
    if len(div_aver) > 0:
        aver = sum(div_aver)/len(div_aver)
    for i in range(len(div_aver)):
        div_aver[i]=div_aver[i]/aver
    return div_aver