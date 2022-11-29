import datetime
from flask import jsonify

from resources.rest_service import config


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 18/11/22
# Created at: 13:24
# Version: 1.0.0
# Description: This is the class for the utils
#

class Util():

    RESOURCE_DOESNT_EXIST = "The resource you are trying to get, doesn't exist"
    NOT_ENOUGH_PERMISSIONS = "You don't have enough permissions to do this"
    RESOURCE_ALREADY_EXISTS = "The resource you are trying to add, already exists"

    @classmethod
    def createList(cls, elements):
        response = []
        for element in elements:
            response.append(element.toJson())
        return jsonify(response)

    @classmethod
    def createSuccessResponse(cls, success, param):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "param": param,
            "code": 200,
        })

    @classmethod
    def createWrongResponse(cls, success, error, code):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "error": error,
            "code": code,
        })

    @classmethod
    def getURL(cls, controllerName):
        return '/api/v_' + config['version'].replace('.', '_') + '/' + controllerName
