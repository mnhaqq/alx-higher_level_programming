#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    dic = dict()
    roman_nums = "IVXLCDM"
    vals = [1, 5, 10, 50, 100, 500, 1000]
    for i in range(len(roman_nums)):
        dic[roman_nums[i]] = vals[i]

    exceptions = {"IV", "IX", "XL", "XC", "CD", "CM"}

    answer = i = 0
    last = False
    while i < len(roman_string)-1:
        if (roman_string[i] + roman_string[i+1]) in exceptions:
            if i == len(roman_string)-2:
                last = True
            answer += dic.get(roman_string[i+1]) - dic.get(roman_string[i])
            i += 2
            continue
        answer += dic.get(roman_string[i])
        i += 1
    if not last:
        answer += dic.get(roman_string[i])
    return answer
