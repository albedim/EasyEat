from easyeat.configuration.Config import mysql


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 11:09
# Version: 1.0.0
# Description: This is the class for the cart model
#

class Cart(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    userId = mysql.Column(mysql.Integer)
    productId = mysql.Column(mysql.Integer)

    def __init__(self, userId, productId):
        self.userId = userId
        self.productId = productId

    def toJson(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'productId': self.productId
        }


mysql.create_all()
