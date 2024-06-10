# class Node:
#     def __init__(self):
#         self.id = None              # 编号
#         self.x_coord = None         # x坐标
#         self.y_coord = None         # y坐标
#         self.demand = None          # 需求量
#         self.ready_time = None      # 最早开始服务时间
#         self.due_time = None        # 最迟开始服务时间
#         self.service_time = None    # 服务时间


# 节点类
class Node:
    __instances = {}

    def __init__(self, **kwargs):
        self.oid = kwargs["oid"]                    # 节点编号
        self.x_coord = kwargs["x_coord"]            # 节点x坐标
        self.y_coord = kwargs["y_coord"]            # 节点y坐标
        self.demand = kwargs["demand"]              # 需求量
        self.ready_time = kwargs["ready_time"]      # 最早开始服务时间
        self.due_time = kwargs["due_time"]          # 最迟开始服务时间
        self.service_time = kwargs["service_time"]  # 服务时间

    @classmethod
    # 加入节点
    def add_instance(cls, node):
        cls.__instances[node.oid] = node

    @classmethod
    # 获取所有节点
    def get_instances(cls):
        return cls.__instances
