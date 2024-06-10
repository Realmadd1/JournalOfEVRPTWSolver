from Input.Node import Node
from Input.Vehicle import Vehicle


class Data:

    def __init__(self):
        self.vehicles = {}      # 车辆集合
        self.nodes = {}         # 节点集合
        self.customers = {}     # 客户节点集合
        self.depot = None       # 仓库节点

    def readData(self, path):
        # 数据读取
        file = open(path)
        file_data = file.readlines()  # 读取所有行
        # 获取车辆数据
        vehicle_inform = file_data[4].strip().split()
        # 创建车辆信息
        for vehicle_no in range(1, int(vehicle_inform[0]) + 1):
            vehicle = Vehicle(oid=vehicle_no,
                              capacity=int(vehicle_inform[1]),
                              battery=int(vehicle_inform[2]),
                              charge=int(vehicle_inform[3]))
            Vehicle.add_instance(vehicle)
        self.vehicles = Vehicle.get_instances()

        # 获取节点数据
        for node_no in range(9, 110):
            node_inform = file_data[node_no].strip().split()  # strip()去除首位空格 split()以字符串为元素将数据存入一个列表
            node = Node(oid=int(node_inform[0]),
                        x_coord=int(node_inform[1]),
                        y_coord=int(node_inform[2]),
                        demand=int(node_inform[3]),
                        ready_time=int(node_inform[4]),
                        due_time=int(node_inform[5]),
                        service_time=int(node_inform[6])
                        )
            Node.add_instance(node)
            if node_no != 9:
                self.customers[node.oid] = node
            else:
                self.depot = node

        self.nodes = Node.get_instances()


