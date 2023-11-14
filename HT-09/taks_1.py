#світлофор
import time

def traffic_light_emulator():
    car_light = ["Red", "Yellow", "Green"]
    ped_light = ["Green", "Red", "Red"]

    while True:
        for car_color, ped_color in zip(car_light, ped_light):
            print(f"{car_color:10}{ped_color}")
            time.sleep(1)

if __name__ == "__main__":
    traffic_light_emulator()
