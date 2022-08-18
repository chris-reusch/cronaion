"""Examples for Aion."""

from cronaion import Aion

watcher = Aion()

@watcher.watch("1 3 * * 0")
def restart_sonarr():
    print("I will run at 03:01 every Sunday.")

@watcher.watch("*/1 * * * *")
def restart_sonarr():
    print("I will run every 30 seconds.")


if __name__ == "__main__":
    watcher.start()
