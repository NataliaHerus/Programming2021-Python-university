class Memento:

    def __init__(self, list, message):
        self._lst = list
        self._message = message

    def get_list(self):
        return self._lst

    def get_name(self):
        return self._message


class Caretaker:

    def __init__(self, list, size):
        self._mementos = []
        self._lst = list
        self._current = 0
        self._size = size

    def make_back_up(self, message):
        if len(self._mementos) == self._size:
            self._mementos.pop(0)
            self._current -= 1
        self._mementos.append(self._lst.save(message))
        self._current += 1

    def undo(self):
        if self._current < 1:
            print('UNDO cant be done now')
            return
        self._current -= 1
        memento = self._mementos[self._current - 1]
        self._lst.restore(memento)

    def redo(self):
        if self._current + 1 > len(self._mementos):
            print('REDO cant be done now')
            return
        self._current += 1
        memento = self._mementos[self._current - 1]
        self._lst.restore(memento)

    def show_history(self):
        print("Your history of operations:")
        for i, memento in enumerate(self._mementos):
            print(str(i + 1), memento.get_name())
        print("Now you are at " + str(self._current))
