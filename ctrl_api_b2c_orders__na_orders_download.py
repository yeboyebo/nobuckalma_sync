from YBLEGACY import qsatype

from controllers.base.magento2.orders.controllers.orders_download import OrdersDownload


class NaOrdersDownload(OrdersDownload):

    orders_url = "http://35.232.135.160/index.php/rest/V1/unsynchronized/orders/"
    orders_test_url = "http://35.232.135.160/index.php/rest/V1/unsynchronized/orders/"

    synchronized_url = "http://35.232.135.160/index.php/rest/default/V1/orders/{}/synchronized"
    synchronized_test_url = "http://35.232.135.160/index.php/rest/V1/orders/{}/synchronized"

    def __init__(self, params=None):
        super().__init__("nab2corders", params)

        self.set_sync_params({
            "auth": "Bearer i2up3syhn8b4su8wbiq1dk0hftha88gn",
            "test_auth": "Bearer i2up3syhn8b4su8wbiq1dk0hftha88gn"
        })
