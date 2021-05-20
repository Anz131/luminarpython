# ducktyping
# more prior to functionalities more than class

class Swift:
    def start(self):
        print("Swift car starts")
    def accelerate(self):
        print("Swift car accelerates")
    def breaks(self):
        print("Swift car breaks")
    def stop(self):
        print("Swift car stops")

class Seltos:
    def start(self):
        print("Seltos car starts")
    def accelerate(self):
        print("Seltos car accelerates")
    def breaks(self):
        print("Seltos car breaks")
    def stop(self):
        print("Seltos car stops")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()
p=Person()
sw=Swift()
p.drive(sw)

# class Pycharm:
#     def compile(self):
#         print("Compile using pycharm")
#     def execute(self):
#         print("Execute using pycharm")

#
# class Vscode:
#     def compile(self):
#         print("Compile using vscode")
#     def execute(self):
#         print("Execute using vscode")
#
# class Programmer:
#     def coding(self,ide):
#         ide.compile()
#         ide.execute()
#
# p=Programmer()
# py=Pycharm()
# p.coding(py)
