import subprocess
import json


class Example:
    def test_order_router(self):
        print("Testing Order Router...")
        result1 = self.run_cli_command("order", "create_order", {"product": "Laptop", "quantity": 1})
        print(result1)

        result2 = self.run_cli_command("order", "get_order", {"order_id": "123"})
        print(result2)

        result3 = self.run_cli_command("order", "get_order")
        print(result3)

    def run_cli_command(self, router, command, json_data=None):
        command_list = ["python", "main.py", "--router", router, "--command", command]

        if json_data:
            json_data_str = json.dumps(json_data)
            command_list.extend(["--json_data", json_data_str])

        result = subprocess.run(command_list, capture_output=True, text=True)

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"


if __name__ == "__main__":
    example = Example()
    example.test_order_router()

