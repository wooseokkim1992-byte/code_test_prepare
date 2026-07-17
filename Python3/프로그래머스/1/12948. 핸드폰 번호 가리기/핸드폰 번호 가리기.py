def solution(phone_number):
    answer = ''
    str_arr = list(phone_number)
    length = len(str_arr)
    for i in range(0,length-4):
        str_arr[i]="*"
    answer = ''.join(str_arr)
    return answer