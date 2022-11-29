from flask import Blueprint, request
from flask_cors import cross_origin

from easyeat.configuration.Config import mysql
from easyeat.controller.CartController import cartService
from easyeat.model.repository.OrderRepository import OrderRepository
from easyeat.service.OrderService import OrderService
from easyeat.utils.Util import Util

order = Blueprint('OrderController', __name__, url_prefix=Util.getURL('order'))
orderRepository = OrderRepository(mysql)
orderService = OrderService(mysql, orderRepository)


@order.route("/add", methods=['POST'])
@cross_origin()
def addOrder():
    return orderService.addOrder(
        request.json['userId'],
        cartService.getIntCartCost(request.json['userId'])
    )


@order.route("/get", methods=['GET'])
@cross_origin()
def getOrders():
    return orderService.getOrders(request.args.get('userId'))