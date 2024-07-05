import sys
from app_plugin import AppPlugin


def main(args=None):
    app_runner = AppPlugin()
    result = app_runner.run(args)
    print(result)


if __name__ == "__main__":
    main(args=sys.argv[1:])
