from pathlib import Path

def get_history(user_id: str):
    file_name = Path(__file__).parent / f"logs/{user_id}.log"
    log_num = 10 # возвращаемое количество записей

    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
        data = data[-log_num - 1:-1]

        for i in range(len(data)):
            text = data[i].split()
            text = text[:2] + text[8:]
            data[i] = " ".join(text)

        return data

#print(get_history('1475535754'))


