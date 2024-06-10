class Node:
    def __init__(self):
        self.id = None              # 编号
        self.x_coord = None         # x坐标
        self.y_coord = None         # y坐标
        self.demand = None          # 需求量
        self.ready_time = None      # 最早开始服务时间
        self.due_time = None        # 最迟开始服务时间
        self.service_time = None    # 服务时间
