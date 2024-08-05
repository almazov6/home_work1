def open_file():
    result = []
    for elem in range(1, 4):
        file_name = f'{elem}.txt'
        with open(file_name, encoding='utf-8') as file:
            read_lines = file.readlines()
            result.append((file_name, len(read_lines), ''.join(read_lines)))
    sorted_list = sorted(
    result,
    key=lambda i: i[1]
    )
    return sorted_list

def write_file():
    with open('result.txt', 'w', encoding='utf-8') as file:
        for elem in open_file():
            file.write(f'{elem[0]}\n')
            file.write(f'{str(elem[1])}\n')
            file.write(f'{elem[2]}\n\n')


write_file()
