"""
Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран виводиться в
   лівій половині - колір автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду виводиться
   поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних
    світлофорах (пішоходам зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""
import time


def traffic_light_emulator():
    car_light = ["Red", "Yellow", "Green", "Green", "Red", "Red"]
    ped_light = ["Green", "Red", "Red", "Green", "Red", "Green"]

    for car_color, ped_color in zip(car_light, ped_light):
        if car_color == "Red":
            ped_color = "Green"
        elif car_color == "Green":
            ped_color = "Red"
        elif car_color == "Yellow":
            ped_color = "Red"
        print(f"{car_color:10}{ped_color}")
        time.sleep(1)


if __name__ == "__main__":
    traffic_light_emulator()
