from models.flsyncppal.objects.aqmodel_raw import AQModel

from models.flfacturac.objects.order_line_raw import OrderLine


class Order(AQModel):

    def __init__(self, init_data, params=None):
        super().__init__("pedidoscli", init_data, params)

    def get_cursor(self):
        cursor = super().get_cursor()

        return cursor

    def get_children_data(self):
        for item in self.data["children"]["lines"]:
            self.children.append(OrderLine(item))

        if self.data["children"]["shippingline"]:
            self.children.append(OrderLine(self.data["children"]["shippingline"]))
