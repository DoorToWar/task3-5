import cv2
import os
import numpy as np


def show_image(image, text, ms):
    """

    Выводит изображение.
    Использует библиотеку cv2.

    Parametrs
    ---------
        image : numpy.ndarray
            Массив с набором данных - представление каждого пикселя в формате чисел
        text : str
            Название окна
    """
    cv2.imshow(text, image)  # выводит изображение
    cv2.waitKey(ms)  # ждет ввода пользователя
    # позволяет вручную менять размер окна
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.destroyWindow(text)  # закрывает окно


def contours_filled(filtered_contours, original_image):
    """

    Обводит и заполняет контуры изображения

    Parametrs
    ---------
    filtered_contours : list 
        Массив с отфильтрованными контурами

    original_image : numpy.ndarray
        Изначальное изображение
    Returns
    -------
    numpy.ndarray
        Изображение
    """

    image_for_contour = original_image.copy()
    for i in range(len(filtered_contours)):
        cv2.fillPoly(image_for_contour, filtered_contours, color=(255, 0, 0))
        cv2.drawContours(image_for_contour,
                         filtered_contours, -1, (255, 0, 0), 1)
    return (image_for_contour)


def contours_rect(original_image, filtered_contours):
    """
    Отрисовывает ограничивающий прямоугольник для каждого контура 

    Parametrs
    ---------
        image_rect : numpy.ndarray 
            Изначальное изображение
        filtered_contours : list
            Массив с размерами контуров
    Returns
    -------
        numpy.ndarray
            Изображение
    """
    image_for_rectangle = original_image.copy()

    for cnt in filtered_contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image_for_rectangle, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return image_for_rectangle


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Прикрепление пути до файла
    file_path = os.path.join(script_dir, 'pcb.jpg')

    original_image = cv2.imread(
        file_path, cv2.IMREAD_COLOR)

    if original_image is None:
        os.exit()
    image_resized = cv2.resize(original_image, (1920, 1080))
    show_image(image_resized, "raw", 0)

    hsv = cv2.cvtColor(image_resized, cv2.COLOR_BGR2HSV)
    show_image(hsv, "hsv", 0)

    # т.к. все выделяют контур фильтры не подходят к данной задаче

    # разделим на каналы

    # Разделение на каналы и вывод
    h, s, v = cv2.split(hsv)
    show_image(h, "h", 0)
    show_image(s, "s", 0)
    show_image(v, "v", 0)

    # Самый информативный (по визуальной оценке) - v

    # перебором подобрал, что 150 - лучшее значение для выеделения золотой подложки
    # порог для светлых пикселей

    threshold = 150

    #  маска для светлых пикселей
    mask = cv2.inRange(v, threshold, 255)

    # применил маску к изображению
    bright_parts = cv2.bitwise_and(hsv, hsv, mask=mask)

    show_image(bright_parts, "v", 0)

    # Найдите контуры на маске
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # перебор контуров
    for contour in contours:
        # просмотр площадей
        print(cv2.contourArea(contour))

    # Если фильтровать, то не вся подложка будет выделяться
    filtered_contours = [
        cnt for cnt in contours if cv2.contourArea(cnt) >= 5]

    # контуры
    image_for_contour = contours_filled(filtered_contours, image_resized)

    image_for_rectangle = contours_rect(image_resized, filtered_contours)

    show_image(image_for_rectangle, "fiiled contour",  0)

    show_image(image_for_contour, "rect contour", 0)


if __name__ == "__main__":
    main()
