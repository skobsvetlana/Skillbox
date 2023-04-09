import re

phone_nums = ['9999999999', '999999-999', '99999x9999', '899999']
pattern = r'[8,9]\d{8}'

for i in range(len(phone_nums)):
    if re.match(pattern=pattern, string=phone_nums[i]):
        print(f'{i + 1}-ый номер: всё в порядке')
    else:
        print(f'{i + 1}-ый номер: не подходит')

