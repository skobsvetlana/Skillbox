def get_input_parameters(word):
    return word


def display_result(is_palindrome):
    if is_palindrome:
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')


def check_palindrome(word):
   reversed_word = word[::-1]

   return word == reversed_word


if __name__ == '__main__':
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
