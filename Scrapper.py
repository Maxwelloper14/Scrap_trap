import subprocess
import getpass

def get_wifi_networks():
    try:
        # Выполняем команду для получения информации о Wi-Fi сетях
        result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Ошибка при получении сетей: {e}")
        return None

def get_connected_devices():
    try:
        # Выполняем команду для получения списка подключенных устройств
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Ошибка при получении устройств: {e}")
        return None

def main():
    # Запрашиваем логин и пароль
    username = input("Введите логин: ")
    password = getpass.getpass("Введите пароль: ")

    # Здесь можно добавить проверку логина и пароля
    print(f"Логин: {username}, Пароль: {'*' * len(password)}")

    # Получаем информацию о ближайших сетях
    networks = get_wifi_networks()
    if networks:
        print("Ближайшие Wi-Fi сети:")
        print(networks)

    # Получаем информацию о подключенных устройствах
    devices = get_connected_devices()
    if devices:
        print("Подключенные устройства:")
        print(devices)

if __name__ == "__main__":
    main()
