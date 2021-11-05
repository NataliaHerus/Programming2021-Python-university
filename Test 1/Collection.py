import json
from Class import *


class Collection:

    def __init__(self, *lst):
        self.list = [*lst]

    def __str__(self):
        string = ""
        for i in range(len(self.list)):
            string += str(self.list[i]) + "\n"
        return string

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return len(self.list)

    def __setitem__(self, key, value):
        self.list[key] = value

    def add(self, element):
        self.list.append(Journey(**element))
        Journey(**element).validate_car_reservation()

    def read_a_file(self, file):
        file_op = open(file)
        file = json.load(file_op)
        for i, element in enumerate(file):
            self.list.append(Journey(**element))
            Journey(**element).validate_car_reservation()
        file_op.close()

    def write_in_file(self, file):
        f = open(file, mode="w")
        f.writelines(str(i) + "\n" for i in self.list)
        f.close()

    def popular_month(self):
        list_of_month = []
        for item in self.list:
            list_of_month.append(item.get_start_date)
        dict = {list_of_month.count(i): i for i in list_of_month}
        list = dict.items()
        m = max(list)
        print(f"Most popular time: {m}")
        return

