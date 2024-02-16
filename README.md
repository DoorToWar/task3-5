# task3-5

# **Задание 4**

Программа считывает файл, содержащий изображение, совершает над этим изображением и его копиями определенные действия (перевод в отличные от BGR цветовые пространства, разделение на каналы, объединение каналов в одно изображение, обработка изображений низкочастотными фильтрами и высокочастотными фильтрами)

# **Технологии**

* Python

# **Использование**

Для запуска приложения необходимо загрузить все файлы из папки task3 и удостовериться, что все необходимые библиотеки установлены.

# **Разработка**

*Требования*

Для работы данной программы необходимо развернуть виртуальное окружение из файла requirements.txt
Для установки необходимо выполнить подобную команду:

```
pip install -r requirements.txt
```

Ход работы:

Было загружено оригинальное изображение
![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/b4986ea7-d62f-4393-8967-2f7c90e3f532)


Изображение было переведено в цветовое пространство RGB

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/0ef5b202-fbfa-43a8-abe6-1647a6483ec7)

Изображение было переведено в цветовое пространство XYZ

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/fb17aeb3-150a-4166-b36b-dfb5d9f7ffa2)

Изображение было переведено в цветовое пространство HSV

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/3236529b-2813-4ac6-9c50-7d5d7bcc9612)

Изображение было переведено в цветовое пространство HLS

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/1906a2b7-d97a-4c06-a852-7d135df6979e)

Изображение было переведено в цветовое пространство LAB

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/32a62c70-400d-49e9-a9af-952622991b0e)

Изображение было переведено в цветовое пространство LUV

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/e19ddcc4-8c7c-40d4-946f-70f88af2a15a)

Изображение было переведено в цветовое пространство YUV

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/04149296-08e6-4837-8212-8cf100597fd9)

Изображение было переведено в цветовое пространство CMYK

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/bd5f03c1-153a-4f56-aa82-a79c000e6cf8)

Изображение в цветовом пространстве LAB было разделено на каналы:

канал L

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/45e6e814-d79b-4e5e-ba4d-cbc39ca11704)

Канал A

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/c044bf68-d572-495e-ba56-210f2237ff3d)

Канал B

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/9fe7590c-ac47-443e-8fa8-768650bc55fb)

С помощью NumPy был обработан канал L (протестированы базовые математические операции):

Изображение до сложения:
![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/31c65e8a-5ee2-463e-8e08-8a11cec5155a)

Изображение после сложения:

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/b19915d6-eb95-4d1a-873a-a207d18b38eb)

Изображение до умножения:
![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/221e5e5d-966f-4a73-8d08-ecd930bd0bd3)

Изображение после умножения:

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/f53a9fc4-8421-459b-b1d3-ba364dfcdb13)

Изображение до вычитания:
![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/b200ff67-5d3f-4a26-b6eb-ab0f4f407d56)

Изображение после вычитания:

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/83fdbbb3-227a-4498-a0fb-7175aa74fad1)

Изображения до деления:

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/2c0e9a5d-b000-4818-9259-5712510d9ab0)

Изображения после деления:

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/94acd33b-540e-42f1-bc18-f43cb7f1aac4)

Все обработанные каналы были объединены в одно изображение:

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/c83d4942-dd56-4144-bad9-96839b8e5c08)

Были применены различные низкочастотные фильтры к изображению:

Blur:
![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/d109b815-8fae-4b46-a2e5-87daeeb7f674)

Gaussian Blur

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/e31ab359-0132-42b2-95d7-9277221ce4eb)

Median Blur

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/b0f5428e-d7e4-489d-8aa4-9fc1544014ea)

Biletteral Blur

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/1d24ea57-f08b-4f92-92ae-f37ee0fb23ad)

Были применены различные высокочастотные фильтры к изображению:

Canny

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/382a5c44-4d97-485b-bd6c-52663863c5fa)

Laplacian

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/4a05c669-4c4f-496b-ac22-07e7f5312576)

Sobel

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/75e57e48-3dff-4102-a58f-a06c675813a7)

Scharr

![изображение](https://github.com/DoorToWar/task3-5/assets/117304018/84d0ce34-0165-4a40-a2a4-e2e2326498da)
