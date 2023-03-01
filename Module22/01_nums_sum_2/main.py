file = open('numbers.txt', 'r', encoding='utf-8')
res = 0

for line in file:
    res += int(line.strip())

file.close()

file = open('answer.txt', 'w')
file.write(str(res))
file.close()
