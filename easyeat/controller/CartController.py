from flask import Blueprint, request
from flask_cors import cross_origin

from easyeat.configuration.Config import mysql
from easyeat.model.repository.CartRepository import CartRepository
from easyeat.service.CartService import CartService
from easyeat.utils.Util import Util

cart = Blueprint('CartController', __name__, url_prefix=Util.getURL('cart'))
cartRepository = CartRepository(mysql)
cartService = CartService(mysql, cartRepository)


@cart.route("/add", methods=['POST'])
@cross_origin()
def addToCart():
    return cartService.addToCart(
        request.json['userId'],
        request.json['productId']
    )


@cart.route("/delete", methods=['DELETE'])
@cross_origin()
def deleteFromCart():
    return cartService.deleteFromCart(
        request.args.get('userId'),
        request.args.get('productId')
    )


@cart.route("/getCost", methods=['GET'])
@cross_origin()
def cartCost():
    return cartService.getCartCost(request.args.get('id'))
