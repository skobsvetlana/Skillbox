import random

squad1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
squad2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [squad1[i] if squad1[i] > squad2[i] else squad2[i]
           for i in range(len(squad1))]

print(f'Первая команда: {squad1}')
print(f'Вторая команда: {squad2}')
print(f'Победители тура: {winners}')