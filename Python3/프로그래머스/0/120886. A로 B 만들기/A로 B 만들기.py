def solution(before, after):
    answer = 0
    bef_list = list(before)
    aft_list = list(after)
    bef_list.sort()
    aft_list.sort()
    for i in range(0,len(aft_list)):
        if bef_list[i]!=aft_list[i]:
            return 0
    return 1