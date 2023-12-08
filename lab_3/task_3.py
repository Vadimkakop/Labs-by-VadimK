def count_letters(text):
    counter_of_each_letter = dict()
    number_of_all_letters = 0
    text = text.lower()
    for symbol in text:
        if symbol.isalpha():
            number_of_all_letters += 1  # если символ - буква, то увеличиваем число букв на единицу
            if symbol in counter_of_each_letter:
                counter_of_each_letter[symbol] += 1
            else:
                counter_of_each_letter[symbol] = 1  # добавление новой буквы в словарь
    return counter_of_each_letter, number_of_all_letters


def calculate_frequency(counter_of_each_letter, number_of_all_letters):
    frequency_of_each_letter = counter_of_each_letter
    for letter_ in frequency_of_each_letter:
        frequency_of_each_letter[letter_] /= number_of_all_letters  # делим число появления буквы на общее число букв
    return frequency_of_each_letter


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

counter, number = count_letters(main_str)
frequency = calculate_frequency(counter, number)
for letter, frequency in frequency.items():  # запись в столбик
    print(f'{letter}: {frequency:.2f}')
