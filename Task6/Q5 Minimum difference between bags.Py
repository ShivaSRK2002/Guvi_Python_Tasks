mangoes = [3, 5, 8, 10, 12, 15]
students = 3
mangoes.sort()
min_diff = float('inf')
min_index = 0
for i in range(len(mangoes) - students + 1):
    diff = mangoes[i + students - 1] - mangoes[i]
    if diff < min_diff:
        min_diff = diff
        min_index = i
print("Minimum difference between bags:", min_diff)
