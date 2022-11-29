from easyeat.configuration.Config import app
from easyeat.controller import OrderController, UserController, CartController, ProductController

# controllers init
app.register_blueprint(CartController.cart)
app.register_blueprint(OrderController.order)
app.register_blueprint(ProductController.product)
app.register_blueprint(UserController.user)
