shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

tool_name = input('Название детали: ')
total_sum = 0
tool_count = 0

for tools in shop:
     if tools[0] == tool_name:
        total_sum += tools[1]
        tool_count += 1

if tool_count == 0:
        print('Данного инструмента в магазине нет')
else:
        print(f'Кол-во деталей — {tool_count}')
        print(f'Общая стоимость — {total_sum}')