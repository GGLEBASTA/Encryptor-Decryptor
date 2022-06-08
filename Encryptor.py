import os
import pyAesCrypt #библиотека для шифровки/дешифровки

def Encryptor(file,password):
    """Функция-шифровальщик файлов"""

    #задаём размер буфера шифрования
    buffer_size = 128 * 1024

    #шифрование файла с помощью библиотеки pyAesCrypt
    pyAesCrypt.encryptFile(
        str(file), #передаём исходный файл
        str(file) + ".crp", #на выходе файл с расширением .crp
        password,           #пароль
        buffer_size         #размер буфера
    )

    #сообщение о завершении
    print(f'Файл: {os.path.splitext(file)[0]} зашифрован!') #splitext позволяет отделить имя файла от расширения

    #удаляем исходный файл (незашифрованный)
    os.remove(file)

def walker(dir,password):
    """Сканер директорий"""

    #для каждого файла в директории,которая сканируется listdir()
    for i in os.listdir(dir):
        path = os.path.join(dir, i) #правильно формирует путь из директории к самому файлу

        #если нашли файл,то шифруем
        if os.path.isfile(path):
            try: #создаём обработку исключений для вызова шифровальщика
                Encryptor(path,password)
            except Exception as error: #на все обыкновенные ошибки срабатывает вывод print
                print(f'Мы наткнулись на ошибку {error}')
        else:
            walker(path,password) #если файлов не нашли,то запускаем рекурсию поиска дальше

password = input('Пароль не должен состоять из одних букв или одних цифр: ')

#цикл проверки пароля на надёжность
while True:
    if (password.isdigit() == True) or (password.isalpha() == True): #не пропускает,где одни буквы/одни цифры
        password = input('Задайте пароль заново: ')
    else:
        break

#вызов функции скана директорий
walker("",password) #НЕ ЗАБУДЬТЕ НА МЕСТО "" ПОСТАВИТЬ ПУТЬ К ФАЙЛУ/ФАЙЛАМ!
