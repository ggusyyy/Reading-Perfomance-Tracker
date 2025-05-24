from datetime import datetime

def get_date_input(prompt: str) -> datetime:
    while True:
        try:
            date_str = input(prompt + " (formato: DD-MM-YYYY): ")
            return datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            print("Fecha inválida. Inténtalo de nuevo.")

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt + ": "))
        except ValueError:
            print("Debes introducir sólo números.")