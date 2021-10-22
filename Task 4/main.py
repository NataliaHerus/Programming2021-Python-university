from Collection_of_contracts import *
from Validation import *
from input_smth import *


def choice():
    while True:
        try:
            print("Choose what you want:\n"
                  "1 - read data from file into collection\n"
                  "2 - write data collection to another file\n"
                  "3 - delete element from collection by ID\n"
                  "4 - edit element in collection by ID\n"
                  "5 - sort contracts \n"
                  "6 - search information in contracts\n"
                  "7 - add new element into container and file \n"
                  "8 - print contracts \n"
                  "9 - exit\n")
            what_chosen = int(input(""))
            if what_chosen == 1:
                data = Collection()
                file = Validation.input_file("Name of the file: ")
                data.read_a_file(file)
                print(data)
                continue
            elif what_chosen == 2:
                file = Validation.input_file("Name of the file: ")
                data.write_in_file(file)
                print("Data was written in file ", file)
                continue
            elif what_chosen == 3:
                ID = input_id()
                data.delete(str(ID))
            elif what_chosen == 4:
                id = input_id()
                field = input_field()
                value = input_value()
                data.edit_by_id(str(id), field, value)
            elif what_chosen == 5:
                field = input_field()
                data.sort(field)
            elif what_chosen == 6:
                what = input("Enter what you want to search: ")
                data.search(what)
            elif what_chosen == 7:
                elem = Contract.input_product("ID", "contractor_name", "contractor_email", "contractor_phone",
                                              "contractor_iban", "start_date", "due_date")
                data.add(elem)
                data.add_element_to_file("Data contract.txt", elem)
            elif what_chosen == 8:
                print(data)
            elif what_chosen == 9:
                break
            else:
                print("Enter right option")
                continue
        except ValueError:
            print("Something went wrong, enter an number you want:")


choice()
