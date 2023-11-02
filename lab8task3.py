"""
Написать функцию, которая принимает путь к
изображению и выполняет над ней autocontrast,
сохраняя новое изображение по тому же пути.
"""


def task3():
    from PIL import Image, ImageOps
    print("Введите путь к изображению")
    path = str(input())
    first_image = Image.open(path)
    second_image = ImageOps.autocontrast(first_image, cutoff=20, ignore=2)
    second_image.show()

task3()
