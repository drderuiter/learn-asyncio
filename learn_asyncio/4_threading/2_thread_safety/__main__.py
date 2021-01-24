import asyncio
import logging
from time import sleep
from learn_asyncio import configure_logging


class Incrementer:
    """A stupid incrementer."""

    def __init__(self):
        self.number = 0

    def increment(self, task_id):
        """A very thread-unsafe way to increment a number."""
        logging.info("Task %d started - number is now %d", task_id, self.number)
        number = self.number + 1
        sleep(0.0001)  # Sleep causes the OS to switch to another thread.
        self.number = number
        logging.info("Task %d done - updated number to %d", task_id, self.number)


async def main():

    """
    The Incrementer instance has an internal number that starts at zero. We
    increment it six times, and we do so from different threads "to speed things up".
    The expected end value of the number six.
    """
    incrementer = Incrementer()
    logging.info("Number is now: %d", incrementer.number)
    await asyncio.gather(
        *[asyncio.to_thread(incrementer.increment, task_id) for task_id in range(6)]
    )
    logging.info("Number is now: %d", incrementer.number)

    """
    What happened? The `increment` method in a certain task was reading the shared 
    resource `self.number`, incremented it, and then the OS decided that it was time 
    for another thread to run, before the updated value `number` was written to 
    `self.number`! The next thread read the old value, also incremented it - and the 
    two threads ended up writing the same value to the shared resource. Make sure to 
    have a look at the logging statements.
    
    This problem could be prevented easily, by removing the sleep that causes the OS 
    to switch threads. Or better, by locking the shared resource. It is not a problem
    that just arises for multithreading, or when using `asyncio`; it is a fundamental 
    problem that arises when a shared resource is accessed by multiple actors at the 
    same time.
    
    The take-home message: not all libraries were written with multithreading in 
    mind. It might break them, and the fix will be a lot harder than for this dummy 
    Incrementer class. When using `asyncio.to_thread`, you are multithreading.
    
    Things might break. 
    """


configure_logging()
asyncio.run(main())
