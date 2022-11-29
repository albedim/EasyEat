from easyeat.model.entity.Order import Order


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 15:48
# Version: 1.0.0
# Description: This is the class for the order repository
#

class OrderRepository():

    def __init__(self, mysql):
        self.mysql = mysql

    def getOrders(self, userId):
        try:
            orders = self.mysql.session.query(Order).filter(Order.userId == userId).order_by(Order.id.desc()).all()
            return orders
        except():
            self.mysql.session.rollback()

    def addOrder(self, userId, date, cost, status):
        try:
            order = Order(userId, date, cost, status)
            self.mysql.session.add(order)
            self.mysql.session.commit()
        except():
            self.mysql.session.rollback()
