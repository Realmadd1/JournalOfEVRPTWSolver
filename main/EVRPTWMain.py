from main.EVRPTWPlanner import EVRPTWSolver


"""求解方式设置"""
# solveMethodNo
#   1:  AlternativeResourceModel




solveMethodNo = 1





if __name__ == "__main__":
    path = "../instances/c101.txt"
    solver = EVRPTWSolver(path, solveMethodNo)
    solver.run()
