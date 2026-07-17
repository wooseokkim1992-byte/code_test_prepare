def solution(my_string):
    answer = ''
    str_list = list(my_string.lower())
    str_len = len(str_list)
    for i in range(str_len-1):
        min_idx = i
        for j in range(i+1,str_len):
            if str_list[j]<=str_list[min_idx]:
                min_idx=j
        str_list[min_idx],str_list[i]=str_list[i],str_list[min_idx]
    answer = ''.join(str_list)
    
    
    return answer