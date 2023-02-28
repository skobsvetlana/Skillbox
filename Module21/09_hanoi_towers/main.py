def hanoi_tower(n, stick1=1, stick2=3, stick3=2):
    if n == 1:
        print(f"Переложить диск {n} со стержня номер {stick1} на стержень номер {stick2}")
        return

    hanoi_tower(n - 1, stick1, stick3, stick2)
    print(f"Переложить диск {n} со стержня номер {stick1} на стержень номер {stick2}")
    hanoi_tower(n-1, stick3, stick2, stick1)


n = 5
hanoi_tower(n)


