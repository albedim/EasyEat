from flask import Blueprint, request
from flask_cors import cross_origin

from easyeat.configuration.Config import mysql
from easyeat.model.repository.UserRepository import UserRepository
from easyeat.service.UserService import UserService
from easyeat.utils.Util import Util

user = Blueprint('UserController', __name__, url_prefix=Util.getURL('user'))
userRepository = UserRepository(mysql)
userService = UserService(mysql, userRepository)


@user.route("/get", methods=['GET'])
@cross_origin()
def getUserData():
    return userService.getData(request.args.get('id'))


@user.route("/login", methods=['POST'])
@cross_origin()
def login():
    return userService.login(
        request.json['email'],
        request.json['password']
    )


@user.route("signin", methods=['POST'])
@cross_origin()
def signin():
    return userService.signin(
        request.jso['name'],
        request.json['surname'],
        request.json['email'],
        request.json['password'],
        request.json['address']
    )