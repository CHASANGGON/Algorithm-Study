def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage += usage * change[i]/100
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1

storage = 5141
usage = 500
change = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]

print(solution(storage, usage, change))