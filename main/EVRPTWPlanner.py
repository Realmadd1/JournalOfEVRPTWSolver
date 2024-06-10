from CPModel.AlternativeResourceModel import AlternativeResourceModel
from Input.Data import Data


class EVRPTWSolver:

    def __init__(self, path, solveNo):
        self.path = path
        self.solveNo = solveNo
        self.data = None

    def run(self):
        self.__readData()
        # 选择求解方法进行求解
        EVRPTWSolver.switch(self, self.solveNo)

    def __readData(self):
        self.data = Data()
        self.data.readData(self.path)

    """
    求解方法
    """

    def __AlternativeResourceModel(self):
        ARModel = AlternativeResourceModel(self.data)
        ARModel.run()

    def case2(self):
        print("执行操作2")

    def case3(self):
        print("执行操作3")

    def switch(self, option):
        switch_dict = {
            1: self.__AlternativeResourceModel,
            2: self.case2,
            3: self.case3,
        }
        case = switch_dict.get(option, lambda: print("求解方法设置错误"))
        case()

