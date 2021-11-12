from Collection import *


def choice():
    file_r = "write.txt"
    while True:
        try:
            print("Choose what you want:\n"
                  "1 - read data from file into collection\n"
                  "2 - add new element into container and file \n"
                  "3 - print contracts \n"
                  "4 - find  popular month\n"
                  "5 - exit\n")
            what_chosen = int(input(""))
            if what_chosen == 1:
                data = Collection()
                file = Validation.input_file("Name of the file: ")
                data.read_a_file(file)
                data.write_in_file(file_r)
                print(data)
                continue
            elif what_chosen == 2:
                elem = Journey.input_product("city", "budget", "start_date", "end_date", "name")
                data.add(elem)
                data.write_in_file(file_r)
            elif what_chosen == 3:
                print(data)
            elif what_chosen == 4:
                data.popular_month()
            elif what_chosen == 5:
                break
            else:
                print("Enter right option")
                continue
        except ValueError:
            print("Something went wrong, enter an number you want:")


choice()
