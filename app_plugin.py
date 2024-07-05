import json
import argparse
from handlers.command_handler import CommandHandler


class AppPlugin:
    def __init__(self):
        self.handler = CommandHandler()
        parser = argparse.ArgumentParser(description="Command line interface for handling commands.")
        parser.add_argument("--router", type=str, required=True, choices=["order", "payment", "delivery"],
                            help="Specify router name")
        parser.add_argument("--command", type=str, required=True, help="Specify command name")
        parser.add_argument("--json_data", type=str, default='{}', help="JSON data for the command")
        self.parser = parser

    def run(self, args=None):
        if args is None:
            args = self.parser.parse_args()
        else:
            args = self.parser.parse_args(args)

        # Parse JSON data
        try:
            data = json.loads(args.json_data)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {str(e)}")
            return

        # Execute command handler
        result = self.handler.handle_command(args.router, args.command, data)
        # print(result)
        return result

