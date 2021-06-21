import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl
        try:
            self.body_length = float(body_whl.split('x')[0])
            self.body_width = float(body_whl.split('x')[1])
            self.body_height = float(body_whl.split('x')[2])
        except (AttributeError, ValueError):
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(f'{csv_filename}', encoding='utf-8') as csv_fd:
        cars = []
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) 
        for row in reader:
            try:
                if row[0] == 'car':
                    machine = Car(row[1], row[3], row[5], row[2])
                elif row[0] == 'truck':
                    machine = Truck(row[1], row[3], row[5], row[4])
                elif row[0] == 'spec_machine':
                    machine = SpecMachine(row[1], row[3], row[5], row[6])
                cars.append(machine)
            except IndexError:
                del machine

    return cars


cars = get_car_list('coursera_week3_cars.csv')
print(len(cars))
for car in cars:
    print(type(car))
