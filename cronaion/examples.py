"""Examples for Aion."""

from cronaion import Aion

watcher = Aion()


@watcher.watch("1 3 * * 0")
def check_the_mail():
    print("I will run at 03:01 every Sunday.")


@watcher.watch("*/1 * * * *")
def blink_my_eyes():
    print("I will run every 60 seconds.")


if __name__ == "__main__":
    watcher.start()
