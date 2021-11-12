import unittest
from Collection_of_contracts import *
from Memento import *


class UnitTests(unittest.TestCase):
    Contract1 = Contract(**{"ID": "23",
                            "contractor_name": "Viktoria",
                            "contractor_email": "vikkyvik@gmail.com",
                            "contractor_phone": "0982346290",
                            "contractor_iban": "UA548201720313281001201002324",
                            "start_date": "2020-02-25",
                            "due_date": "2021-08-09"})

    Contract2 = Contract(**{"ID": "2",
                            "contractor_name": "Myron54",
                            "contractor_email": "mykymyroutlook.com",
                            "contractor_phone": "0985674321",
                            "contractor_iban": "UA9635100500000265072738706",
                            "start_date": "2022-23-12",
                            "due_date": "2021-07-01"})

    Contract3 = Contract(**{"ID": "36",
                            "contractor_name": "Artem",
                            "contractor_email": "artymko@gmail.com",
                            "contractor_phone": "0934233457",
                            "contractor_iban": "UA112222220000033333333333333",
                            "start_date": "2020-04-13",
                            "due_date": "2021-11-11"})

    def setUp(self):
        self.empty_list_test = Collection()
        self.contracts = [UnitTests.Contract1, UnitTests.Contract2, UnitTests.Contract3]
        self.list_test = Collection(*self.contracts)
        self.caretaker = Caretaker(self.list_test, 2)
        self.caretaker.make_back_up("Current collection.")

    def test_add(self):
        self.empty_list_test.add_smth(UnitTests.Contract1)
        self.empty_list_test.add_element_to_file('write.txt', self.list_test[0])
        self.assertListEqual([i for i in self.empty_list_test], [UnitTests.Contract1])

        self.empty_list_test.add_smth(UnitTests.Contract2)
        self.assertListEqual([i for i in self.empty_list_test], [UnitTests.Contract1, UnitTests.Contract2])

        self.empty_list_test.add_smth(UnitTests.Contract3)
        self.assertNotEqual([i for i in self.empty_list_test], [UnitTests.Contract1, UnitTests.Contract2])
        self.assertEqual(self.empty_list_test.__len__(), 3)

    def test_sort(self):
        obj = [name for name in dir(UnitTests.Contract3)]
        for field in obj:
            self.contracts = sorted(self.contracts, key=lambda product: str(getattr(product, field)).lower())
            self.list_test.sort(field)
            self.assertListEqual([el for el in self.list_test], self.contracts)
            self.assertRaises(AttributeError, self.list_test.sort)

    def test_edit(self):
        edit_1 = ("23", "contractor_name", "Oleksandr")
        edit_2 = ("2", "contractor_phone", "0967892312")
        edit_3 = ("4", "contractor_phone", "0967892312")
        self.list_test.edit_by_id(*edit_3)
        self.assertEqual(self.list_test.edit_by_id(*edit_3), None)
        self.list_test.edit_by_id(*edit_1)
        self.assertEqual(getattr(UnitTests.Contract1, edit_1[1]), edit_1[2])
        self.list_test.edit_by_id(*edit_2)
        self.assertEqual(getattr(UnitTests.Contract2, edit_2[1]), edit_2[2])

    def test_delete(self):
        id1, id2, id3 = "23", "2", "36"
        self.list_test.delete(id1)
        self.assertListEqual([el for el in self.list_test], [UnitTests.Contract2, UnitTests.Contract3])

        self.list_test.delete(id2)
        self.assertListEqual([el for el in self.list_test], [UnitTests.Contract3])

        self.list_test.delete(id3)
        self.assertNotEqual([el for el in self.list_test], [UnitTests.Contract3])

        self.assertEqual(self.list_test.delete("212"), None)

    def test_search(self):
        found_tst_1 = self.list_test.search("Ar")
        found_tst_2 = self.list_test.search("gmail")
        found_tst_3 = self.list_test.search('ash')

        self.assertListEqual(found_tst_1, [UnitTests.Contract3])
        self.assertListEqual(found_tst_2, [UnitTests.Contract1, UnitTests.Contract3])
        self.assertNotEqual(found_tst_3, UnitTests.Contract2)

    def test_undo(self):
        self.list_test.sort('contractor_name')
        self.caretaker.make_back_up("Sort elements")
        self.caretaker.undo()
        self.assertListEqual([str(i) for i in self.list_test], [str(i) for i in self.contracts])

    def test_redo(self):
        self.list_test.add_smth(self.list_test[0])
        self.contracts.append(self.list_test[0])
        self.caretaker.make_back_up("Add new element")
        self.caretaker.undo()
        self.caretaker.redo()
        self.assertListEqual([str(el) for el in self.list_test], [str(el) for el in self.contracts])

    def test_read_a_file(self):
        self.empty_list_test.read_a_file('Data contract.txt')
        self.empty_list_test.write_in_file('write.txt')
        self.assertEqual(len(self.empty_list_test), 3)

    def test_valid(self):
        self.assertEqual(self.contracts[1].validate_contract(), None)


if __name__ == '__main__':
    unittest.main()
