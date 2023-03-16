class Stack:
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return str(", ".join(self.__stack))


    def add(self, el):
        self.__stack.append(el)


    def pop(self):
        if len(self.__stack) == 0:
            return None

        return self.__stack.pop()


    def get_stack(self):
        return self.__stack