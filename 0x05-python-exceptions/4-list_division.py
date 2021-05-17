#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    try:
        for elem in range(list_length):
            try:
                div_list.append(my_list_1[elem] / my_list_2[elem])
            except(TypeError, ZeroDivisionError, IndexError) as exception:
                if (isinstance(exception, TypeError)):
                    print("wrong type")
                elif (isinstance(exception, ZeroDivisionError)):
                    print("division by 0")
                elif (isinstance(exception, IndexError)):
                    print("out of range")
                div_list.append(0)
    except:
        pass
    finally:
        return div_list
