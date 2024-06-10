from Input.Node import Node
from Input.Vehicle import Vehicle


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

        self.nodes = Node.get_instances()
        # 获取第一个节点的属性
        first_node = self.nodes[0]

        # 创建虚拟节点对象，oid为101，其他属性与第一个节点相同；分别表示从仓库出发和回到仓库
        virtual_node = Node(oid=101,
                            x_coord=first_node.x_coord,
                            y_coord=first_node.y_coord,
                            demand=first_node.demand,
                            ready_time=first_node.ready_time,
                            due_time=first_node.due_time,
                            service_time=first_node.service_time
                            )
        Node.add_instance(virtual_node)

        # 更新 self.nodes，获取更新后的节点集合
        self.nodes = Node.get_instances()
