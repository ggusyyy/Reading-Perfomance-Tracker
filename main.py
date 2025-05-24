from datetime import datetime
from inputs import get_date_input, get_int_input
from calculations import calculate_stats

def main() -> None:
    test_mode = False

    if test_mode:
        print("🔬 modo test activado...\n")
        start_date = datetime.strptime("03-11-2024", "%d-%m-%Y")
        end_date = datetime.strptime("17-05-2025", "%d-%m-%Y")
        pages_read = 3006
        reading_days = 20
        total_pages = 500
    else:
        print("📚 introduce tus datos de lectura 👇\n")
        start_date = get_date_input("fecha en la que empezaste a leer el libro")
        end_date = get_date_input("fecha de hoy")
        pages_read = get_int_input("número total de páginas que has leído")
        reading_days = get_int_input("número total de días que has leído")
        total_pages = get_int_input("número total de páginas que tiene el libro")

    stats = calculate_stats(start_date, end_date, pages_read, reading_days, total_pages)

    print("\n📊 estadísticas de lectura:")
    print(f"- días que lees al mes: {stats.days_per_month:.2f} días/mes")
    print(f"- páginas al día (en total): {stats.pages_per_day_total:.2f} páginas/día")
    print(f"- páginas por día que lees: {stats.pages_per_reading_day:.2f} páginas/día que lees")

    print("\n📅 predicción de finalización:")
    print(f"- te faltan {stats.pages_remaining} páginas")
    print(f"- a este ritmo, acabarías en {stats.days_to_finish:.2f} días")
    print(f"- fecha estimada de finalización: {stats.estimated_finish_date.strftime('%d-%m-%Y')}")

if __name__ == "__main__":
    main()
