from YBLEGACY import qsatype

from controllers.base.magento2.orders.controllers.orders_download import OrdersDownload


class NaOrdersDownload(OrdersDownload):

    orders_url = "https://tintopro.com/index.php/rest/V1/unsynchronized/orders/"
    orders_test_url = "https://tintopro.com/index.php/rest/V1/unsynchronized/orders/"

    synchronized_url = "https://tintopro.com/index.php/rest/default/V1/orders/{}/synchronized"
    synchronized_test_url = "https://tintopro.com/index.php/rest/V1/orders/{}/synchronized"

    def __init__(self, params=None):
        super().__init__("nab2corders", params)

        self.set_sync_params({
            "auth": "Bearer 4gt9sndpj981jgv7v1bx5i0h1yo8wjq8",
            "test_auth": "Bearer 4gt9sndpj981jgv7v1bx5i0h1yo8wjq8"
        })
