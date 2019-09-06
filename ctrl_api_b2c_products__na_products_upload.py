from YBLEGACY import qsatype

from controllers.base.magento2.products.controllers.products_upload import ProductsUpload


class NaProductsUpload(ProductsUpload):

    product_url = "http://35.232.135.160/index.php/rest/V1/products"
    product_test_url = "http://35.232.135.160/index.php/rest/V1/products"

    link_url = "http://35.232.135.160/index.php/rest/all/V1/configurable-products/child"
    link_test_url = "http://35.232.135.160/index.php/rest/all/V1/configurable-products/child"

    def __init__(self, params=None):
        super().__init__("nab2cproducts", params)

        self.set_sync_params({
            "auth": "Bearer i2up3syhn8b4su8wbiq1dk0hftha88gn",
            "test_auth": "Bearer i2up3syhn8b4su8wbiq1dk0hftha88gn"
        })
