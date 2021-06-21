import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        if len(body_whl.split('x')) != 3:
            body_whl = 0
        self.body_whl = body_whl
        try:
            self.body_length = float(body_whl.split('x')[0])
            self.body_width = float(body_whl.split('x')[1])
            self.body_height = float(body_whl.split('x')[2])
        except (AttributeError, ValueError):
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    with open(f'{csv_filename}', encoding='utf-8') as csv_fd:
        cars = []
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                ext = os.path.splitext(row[3])[1]
                if len(row[1]) < 2 or len(row[3]) < 0 or len(row[5]) < 0:
                    continue
                elif ext != '.jpg' and ext != '.jpeg' and ext != '.png' and ext != '.gif':
                    continue
                elif row[0] == 'car' and len(row[2]) > 0:
                    machine = Car(row[1], row[3], row[5], row[2])
                elif row[0] == 'truck':
                    machine = Truck(row[1], row[3], row[5], row[4])
                elif row[0] == 'spec_machine' and len(row[6]) > 1:
                    machine = SpecMachine(row[1], row[3], row[5], row[6])
                else:
                    continue
                cars.append(machine)
            except (IndexError, ValueError):
                pass

    return cars

