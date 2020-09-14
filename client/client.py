import socket # Библиотека для передачи данных
import cv2 # Библиотека для работы с изображениями
import pickle # Библиотека для упаковки байтов

image = cv2.imread("./python-dictionary.png") # Чтение файла с изображением

data = pickle.dumps(image) # Упаковка изображения в байты

sock = socket.socket() # Создание сокеда

sock.connect(('localhost', 9090)) # Подключение к хосту

sock.send(data) # Отправлка изображения

print(data)

sock.close() # Закрытие сокета

