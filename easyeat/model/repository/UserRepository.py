from easyeat.model.entity.User import User


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 22:44
# Version: 1.0.0
# Description: This is the class for the user repository
#

class UserRepository():

    def __init__(self, mysql):
        self.mysql = mysql

    def login(self, email, password):
        try:
            user = self.mysql.session.query(User).filter(User.email == email).filter(User.password == password).first()
            return user
        except():
            self.mysql.session.rollback()

    def signin(self, name, surname, email, password, address):
        try:
            user = User(name, surname, email, password, address, 'user')
            self.mysql.session.add(user)
            self.mysql.session.commit()
        except():
            self.mysql.session.rollback()

    def emailsCounter(self, email):
        try:
            counter = self.mysql.session.query(User).filter(User.email == email).count()
            return counter
        except():
            self.mysql.session.rollback()

    def getUserObject(self, id):
        try:
            user = self.mysql.session.query(User).filter(User.id == id).first()
            return user
        except():
            self.mysql.session.rollback()

    def changeData(self, id, name, surname, email, password, address):
        try:
            user = self.getUserObject(id)
            user.name = name
            user.surname = surname
            user.email = email
            user.password = password
            user.address = address
            self.mysql.session.commit()
        except():
            self.mysql.session.rollback()
