#ДПИ22-1 Быкова Ксения Дмитриевна

#Ссылка на гитхаб https://github.com/whoiskseny/1_echo_server/tree/whoiskseny-Лабораторная-Простой-эхо-сервер

import socket

def my_client():
    host = input("Введите адрес сервера: ").strip() or "localhost"
    
    while True:
        try:
            port = int(input("Введите порт сервера: "))
            if 1 <= port <= 65535:
                break
            else:
                print("Ошибка: введите корректный номер порта.")
        except ValueError:
            print("Ошибка: введите число.")
    
    print(f"Попытка подключения к серверу {host}:{port}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((host, port))
            print(f"Успешное подкключение к серверу {host}:{port}.")

            while True:
                message = input("Введите данные для отправки. Чтобы выйти введите exit: ")
                
                if message.lower() == 'exit':
                    sock.send(message.encode())
                    break
                
                sock.send(message.encode())
                print("Данные успешно отправлены.")

                data = sock.recv(1024).decode()
                print(f"Приём данных от сервера: {data}")

        except ConnectionRefusedError:
            print(f"Подключение к серверу {host}:{port} не установлено.")
        except KeyboardInterrupt:
            print("\nПринудительный разрыв подключения.")

    print("Прекращение подключения к серверу...")
    sock.close()
    print("Подключение остановлено.")

if __name__ == "__main__":
    my_client()
