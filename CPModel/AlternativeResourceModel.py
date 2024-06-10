from docplex.cp.model import CpoModel
from docplex.cp.function import *


class AlternativeResourceModel:
    def __init__(self, data):
        self.data = data
        self.model = CpoModel("AlternativeResourceModel")
        """参数"""
        self.resourceWise = []  # 资源区间, 时间窗
        """决策变量"""
        self.xm = {}            # 强制区间变量, xm[i], 客户i的服务
        self.xo = {}            # 可选区间变量, xo[i,k], 客户i与车辆k的关联
        self.pai = {}           # 序列变量, pai[k], 与车辆k相关的变量集合, 表示车辆访问顺序
        self.C = {}             # 累积资源函数, C[k], 与车量k有关的负载累积资源函数
        self.Q = {}             # 累积资源函数, Q[k], 与车辆k有关的电量累积资源函数

    def run(self):
        self.__createParameters()
        self.__createVariables()
        self.__createObjection()
        self.__createConstraints()
        self.__solve()

    def __createParameters(self):
        for t in range(self.data.depot.ready_time, self.data.depot.due_time + 1):
            self.resourceWise.append(t)

    def __createVariables(self):
        for i, cus in self.data.customers.items():
            self.xm[i] = self.model.interval_var(
                start=[self.resourceWise[0], self.resourceWise[-1]],
                end=[self.resourceWise[0], self.resourceWise[-1]],
                size=cus.service_time, optional=False, name='x_{}'.format(i)
                )





        # self.pai = self.model.sequence_var(size=5, types=[1, 2, 3, 4, 5])

    def __createObjection(self):
        pass

    def __createConstraints(self):
        pass

    def __solve(self):
        pass
