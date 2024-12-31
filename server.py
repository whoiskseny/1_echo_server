# ДПИ22-1 Быкова Ксения Дмитриевна
#Ссылка на гитхаб https://github.com/whoiskseny/1_echo_server/tree/whoiskseny-Лабораторная-Простой-эхо-сервер
import socket

def my_server():
	
    host = ''

    while True:
        port = input("Введите порт для запуска сервера: ").strip()
        if port.isdigit() and 1 <= int(port) <= 65535:
            port = int(port)
            break
        else:
            print("Ошибка: введите корректный номер порта).")

    # Создаём сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            # Привязка сокета к хосту и порту
            sock.bind((host, port))
            # Прослушивание порта
            sock.listen(1)
            print(f"Сервер запуще.")
            print(f"Прослушивания порта {port}...")

            # Принимаем подключение клиента
            conn, addr = sock.accept()
            print(f"Подключение клиента {addr} к серверу.")

            while True:
                # Принимаем сообщение от клиента порционно
                data = conn.recv(1024)
                if not data:
                    break
                if data.decode().strip().lower() == "exit":
                    print(f"Отключение клиента...")
                    break
                print(f"Сервер получил данные от клиента: {data.decode()}")

                changed_data = f"{data.decode().replace(' ', '...')}..."
                conn.send(changed_data.encode())
                print("Полученные данные были видоизменены и отправлены обратно клиенту.")

            # Закрываем соединение
            print(f"Отключение клиента от сервера...")
            conn.close()
            print(f"Клиент {addr} отключён.")
		
        except KeyboardInterrupt:
            if conn:
                conn.send("Сервер был остановлен.".encode())

    print("Остановка сервера...")
    print("Сервер остановлен.")

if __name__ == "__main__":
    my_server()
