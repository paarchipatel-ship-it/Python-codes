t = int(input())
for _ in range(t):
    s = 0
    x,y = map(int, input().split())
    if x > y:
        st = y
        end = x
    else:
        st = x
        end = y
    for i in range(st+1, end):
        if i % 2 != 0:
            s += i
    print(s)