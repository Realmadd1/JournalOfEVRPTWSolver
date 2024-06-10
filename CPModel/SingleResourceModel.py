from docplex.cp.model import CpoModel
from docplex.cp.function import *


class SingleResourceModel:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.__createVariables()
        self.__createObjection()
        self.__createConstraints()
        self.__solve()

    def __createVariables(self):
        pass

    def __createObjection(self):
        pass

    def __createConstraints(self):
        pass

    def __solve(self):
        pass
