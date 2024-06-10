from Input.Node import Node


class Data:

    def __init__(self):
        self.vehicles = {}      # 车辆集合
        self.nodes = {}         # 节点集合

    def readData(self, path):
        # 数据读取
        file = open(path)
        file_data = file.readlines()  # 读取所有行
        # 获取车辆数据
        vehicle_inform = file_data[4].strip().split()
        vehicle_number = int(vehicle_inform[0])
        vehicle_capacity = int(vehicle_inform[1])
        # 获取节点数据
        node_list = []
        for node_no in range(9, 110):
            node = Node()
            node_inform = file_data[node_no].strip().split()  # strip()去除首位空格 split()以字符串为元素将数据存入一个列表
            node.id = int(node_inform[0])
            node.x_coord = int(node_inform[1])
            node.y_coord = int(node_inform[2])
            node.demand = int(node_inform[3])
            node.ready_time = int(node_inform[4])
            node.due_time = int(node_inform[5])
            node.service_time = int(node_inform[6])
            node_list.append(node)
