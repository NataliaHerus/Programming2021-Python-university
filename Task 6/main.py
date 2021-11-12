from Collection_of_contracts import *
from Validation import *
from input_smth import *
from Memento import *


def choice():
    file_n = "write.txt"
    data = Collection()
    amount = input_save()
    caretaker = Caretaker(data, amount)
    caretaker.make_back_up("There are no object in collection.")
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
                  "9 - undo moment \n"
                  "10 - redo moment \n"
                  "11 - show history of moments \n"
                  "12 - exit\n")
            what_chosen = int(input(""))
            if what_chosen == 1:
                file = Validation.input_file("Name of the file: ")
                data.read_a_file(file)
                caretaker.make_back_up("Read file.")
                print(data)
                continue
            elif what_chosen == 2:
                file = Validation.input_file("Name of the file: ")
                data.write_in_file(file_n)
                print("Data was written in file ", file)
                continue
            elif what_chosen == 3:
                ID = input_id()
                data.delete(str(ID))
                caretaker.make_back_up("Delete element from collection")
                data.write_in_file(file_n)
            elif what_chosen == 4:
                id = input_id()
                field = input_field()
                value = input_value()
                data.edit_by_id(str(id), field, value)
                caretaker.make_back_up("Edit element in collection")
                data.write_in_file(file_n)
            elif what_chosen == 5:
                field = input_field()
                data.sort(field)
                caretaker.make_back_up("Sort elements")
                data.write_in_file(file_n)
            elif what_chosen == 6:
                what = input("Enter what you want to search: ")
                data.search(what)
            elif what_chosen == 7:
                elem = Contract.input_product("ID", "contractor_name", "contractor_email", "contractor_phone",
                                              "contractor_iban", "start_date", "due_date")
                data.add(elem)
                caretaker.make_back_up("Add object to collection")
                data.add_element_to_file("Data contract.txt", elem)
                data.write_in_file(file_n)
            elif what_chosen == 8:
                print(data)
            elif what_chosen == 9:
                caretaker.undo()
                data.write_in_file(file_n)
            elif what_chosen == 10:
                caretaker.redo()
                data.write_in_file(file_n)
            elif what_chosen == 11:
                caretaker.show_history()
                data.write_in_file(file_n)
            elif what_chosen == 12:
                break
            else:
                print("Enter right option")
                continue
        except ValueError:
            print("Something went wrong, enter an number you want:")


if __name__ == "__main__":
    choice()
