def lab5var17():
    """
    Написать функцию, которая принимает
    путь к файлу, текст и номер строки
    и записывает в файл полученный текст
    в указанный номер строки.
    """

    print("Введите полный путь к файлу", end='\n')
    base_path = input()
    print("Введите текст", end='\n')
    your_text = input()
    print("Введите номер строки", end='\n')
    num_str = int(input())

    with open(base_path, 'r+') as file:
        number = "1"
        while num_str > 1:
            file.write(number)
            file.write("\n")
            num_str = num_str - 1
            number=int(number)
            number = str(number + 1)
        file.write(number)
        file.write(" " + your_text)
    return()
lab5var17()
