from Class_Contract import *
import json


class Collection:

    def __init__(self):
        self.list = []

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
        self.list.append(Contract(**element))
        Contract(**element).validate_contract()

    @Validation.check_file
    def read_a_file(self, file):
        file_op = open(file)
        file = json.load(file_op)
        for i, contract in enumerate(file):
            self.list.append(Contract(**contract))
            Contract(**contract).validate_contract()

    def delete(self, id):
        for element in self.list:
            if str(element.ID) == id:
                self.list.remove(element)
                break
        else:
            print('There are no product with such ID')

    def edit_by_id(self, id, attr, value):
        for element in self.list:
            if str(element.ID) == id:
                setattr(element, attr, value)
                break
        else:
            print('There are no product with such ID')

    @Validation.check_file
    def write_in_file(self, file):
        f = open(file, mode="w")
        f.writelines(str(i) + "\n" for i in self.list)
        f.close()

    def add_element_to_file(self, file, element):
        f = open(file, mode="a+", encoding="utf-8")
        f.writelines(str(element) + "\n")

    def sort(self, field=""):
        self.list = sorted(self.list, key=lambda product: str(getattr(product, field)).lower())

    def add_smth(self, element):
        self.list.append(element)

    def search(self, string):
        search_it = Collection()
        string_low = string.lower()
        string_up = string.capitalize()
        for i in self.list:
            for val in i.__dict__.values():
                if string_low in val or string_up in val:
                    search_it.add_smth(i)
                    break
        print("Found it!")
        print(search_it)
