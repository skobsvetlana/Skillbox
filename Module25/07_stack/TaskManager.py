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


