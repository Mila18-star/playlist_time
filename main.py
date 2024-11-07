import random
from datetime import timedelta


def get_duration(playlist: iter, n: int):
    sumTm = timedelta(minutes=0, seconds=0)       # Суммарное время песен
    length = len(playlist) - 1

    if playlist != list(playlist):  # Приводим списки к единому виду
        playlist = list(map(list, zip(*list(playlist.items()))))

    for i in range(n):
        nIter = random.randint(0, length) # Рандомное число песен
        currTm = str(playlist[1][nIter]) # Преобразуем в строку
        
        #Исправила ошибку

        if currTm[1] != ".":  # Делаем прверку на двузначность минут и секунд
            min = float(currTm[:2])
        else:
            min = float(currTm[0])
        if currTm[-2] != ".":
            sec = float(currTm[-2:])
        else:
            sec = float(currTm[-1])

        currTm = timedelta(minutes=min, seconds=sec) # Формат мин.сек
        sumTm += currTm # Ввели новую переменную

    return sumTm


playlist_d = [
    ("The Flute Tune", "Voodoo People", "Galvanize", "Miami Disco", "Komarovo", "Wild Frontier", "Check It Out", "Seasons", "These Things Will Come To Be"),
    (5.23, 5.07, 7.34, 4.31, 2.26, 4.28, 2.09, 4.25, 4.56),
]

playlist_b = {
    'Портофино': 3.32,
    'Снег': 4.35,
    'Попытка №5': 3.23,
    'Тополиный Пух': 3.53,
    'Если хочешь остаться': 4.48,
    'Зеленоглазое такси': 5.52,
    'Ты не верь слезам': 3.1,
    'Nowhere to Run': 2.58,
    'Салют, Вера': 4.41,
    'Улетаю': 3.24,
    'Опять метель': 3.37,
    }

#остаётся только сделать input для введения песен и print результата
n = int(input("Введите количество песен: "))
print(get_duration(playlist_b, n))
print(get_duration(playlist_d, n))

#Проверила, работает.