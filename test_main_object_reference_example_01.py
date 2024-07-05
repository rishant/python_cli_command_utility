# Import necessary modules
from app_plugin import AppPlugin


# Example class for testing
class Example:
    def __init__(self):
        self.cli_entry = AppPlugin()

    def test_order_router(self):
        print("Testing Order Router...")
        result1 = self.cli_entry.run(
            ["--router", "order", "--command", "create_order", "--json_data", '{"product": "Laptop", "quantity": 1}'])
        print(result1)

        result2 = self.cli_entry.run(
            ["--router", "order", "--command", "get_order", "--json_data", '{"order_id": "123"}'])
        print(result2)

        result3 = self.cli_entry.run(["--router", "order", "--command", "get_order"])
        print(result3)

    def test_payment_router(self):
        print("Testing Payment Router...")
        result1 = self.cli_entry.run(
            ["--router", "payment", "--command", "process_payment", "--json_data", '{"amount": 100}'])
        print(result1)

        result2 = self.cli_entry.run(["--router", "payment", "--command", "process_payment"])
        print(result2)

    def test_delivery_router(self):
        print("Testing Delivery Router...")
        result1 = self.cli_entry.run(
            ["--router", "delivery", "--command", "schedule_delivery", "--json_data", '{"address": "123 Main St"}'])
        print(result1)

        result2 = self.cli_entry.run(["--router", "delivery", "--command", "schedule_delivery"])
        print(result2)


# Main execution
if __name__ == "__main__":
    example = Example()

    # Test each router
    example.test_order_router()
    example.test_payment_router()
    example.test_delivery_router()
