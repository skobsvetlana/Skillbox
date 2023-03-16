from TaskManager import TaskManager

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.new_task("поспать", 1)
print(manager)

manager.new_task("погладить кота", 1)

print(manager)

manager.delete_task("поспать", 1)
print(manager)