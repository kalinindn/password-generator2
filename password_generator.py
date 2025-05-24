import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if length < 4:
        return "Пароль слишком короткий!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Генератор паролей")
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
        use_digits = input("Добавить цифры? (y/n, по умолчанию y): ").lower() != 'n'
        use_specials = input("Добавить спецсимволы? (y/n, по умолчанию y): ").lower() != 'n'
        password = generate_password(length, use_digits, use_specials)
        print(f"Ваш пароль: {password}")
    except ValueError:
        print("Ошибка: введите корректное число!")

if __name__ == "__main__":
    main()