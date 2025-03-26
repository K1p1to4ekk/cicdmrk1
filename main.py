from filter_txt_lines import filter_lines

if __name__ == "__main__":
    input_filename = input("Введіть ім'я файлу: ")
    keyword_to_search = input("Введіть ключове слово: ")
    filter_lines(input_filename, keyword_to_search)