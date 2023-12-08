def find_common_participants(first_group, second_group, separator=','):
    first_group = set(first_group.split(separator))
    second_group = second_group.split(separator)
    common_participants = list(first_group.intersection(second_group))
    common_participants.sort(reverse=True)   # без reverse сортируется НЕ по алфавиту (???)
    return common_participants


participants_first_group = "Иванов,Петров,Cидоров"
participants_second_group = "Петров,Cидоров,Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))

# при другом разделителе
participants_first_group = "Иванов|Петров|Cидоров"
participants_second_group = "Петров|Cидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))
