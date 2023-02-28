def move(n, stick2, stick3, stick1=1):
    if n == 1:
        print(f"Переложить диск {n} со стержня номер {stick1} на стержень номер {stick2}")
        return

    move(n - 1, stick3, stick2, stick1)
    print(f"Переложить диск {n} со стержня номер {stick1} на стержень номер {stick2}")
    move(n-1, stick2, stick1, stick3)


n = 2
x, y = 3, 2
move(n, x, y)


