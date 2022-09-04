



data = {}

for i in range(1, int(input()) + 1):
    sum_of_digits = sum(map(lambda d: int(d), str(i)))
    data[sum_of_digits] = data.get(sum_of_digits, 0) + 1
    
print(max(data.values()))
