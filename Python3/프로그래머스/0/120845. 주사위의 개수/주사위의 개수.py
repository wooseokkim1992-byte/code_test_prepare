def solution(box, n):
    answer = 0
    x = int(box[0]/n)
    y = int(box[1]/n)
    z = int(box[2]/n)
    return x*y*z