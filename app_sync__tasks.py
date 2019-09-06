from AQNEXT.celery import app
from YBUTILS import globalValues

from controllers.base.default.managers.task_manager import TaskManager

from controllers.api.b2c.products.controllers.na_products_upload import NaProductsUpload as b2cProducts
from controllers.api.b2c.orders.controllers.na_orders_download import NaOrdersDownload as b2cOrders

sync_object_dict = {
    "products_upload": {
        "sync_object": b2cProducts
    },
    "orders_download": {
        "sync_object": b2cOrders
    }
}

task_manager = TaskManager(sync_object_dict)

globalValues.registrarmodulos()
cdDef = 10
