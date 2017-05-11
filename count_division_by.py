def divide_by_3(number):
    return_list = []
    for i in range(1, number):
        if i%3==0:
            return_list.append(i)
    return return_list

def divide_by_5(number):
    return_list = []
    for i in range(1, number):
        if i%5==0:
            return_list.append(i)
    return return_list


def solution(number):
    list_1 = divide_by_5(number)
    list_2 = divide_by_3(number)
    return (sum(list(set(list_1+list_2))))