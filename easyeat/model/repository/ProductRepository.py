from sqlalchemy import text

from easyeat.model.entity.Product import Product


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 11:38
# Version: 1.0.0
# Description: This is the class for the product repository
#

class ProductRepository():

    def __init__(self, mysql):
        self.mysql = mysql

    def getProducts(self):
        try:
            products = self.mysql.session.query(Product).all()
            return products
        except():
            self.mysql.session.rollback()

    def getCartProducts(self, userId):
        try:
            # cart = self.mysql.session.query(Product).join(Cart, Product.id == Cart.productId).filter(
            # Cart.userId == userId).all()
            cart = self.mysql.session.query(Product).from_statement(
                text("SELECT * FROM product JOIN cart on cart.productId = product.id WHERE cart.userId = :userId")
            ).params(userId=userId).all()
            return cart
        except():
            self.mysql.session.rollback()