from easyeat.utils import Util

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 11:38
# Version: 1.0.0
# Description: This is the class for the cart service
#


class CartService():

    def __init__(self, mysql, cartRepository):
        self.mysql = mysql
        self.cartRepository = cartRepository

    def addToCart(self, userId, productId):
        self.cartRepository.addToCart(userId, productId)
        return Util.createSuccessResponse(True, None)

    def deleteFromCart(self, userId, productId):
        self.cartRepository.deleteFromCart(userId, productId)
        return Util.createSuccessResponse(True, None)

    def getIntCartCost(self,userId):
        products = self.cartRepository.getCartProducts(userId)
        cost = 0
        for product in products:
            cost += product.cost
        return cost

    def getCartCost(self, userId):
        products = self.cartRepository.getCartProducts(userId)
        cost = 0
        for product in products:
            cost += product.cost
        return Util.createSuccessResponse(True, cost)
