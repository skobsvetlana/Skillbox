
text = input('Введите строку: ')
ind = [i for i in range(len(text)) if text[i] == 'h']
res = text[ind[0] + 1: ind[len(ind) - 1]]

print(f'Развёрнутая последовательность между первым и последним h: {res[::-1]}')