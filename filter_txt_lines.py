def filter_lines(input_file, keyword, output_file="filtered.txt"):
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            filtered_lines = [line for line in infile if keyword in line]
            outfile.writelines(filtered_lines)
        print(f"Фільтрація завершена. Результат записано у {output_file}")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено!")
        raise  
    except Exception as e:
        print(f"Сталася помилка: {e}")


