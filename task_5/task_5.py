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


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Прикрепление пути до файла
    file_path = os.path.join(script_dir, 'pcb.jpg')
    original_image = cv2.resize(cv2.imread(
        file_path, cv2.IMREAD_COLOR), (1920, 1080))
    show_image(original_image, "raw", 0)


if __name__ == "__main__":
    main()
