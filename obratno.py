# 2. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). Через рекурсию необходимо делать

# Input: 2 -> 3 4
# Output: 4 3

def reverse(n):
    if n == 0:
        return ''
    x = int(input())
    return reverse(n -1 ) + f" {x}"

n = int(input())
print(reverse(n))
