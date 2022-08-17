"""Watcher file for Aion."""

import datetime
import functools
import logging
import threading
import time
import logging
from typing import Callable, List

from cron_converter import Cron


class TaskCron:

    func_to_run = None

    cron_schedule = ""

    scheduler = None

    def __init__(
        self,
        func_to_run: Callable,
        cron_schedule: str,
        logger: logging.Logger,
        raise_except=False,
    ) -> None:
        self.func_to_run = func_to_run
        self.cron_schedule = cron_schedule

        local_date = datetime.datetime.now()

        cron_obj = Cron(self.cron_schedule)
        self.scheduler = cron_obj.schedule(start_date=local_date)

        self.logger = logger
        self.raise_except = raise_except

    def start(self):
        """"""

        while True:
            self.logger.info("Sleeping to next time scheduled")
            time.sleep(self.get_seconds_to_next_execution())
            self.logger.info("running a loop")
            self.logger.info(datetime.datetime.now())

            try:
                self.func_to_run()

            except Exception as err:
                msg = f"Could not execute {self.func_to_run.__name__}"
                if self.logger is not None:
                    self.logger.error(msg)
                    self.logger.error(err)
                else:
                    logging.error(msg)
                    logging.error(err)

                if self.raise_except:
                    raise err

    def wait_for_next(self):
        """"""
        self.logger.info("waiting for next")

    def get_seconds_to_next_execution(self) -> float:
        """"""
        next_run = self.scheduler.next()
        now = datetime.datetime.now()

        seconds_to_next = next_run - now
        seconds_to_next = seconds_to_next.total_seconds()

        self.logger.info(f"Seconds to next: {seconds_to_next}")
        return seconds_to_next


class Aion:

    tasks: List[Callable] = None

    def __init__(
        self,
        logger=None,
        *args,
        **kwargs,
    ) -> None:
        self.tasks = []

        if logger is None:
            self.logger = logging

        super().__init__(*args, **kwargs)

    def watch(self, cron, raise_except=False):
        def decorator_repeat(func):
            @functools.wraps(func)
            def wrapper_repeat(*args, **kwargs):

                func(*args, **kwargs)

            self.logger.info(f"Appended func {func.__name__} to list to run.")

            task = TaskCron(
                cron_schedule=cron,
                func_to_run=func,
                logger=self.logger,
                raise_except=raise_except,
            )
            self.tasks.append(task)

            return wrapper_repeat

        return decorator_repeat

    def start(self) -> None:
        """Starts the process."""
        threads: List[threading.Thread] = []
        for task in self.tasks:
            y = threading.Thread(target=task.start)
            y.start()
            threads.append(y)

        for thread in threads:
            thread.join()
