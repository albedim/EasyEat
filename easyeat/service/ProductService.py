from easyeat.utils.Util import Util

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 13:44
# Version: 1.0.0
# Description: This is the class for the product service
#

class ProductService():

    def __init__(self, mysql, productRepository):
        self.mysql = mysql
        self.productRepository = productRepository

    def getProducts(self):
        return Util.createList(self.productRepository.getProducts())

    def getCartProducts(self, userId):
        return Util.createList(self.productRepository.getCartProducts(userId))
