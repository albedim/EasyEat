from easyeat.model.entity.Cart import Cart
from easyeat.model.entity.Product import Product
from sqlalchemy.sql import text


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 11:38
# Version: 1.0.0
# Description: This is the class for the cart repository
#

class CartRepository():

    def __init__(self, mysql):
        self.mysql = mysql

    def addToCart(self, userId, productId):
        try:
            cart = Cart(userId, productId)
            self.mysql.session.add(cart)
            self.mysql.session.commit()
        except():
            self.mysql.session.rollback()

    def deleteFromCart(self, userId, productId):
        try:
            cart = self.mysql.session.query(Cart).filter(Cart.userId == userId).filter(
                Cart.productId == productId).first()  # .delete()
            self.mysql.session.delete(cart)
            self.mysql.session.commit()
        except():
            self.mysql.session.rollback()
