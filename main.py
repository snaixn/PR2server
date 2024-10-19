import os
def start_server():
    os.system("python server.py")
def main():
    print("Выберите режим:")
    print("1. Запустить сервер")
    choice = input("Введите 1 что бы запустить сервер: ")
    if choice == '1':
        start_server()
    else:
        print("Неверный выбор. Попробуйте снова.")
if __name__ == "__main__":
    main()