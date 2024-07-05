import json


# Router class for Order commands
class OrderRouter:

    def create_order(self, data):
        product = data.get("product")
        quantity = data.get("quantity")
        # Implement create order logic here
        return {"message": f"Order created for {quantity} {product}(s)"}

    def get_order(self, data):
        order_id = data.get("order_id")
        # Implement get order logic here
        return {"order_id": order_id, "status": "Delivered"}
