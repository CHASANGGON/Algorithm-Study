# 주사위 게임 3
def solution(a, b, c, d):
    answer = 0

    # collection 아닌 set
    values = [a, b, c, d]
    set_values = set(values)

    if len(set_values) == 4:  # 모두 다른 경우
        return min(values)

    elif len(set_values) == 1:  # 모두 같은 경우
        return a * 1111

    elif len(set_values) == 2:
        for value in set_values: 
            if values.count(value) == 2:
                p = value
                q = (set_values - {p}).pop()
                return (10*p+q) ** 2

    elif len(set_values) == 2:
        p, q = set_values
        if values.count(p) == 2 and values.count(q) == 2:
            return (p+q) * abs(p-q)

    elif len(set_values) == 3:
        for value in set_values:
            if values.count(value) == 2:  # 2개가 같은 숫자 찾기
                p = value
                q, r = sorted(set_values - {p})  # 안전하게 두 개의 숫자 추출
                return q * r  # 남은 두 숫자의 곱

    return answer

a = 1
b = 2
c = 1
d = 2

print(solution(a, b, c, d))

# [PCCE 기출문제] 3번 / 나이 계산

year = int(input())
age_type = input()

if age_type == 'Korea':
    answer = 2030 - year + 1

elif age_type == "Year":
    answer = 2030 - year
    
print(answer)

# [PCCE 기출문제] 4번 / 저축
start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1
while 70 <= money < 100:
    money += after
    month += 1

print(month)