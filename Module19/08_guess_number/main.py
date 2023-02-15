import random

n = int(input('Введите максимальное число: '))
hidden_num = random.randint(1, n)
ans = set([x for x in range(1, n + 1)])

while True:
    nums = input('Нужное число есть среди вот этих чисел: ')

    if nums == 'Помогите!'.lower():
        print('Артём мог загадать следующие числа: {}'.format(ans))
        break

    nums = set(map(int, nums.split()))

    if hidden_num in nums:
        print('Ответ Артёма: Да')
        ans = ans.intersection(nums)
    else:
        print('Ответ Артёма: Нет')
        ans = ans.difference(nums)




