import os
import pyAesCrypt #библиотека для шифровки/дешифровки

def Decryptor(file,password):
    """Функция-дешифровальщик файлов"""

    #задаём размер буфера шифрования
    buffer_size = 128 * 1024

    #дешифрование файла с помощью библиотеки pyAesCrypt
    pyAesCrypt.decryptFile(
        str(file),#исходный зашифрованный файл
        str(os.path.splitext(file)[0]),#на выходной файл берётся только имя зашифрованного файла
        password,           #пароль
        buffer_size         #буфер
    )

    #сообщение о завершении
    print(f'Файл: {os.path.splitext(file)[0]} дешифрован!')

    #удаляем исходный файл (зашифрованный)
    os.remove(file)

def walker(dir,password):
    """Сканер директорий"""

    #для каждого файла в директории,которая сканируется listdir()
    for i in os.listdir(dir):
        path = os.path.join(dir, i) #правильно формирует путь из директории к самому файлу

        #если нашли файл,то дешифруем
        if os.path.isfile(path):
            try: #создаём обработку исключений для вызова дешифровальщика
                Decryptor(path,password)
            except Exception as error: #на все обыкновенные ошибки срабатывает вывод print
                print(f'Мы наткнулись на ошибку {error}')
        else:
            walker(path,password) #если файлов не нашли,то запускаем рекурсию поиска дальше

password = input('Введите пароль: ')

#вызов функции скана директорий
walker("",password) #НЕ ЗАБУДЬТЕ НА МЕСТО "" ПОСТАВИТЬ ПУТЬ К ФАЙЛУ/ФАЙЛАМ!
