from flask import Blueprint, request
from flask_cors import cross_origin

from easyeat.configuration.Config import mysql
from easyeat.model.repository.ProductRepository import ProductRepository
from easyeat.service.ProductService import ProductService
from easyeat.utils.Util import Util

product = Blueprint('ProductController', __name__, url_prefix=Util.getURL('product'))
productRepository = ProductRepository(mysql)
productService = ProductService(mysql, productRepository)


@product.route("/getProducts", methods=['GET'])
@cross_origin()
def getProducts():
    return productService.getProducts()


@product.route("/getCart", methods=['GET'])
@cross_origin()
def getCart():
    return productService.getCartProducts(request.args.get('userId'))
