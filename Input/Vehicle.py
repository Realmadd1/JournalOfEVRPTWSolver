# 车辆类
class Vehicle:
    __instances = {}

    def __init__(self, **kwargs):
        self.oid = kwargs["oid"]                    # 车辆编号
        # self.number = kwargs["number"]            # 车辆数量
        self.capacity = kwargs["capacity"]          # 车辆容量
        self.battery = kwargs["battery"]            # 车辆电容
        self.charge = kwargs["charge"]              # 充电速率

    @classmethod
    def add_instance(cls, vehicle):
        cls.__instances[vehicle.oid] = vehicle

    @classmethod
    def get_instances(cls):
        return cls.__instances
