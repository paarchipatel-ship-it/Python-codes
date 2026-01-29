t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    arr = sorted(lst)
    min_sum = arr[0] + arr[1] - lst.index(arr[0]) +  lst.index(arr[1])
    print(min_sum)