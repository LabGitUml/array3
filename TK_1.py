def list_of_values(value):
    list_of_data = []
    for i in range(value):
        list_of_data += [float(input('Enter' + str(i+1) + 'value: '))]
        return list_of_data