#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        ans = 0
        try:
            ans = my_list_1[i]/my_list_2[i]
        except TypeError:
            ans = 0
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(ans)
        i += 1
    return new_list
