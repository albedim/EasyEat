from easyeat.configuration.Config import mysql

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 21:44
# Version: 1.0.0
# Description: This is the class for the user model
#


class User(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    name = mysql.Column(mysql.String(100), nullable=False)
    surname = mysql.Column(mysql.String(100), nullable=False)
    email = mysql.Column(mysql.String(80), nullable=False)
    password = mysql.Column(mysql.String(80))
    address = mysql.Column(mysql.String(80))
    rank = mysql.Column(mysql.Text)

    def __init__(self, name, surname, email, password, address, rank):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.address = address
        self.rank = rank

    def toJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'password': self.password,
            'address': self.address,
            'rank': self.rank
        }


mysql.create_all()
