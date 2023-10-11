# TODO Найдите количество книг, которое можно разместить на дискете
numbers_of_symbols = 25
numbers_of_str = 50
numbers_of_pages = 100
size_of_symbols_in_b = 4
size_of_flop_in_mb = 1.44
size_of_flop_in_kb = size_of_flop_in_mb * 1024
size_of_flop_in_b = size_of_flop_in_kb * 1024
numbers_of_summary_symbols = numbers_of_symbols * numbers_of_str * numbers_of_pages
size_of_summary_symbols = numbers_of_summary_symbols * size_of_symbols_in_b
numbers_of_books = size_of_flop_in_b / size_of_summary_symbols
print("Количество книг, помещающихся на дискету:", round(numbers_of_books))
