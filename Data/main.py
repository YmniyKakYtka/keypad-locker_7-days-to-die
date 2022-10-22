from random import choice
import pyautogui as pag
from keyboard import wait, write, send, is_pressed
from sys import exit
import csv

startButton = "f"
stopButton = "space"

#Point(x=825, y=547)

correctPassword = "unknownPassword"
wrongPasswords = set()

#length = len(correctPassword)

targetRow = str(pag.size()).replace("Size(width=", "").replace(",", "").replace("height=", "").replace(")", "")  #"Size(width=1920, height=1080)"
target = (targetRow.split())

with open('../passwords.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=' ')

сharsChoise = int(input("Из каких символов будет подбираться пароль? \n1 - \"0123456789\"\n2 - \"0123456789 + спецсимволы\"\n3 - \"A-Z\"\n4 - \"A-Z + 0123456789 + спецсимолы\"\n5 - \"А-Я\"\n6 - \"А-Я + 0123456789 + спецсимолы\"\n7 - \"A-B + А-Я + 0123456789 + спецсимолы\"\nВведите цифру: "))

if сharsChoise == 1:
    chars = "0123456789"

elif сharsChoise == 2:
    chars = "0123456789!@#$%^&*()_+={}[]"

elif сharsChoise == 3:
    chars = "QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"

elif сharsChoise == 4:
    chars = "0123456789!@#$%^&*()_+={}[]QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"

elif сharsChoise == 5:
    chars = "ЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮю"

elif сharsChoise == 6:
    chars = "0123456789!@#$%^&*()_+={}[]ЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮю"

elif сharsChoise == 7:
    chars = "0123456789!@#$%^&*()_+={}[]QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMmЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮю"

rangeChoise = int(input("Введите число, обозначающее сколько знаков будет в пароле: "))

print(f"Откройте окно с игрой, убрав окно консоли и нажмите {startButton} для того чтобы начать\nДля того чтобы завершить процесс преждевременно - зажмите {stopButton}")

wait(startButton)
pag.moveTo(x=int(target[0])/2, y=int(target[1])/2)

for length in range(1, 7):
    while True:
        password = ''
        for i in range(0, rangeChoise):
            password += choice(chars)
        if password not in wrongPasswords:

            with open('../passwords.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        password
                    )
                )

            pag.click()

            write(password, 0.01)
            send('enter')

            if password != correctPassword:
                wrongPasswords.add(password)
            else:
                break

        if is_pressed(stopButton):
            exit(0)

        if is_pressed('delete') == True:
            break

    print(f'{password} is correct')