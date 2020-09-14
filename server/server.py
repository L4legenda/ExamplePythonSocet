import socket # Библиотека для передачи данных
import cv2 # Библиотека для работы с изображениями
import pickle # Библиотека для упаковки байтов

sock = socket.socket() # Создание сокеда

sock.bind(('', 9090)) # Создание хоста

sock.listen(1) # Количество подключений в хосту

conn, addr = sock.accept() # Получение conn = Сокет, addr = Адрес клиента

image = bytearray() # Массив для сохранения изображения

while True:
    data = conn.recv(1024) # Получения 1024 байта
    image += data # Сохранение их в image
    if not data:
        break

conn.close() # Выключене сокета

obj = pickle.loads(image) # Перевод из байтов в данные
print(obj)

cv2.imshow("Image", obj) # Вывод изображения
cv2.waitKey(0)
cv2.destroyAllWindows()

