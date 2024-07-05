import json
from routers.order_router import OrderRouter
from routers.payment_router import PaymentRouter
from routers.delivery_router import DeliveryRouter

DEFAULT_METHODS = dir(object)

# Main class to handle commands
class CommandHandler:
    def __init__(self):
        self.routers = {
            "order": OrderRouter(),
            "payment": PaymentRouter(),
            "delivery": DeliveryRouter(),
        }

    def handle_command(self, router_name, command, data):
        # Check if router_name exists
        if router_name in self.routers:
            router = self.routers[router_name]
            # Check if method exists in the router
            if hasattr(router, command):
                method = getattr(router, command)
                # Execute method with data
                return method(data)
            else:
                available_methods = [
                    method for method in dir(router)
                    if callable(getattr(router, method)) and method not in DEFAULT_METHODS
                ]
                return {"error": f"Method '{command}' not found in {router_name} router", "available_methods": available_methods}
        else:
            return {"error": f"Router '{router_name}' not found"}
