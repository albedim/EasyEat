from flask import jsonify

from easyeat.configuration.Config import mysql


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 21:14
# Version: 1.0.0
# Description: This is the class for the product model
#

class Product(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    image = mysql.Column(mysql.String(100), nullable=False)
    name = mysql.Column(mysql.String(80), nullable=False)
    cost = mysql.Column(mysql.Float, nullable=False)

    def __init__(self, image, name, cost):
        self.image = image
        self.name = name
        self.cost = cost

    def toJson(self):
        return {
            'id': self.id,
            'image': self.image,
            'name': self.name,
            'cost': self.cost
        }


mysql.create_all()
