import time
import random

#дольше
def findEl(mass:list) -> set:
    res = {}
    l = len(mass)
    k = 1 if len(mass)%2==1 else 0
    for i in range((len(mass)//2) + k):
        if id(mass[i]) != id(mass[l-i-1]):
            if mass[i] in res:
                res[mass[i]] += 1
            else:
                res[mass[i]] = 1
            if mass[l-i-1] in res:
                res[mass[l-i-1]] += 1
            else:
                res[mass[l-i-1]] = 1
        else:
            if mass[i] in res:
                res[mass[i]] += 1
            else:
                res[mass[i]] = 1
    s = list(res.values())
    s.sort()
    value = {i for i in res if res[i]==s[-1]}
    return value

#быстрее
def findEl2(mass:list)-> set:
    res = {}
    for i in range(len(mass)):
        res[mass[i]] = res[mass[i]] + 1 if mass[i] in res else 1
    s = list(res.values())
    s.sort()
    value = {i for i in res if res[i]==s[-1]}
    return value
    
s = [random.randint(1,100) for i in range(100000)]
start = time.time()
print(findEl(s))
end = time.time()
print('Время работы: ', end-start)

s = [random.randint(1,100) for i in range(100000)]
start = time.time()
print(findEl2(s))
end = time.time()
print('Время работы: ', end-start)