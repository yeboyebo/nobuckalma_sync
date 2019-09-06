
# @class_declaration nobuckalma #
class nobuckalma(flsyncppal):

    def nobuckalma_get_customer(self):
        return "nobuckalma"

    def __init__(self, context=None):
        super().__init__(context)

    def get_customer(self):
        return self.ctx.nobuckalma_get_customer()

