from main.EVRPTWPlanner import EVRPTWSolver


if __name__ == "__main__":
    path = "D:\Pycharm\PyCharmProjects\JournalOfEVRPTWSolver\instances\c101.txt"
    solver = EVRPTWSolver()
    solver.run(path)
