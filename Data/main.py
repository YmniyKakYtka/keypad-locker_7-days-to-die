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
chars = "1234567890"

with open('../passwords.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=' ')

print(f"Откройте окно с игрой, убрав окно консоли и нажмите {startButton} для того чтобы начать\nДля того чтобы завершить процесс преждевременно - зажмите {stopButton}")

wait(startButton)

print(pag.position())

# pag.moveTo(x=825, y=547)
#
# for length in range(1, 7):
#     while True:
#         password = ''
#         for i in range(0, length):
#             password += choice(chars)
#         if password not in wrongPasswords:
#
#             with open('../passwords.csv', 'a', encoding='utf-8') as file:
#                 writer = csv.writer(file)
#                 writer.writerow(
#                     (
#                         password
#                     )
#                 )
#
#             pag.click()
#
#             write(password, 0.01)
#             send('enter')
#
#             if password != correctPassword:
#                 wrongPasswords.add(password)
#             else:
#                 break
#
#         if is_pressed(stopButton):
#             exit(0)
#
#         if is_pressed('delete') == True:
#             break
#
#     print(f'{password} is correct')