def solution(numbers):
    answer = 0
    numbers.sort()
    return numbers[len(numbers)-1]*numbers[len(numbers)-2]