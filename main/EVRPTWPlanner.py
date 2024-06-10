from Input.Data import Data


class EVRPTWSolver:
    def __init__(self):
        self.data = None

    def run(self, path):
        self.__readData(path)

    def __readData(self, path):
        self.data = Data()
        self.data.readData(path)

