from easyeat.configuration.Config import mysql


#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 14/10/22
# Created at: 21:34
# Version: 1.0.0
# Description: This is the class for the order model
#

class Order(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    userId = mysql.Column(mysql.Integer, nullable=False)
    date = mysql.Column(mysql.String(100), nullable=False)
    cost = mysql.Column(mysql.Float, nullable=False)
    status = mysql.Column(mysql.String(80), nullable=False)

    def __init__(self, userId, date, cost, status):
        self.userId = userId
        self.date = date
        self.cost = cost
        self.status = status

    def toJson(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'date': self.date,
            'cost': self.cost,
            'status': self.status
        }


mysql.create_all()
