from YBLEGACY import qsatype

from controllers.base.magento2.orders.controllers.orders_download import OrdersDownload


class NaOrdersDownload(OrdersDownload):

    def __init__(self, params=None):
        super().__init__("nab2corders", params)

        order_params = self.get_param_sincro('b2cOrdersDownload')
        self.order_url = order_params['url']
        self.order_test_url = order_params['test_url']

        synchronized_params = self.get_param_sincro('b2cOrdersDownloadSync')
        self.synchronized_url = synchronized_params['url']
        self.synchronized_test_url = synchronized_params['test_url']

        self.set_sync_params(self.get_param_sincro('b2c'))
