import cv2
import numpy as np
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


def BGR2CMYK(image):
    """
    Преобразовние из BGR в CMYK.
    Parametrs:
        image (ndarray): Массив с набором данных - представление каждого пикселя в формате чисел

    Returns:
        fin_img (ndarray): Массив с набором данных - представление каждого пикселя в формате чисел
    """

    colours = image.astype(float)/255
    b, g, r = cv2.split(colours)  # изображение делится на каналы

    # расчет кадого параметра
    k = 1 - np.max([b, g, r], axis=0)
    c = (1 - r - k) / (1-k)
    m = (1 - g - k) / (1-k)
    y = (1 - b - k) / (1-k)
    # с помощью merge "собираем" изображение
    fin_img = cv2.merge([c, m, y, k])

    # для корректного отображения значение приводится обратно в диапозон от 0 до 255
    fin_img = (fin_img * 255).astype(np.uint8)
    return fin_img


def math_with_chanel(chanel):
    """
    Тестирование базовых математических операций над каналом.
    Parametrs:
        chanel (ndarray): Канал изображения
    """
    ch_plus = chanel + 15
    ch_minus = chanel - 15
    ch_mult = chanel * 2
    ch_div = chanel / 60
    return ch_plus, ch_mult, ch_minus, ch_div


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Прикрепление пути до файла
    file_path = os.path.join(script_dir, 'pcb.jpg')
    original_image = cv2.resize(cv2.imread(
        file_path, cv2.IMREAD_COLOR), (1920, 1080))
    show_image(original_image, "raw", 0)

    # Преобразование из BGR в RGB
    rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    show_image(rgb, "rgb", 0)

    # Преобразование из BGR в XYZ
    xyz = cv2.cvtColor(original_image, cv2.COLOR_BGR2XYZ)
    show_image(xyz, "xyz", 0)
    # Преобразование из BGR в HSV
    hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    show_image(hsv, "hsv", 0)
    # Преобразование из BGR в HLS
    hls = cv2.cvtColor(original_image, cv2.COLOR_BGR2HLS)
    show_image(hls, "hls", 0)
    # Преобразование из BGR в LAB
    lab = cv2.cvtColor(original_image, cv2.COLOR_BGR2Lab)
    show_image(lab, "lab", 0)
    # Преобразование из BGR в LUV
    luv = cv2.cvtColor(original_image, cv2.COLOR_BGR2Luv)
    show_image(luv, "luv", 0)
    # Преобразование из BGR в YUV
    yuv = cv2.cvtColor(original_image, cv2.COLOR_BGR2YUV)
    show_image(yuv, "yuv", 0)
    # Преобразование из BGR в CMYK
    cmyk = BGR2CMYK(original_image)
    show_image(cmyk, "cmyk", 0)

    # Разделение на каналы и вывод
    l, a, b = cv2.split(original_image)
    show_image(l, "l", 0)
    show_image(a, "a", 0)
    show_image(b, "b", 0)

    # Тестирование базовых математических операций над каналом
    l_plus, l_mult, l_minus, l_div = math_with_chanel(l)
    show_image(l, "chanel b4 +", 0)
    show_image(l_plus, "chanel after +", 0)
    show_image(l, "chanel b4 *", 0)
    show_image(l_mult, "chanel after *", 0)
    show_image(l, "chanel b4 -", 0)
    show_image(l_minus, "chanel after -", 0)
    show_image(l, "chanel b4 /", 0)
    show_image(l_div, "chanel after /", 0)
    l_div = l_div.astype(np.uint8)
    merged_l = cv2.merge([l_div, l_minus, l_mult, l_plus])
    show_image(merged_l, "merged image", 0)

    # Фильтр Blur

    blur = cv2.blur(original_image, (5, 5))
    show_image(blur, "blur", 0)

    # Фильтр GaussianBlur

    gaussian_blur = cv2.GaussianBlur(original_image, (5, 5), 0)
    show_image(gaussian_blur, "gaussian_blur", 0)

    # Фильтр Median Blur

    median_blur = cv2.medianBlur(original_image, 5)
    show_image(median_blur, "median blur", 0)

    # Фильтр BiletteralFilter

    biletteral_filter = cv2.bilateralFilter(original_image, 9, 75, 75)
    show_image(biletteral_filter, "biletteral filter", 0)

    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Фильтр Canny
    сanny = cv2.Canny(gray_image, 50, 150)
    show_image(сanny, "canny", 0)

    # Фильтр Laplacian
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    show_image(laplacian, "laplacian", 0)

    # Фильтр Sobel
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
    combined_sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    show_image(combined_sobel, "sobel", 0)

    # Фильтр Scharr
    scharrx = cv2.Scharr(gray_image, cv2.CV_64F, 1, 0)
    scharry = cv2.Scharr(gray_image, cv2.CV_64F, 0, 1)
    combined_scharr = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    show_image(combined_scharr, "combined_scharr", 0)


if __name__ == "__main__":
    main()
