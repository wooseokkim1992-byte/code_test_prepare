def solution(my_string):
    answer = ''
    vowel = ['a','e','i','o','u']
    for ch in my_string:
        if ch not in vowel:
            answer+=ch
    return answer