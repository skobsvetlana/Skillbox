import os
def count_letters(my_list):
    letters_dict = {}

    for el in my_list:
        if el in letters_dict:
            letters_dict[el] += 1
        else:
            letters_dict[el] = 1

    res = sorted(letters_dict.items(),  key=lambda x: x[1])

    return  res[0][0]


path = os.path.abspath(os.path.join('..', '02_zen_of_python', "zen.txt"))
with open(path) as my_file:
    data = my_file.read().lower().split('.\n')

line_count = len(data)
word_count = sum((len(line.split()) for line in data))
words_list = (x.split() for x in data)
letters_list = [letter for letter_list in data for words in letter_list for letter in words if letter.isalpha()]
letter_count = sum([len(el) for word in words_list for el in word])
r_letter = count_letters(letters_list)

print('Количество букв в файле: {letters}\n'
      'Количество слов в файле: {words}\n'
      'Количество строк в файле: {lines}\n'
      'Наиболее редкая буква: {rarest_letter}'.format(letters=letter_count,
                                                      words=word_count,
                                                      lines=line_count,
                                                      rarest_letter= r_letter,))
