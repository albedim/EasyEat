import datetime

from easyeat.utils.Util import Util


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 15:48
# Version: 1.0.0
# Description: This is the class for the order service
#

class OrderService():

    def __init__(self, mysql, orderRepository):
        self.mysql = mysql
        self.orderRepository = orderRepository

    def getOrders(self, userId):
        return Util.createList(self.orderRepository.getOrders(userId))

    def addOrder(self, userId, cost):
        self.orderRepository.addOrder(userId, str(datetime.now()), cost, 'In attesa')
        return Util.createSuccessResponse(True, None)
