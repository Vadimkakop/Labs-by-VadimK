list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_of_players = len(list_players) // 2
first_half = list_players[:middle_of_players]
second_half = list_players[middle_of_players:]
print(f'Первая команда: {first_half}\nВторая команда: {second_half}')
