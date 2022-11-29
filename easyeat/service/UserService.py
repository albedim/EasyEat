from easyeat.utils.Util import Util

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 22:48
# Version: 1.0.0
# Description: This is the class for the user service
#

class UserService():

    def __init__(self, mysql, userRepository):
        self.mysql = mysql
        self.userRepository = userRepository

    def login(self, email, password):
        user = self.userRepository.login(email, password)
        if user is not None:
            return Util.createSuccessResponse(True, user.id)
        else:
            return Util.createWrongResponse(False, Util.RESOURCE_DOESNT_EXIST, 404)

    def signin(self, name, surname, email, password, address):
        if self.userRepository.emailsCounter(email) < 1:
            self.userRepository.signin(name, surname, email, password, address)
            return Util.createSuccessResponse(True, None)
        else:
            return Util.createWrongResponse(False, Util.RESOURCE_ALREADY_EXISTS, 403)

    def getData(self, id):
        return self.userRepository.getUserObject(id).toJson()

    def changeData(self, id, name, surname, email, password, address):
        self.userRepository.changeData(id, name, surname, email, password, address)
        return Util.createSuccessResponse(True, None)