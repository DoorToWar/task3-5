import cv2
import os


def show_image(image, text, ms):
    """
    Выводит изображение.
    Использует библиотеку cv2 .
    Parametrs:
        image (ndarray): Массив с набором данных - представление каждого пикселя в формате чисел
        text (str): Название окна
    """
    cv2.imshow(text, image)  # выводит изображение
    cv2.waitKey(ms)  # ждет ввода пользователя
    # позволяет вручную менять размер окна
    cv2.namedWindow(text, cv2.WINDOW_NORMAL)
    cv2.destroyWindow(text)  # закрывает окно


def print_info(image):
    """
    Выводит информацию об изображении (разрешение и само изображение в формате данных).
    Parametrs:
        image (ndarray): Массив с набором данных - представление каждого пикселя в формате чисел
    """
    # вывод самого изображения (выводится набор данных - представление каждого пикселя в формате чисел)
    print("Изображение ", image)
    # вывод элементов shape (хранит высоту, ширину и кол-во каналов)
    print("Разрешение: ", image.shape[1], "x", image.shape[0])
    print("Количество каналов: ", len(image.shape))


def rotate(image, degree):
    """
    Поворачивает изображение.
    Parametrs:
        image (ndarray): Массив с набором данных - представление каждого пикселя в формате чисел
        degree (int): Угол, на который необходимо повернуть изображение
    """
    # получаем размер и изображения
    (h, w) = image.shape[:2]
    # находим центр
    center = (w/2, h/2)

    # создаётся матрица поворота вокруг центра
    M = cv2.getRotationMatrix2D(center, degree, 1.0)
    # применяется матрица поворота к изображению
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Прикрепление пути до файла
    file_path = os.path.join(script_dir, 'data/images', 'pcb.jpg')

    original_image = cv2.imread(file_path,
                                cv2.IMREAD_COLOR)  # IMREAD_COLOR обеспечивает вывод изображения в цвете

    # Проверка корректности загрузи изображения
    if original_image is None:
        raise Exception("Invalid")
    if original_image.shape[0] <= 0 or original_image.shape[1] <= 0:
        raise ValueError("Invalid")

    show_image(original_image, "original", 0)

    print_info(original_image)

    # изменение разрешения изображения
    resized_raw_image = cv2.resize(original_image, (1920, 1080))
    print("Разрешение: ",
          resized_raw_image.shape[1], "x", resized_raw_image.shape[0])
    show_image(resized_raw_image, "resized raw", 1000)

    copy_resized_rotate = resized_raw_image.copy()

    # поворот изображения
    rotated_45 = rotate(copy_resized_rotate, 45)
    show_image(rotated_45, "45", 0)
    rotated_90 = rotate(copy_resized_rotate, 90)
    show_image(rotated_90, "90", 0)
    rotated_180 = rotate(copy_resized_rotate, 180)
    show_image(rotated_180, "180", 0)

    copy_resized_mirror = resized_raw_image

    # отражение изображения
    flip_y = cv2.flip(copy_resized_mirror, 1)
    show_image(flip_y, "flip_y", 0)
    flip_x = cv2.flip(copy_resized_mirror, 0)
    show_image(flip_x, "flip_x", 0)

    # вырезается изображение размером 100x100
    cropped = resized_raw_image[500:600, 500:600]
    show_image(cropped, "crop", 0)

    # получаем размер и изображения
    (h, w) = cropped.shape[:2]
    # находим центр
    (cropped_y, cropped_x) = (w//2, h//2)

    print("Center = ", (cropped_y, cropped_x))

    # изменение цвета центрального пикселя

    cropped[cropped_y, cropped_x] = [0, 0, 255]
    show_image(cropped, "red", 0)

    # изменение цвета группы пикселей

    cropped[10:20, 10:20] = [255, 0, 0]
    show_image(cropped, "redes", 0)

    # выделяется прямоугольник
    cv2.rectangle(cropped, (10, 10), (20, 20), (0, 0, 0), 2)
    show_image(cropped, "redes", 0)

    # добавление текста на изображение
    cv2.putText(cropped, "rect", (10, 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    show_image(cropped, "image_fin", 0)
    if cropped is None:
        raise Exception("Invalid")
    if cropped.shape[0] <= 0 or cropped.shape[1] <= 0:
        raise ValueError("Invalid")
    # сохранение изображения
    save_path = os.path.join(script_dir, 'data/save', 'image_fin.jpg')
    cv2.imwrite(
        save_path, cropped)


if __name__ == "__main__":
    main()
