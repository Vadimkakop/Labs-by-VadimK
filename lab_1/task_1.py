numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
pos = 4
sr_arifm = (sum(numbers[0:pos]) + sum(numbers[pos + 1:]))/len(numbers)
numbers[pos] = sr_arifm
print("Измененный список:", numbers)
