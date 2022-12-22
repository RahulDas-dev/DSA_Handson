"""Implementation of Ordered List ."""


class OrderedList:
    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)

    @property
    def values(self):
        return self.__list

    def add(self, item):
        if len(self.__list) == 0:
            self.__list.append(item)
        else:
            max_item = self.__list[-1]
            min_item = self.__list[0]
            if item <= min_item:
                self.__list = [item] + self.__list
            elif item >= max_item:
                self.__list = self.__list + [item]
            else:
                index = 0
                for i, j in enumerate(self.__list):
                    if j >= item:
                        index = i
                        break
                self.__list = self.__list[:index] + [item] + self.__list[index:]

    def remove(self, item):
        if len(self.__list) == 0:
            return
        max_item = self.__list[-1]
        min_item = self.__list[0]
        if item == min_item:
            self.__list = self.__list[1:]
            return
        elif item == max_item:
            self.__list = self.__list[:-1]
            return
        index = 0
        for i, j in enumerate(self.__list):
            if j == item:
                index = i
                break
        self.__list = self.__list[:index] + self.__list[index + 1 :]  # noqa: E203
