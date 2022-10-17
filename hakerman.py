# 1.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


N = int(input())
arr = list(map(int, input().split(maxsplit=N)))

min = 1000
max = 0
for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
    if arr[i] > max:
        max = arr[i]

for i in range(len(arr)):
    if arr[i] == max:
        arr[i] = min

for i in range(len(arr)):
    print(arr[i], end=' ')