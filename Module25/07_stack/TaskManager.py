from Stack import Stack
class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        string = ""
        for priority in sorted(self.task.keys()):
            string += str(priority) + " " + str(self.task[priority]) + ";\n"

        return string


    def new_task(self, task, priority):
        if priority in self.task.keys():
            self.task[priority].add(task)
        else:
            self.task[priority] = Stack()
            self.task[priority].add(task)


    def delete_task(self, task, priority):
        if not priority in self.task.keys():
            print("Задачи с таким приоритетом нет!")
        else:
            spam = Stack()

            while True:
                el = self.task[priority].pop()
                if not el:
                    print('')
                    break
                if el != task:
                    spam.add(el)
                else:
                    print(f'{el} has been removed')


            while True:
                el = spam.pop()
                if not el:
                    break
                self.task[priority].add(el)







