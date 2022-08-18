# Cronaion

Watcher

* A scheduler for your python programs.
* Easily schedule with a cronjob string.
* Very light on cpu as there are just sleeps called, not a while loop checker.
* Everything is run as a thread.
  * Note this means that you can easily use objects and non-picklable data types. However this means programs using Aion will only run on a single GIL and will be bound to a single core on a CPU. Process intensive tasks should not be used with Aion.

Located on pypi [Here](https://pypi.org/project/cronaion/)

* Install with a `pip install cronaion`

## Example Usage

```python
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
```
* Use the site [crontab.guru](https://crontab.guru/) to make your crontab strings.