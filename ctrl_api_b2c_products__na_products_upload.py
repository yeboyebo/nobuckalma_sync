from YBLEGACY import qsatype

from controllers.base.magento2.products.controllers.products_upload import ProductsUpload


class NaProductsUpload(ProductsUpload):

    def __init__(self, params=None):
        super().__init__("nab2corders", params)

        product_params = self.get_param_sincro('b2cProductsUpload')
        self.product_url = product_params['url']
        self.product_test_url = product_params['test_url']

        link_params = self.get_param_sincro('b2cProductsUploadLink')
        self.link_url = link_params['url']
        self.link_test_url = link_params['test_url']

        self.set_sync_params(self.get_param_sincro('b2c'))
