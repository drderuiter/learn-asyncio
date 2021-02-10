import asyncio
import logging
from learn_asyncio import configure_logging


class Incrementer:
    """A stupid incrementer."""

    def __init__(self):
        self.number = 0

    async def increment(self, task_id):
        """Yet another unsafe way to increment a number."""
        logging.info("Task %d started - number is now %d", task_id, self.number)
        number = self.number + 1

        "What happens when you (un)comment this line?"
        await asyncio.sleep(0.001)

        self.number = number
        logging.info("Task %d done - updated number to %d", task_id, self.number)


async def coroutine_a(task_id: int):
    logging.info("Task %d started on coroutine A", task_id)
    await asyncio.sleep(0.1)
    logging.info("Task %d performed coroutine A", task_id)


async def coroutine_b(task_id: int):
    logging.info("Task %d started on coroutine B", task_id)
    await asyncio.sleep(0.1)
    logging.info("Task %d performed coroutine B", task_id)


async def coroutine_c(task_id: int):
    logging.info("Task %d started on coroutine C", task_id)
    await asyncio.sleep(0.1)
    logging.info("Task %d performed coroutine C", task_id)


async def run_coroutines(task_id: int):
    await coroutine_a(task_id)
    await coroutine_b(task_id)
    await coroutine_c(task_id)


async def main():

    """
    We can mimic the "thread unsafe" situation from the previous section with pure
    `asyncio` code, too. Here, giving up control to the event loop is made very
    explicit by means of the `await` keyword.
    """
    incrementer = Incrementer()
    logging.info("Number is now: %d", incrementer.number)
    await asyncio.gather(*[incrementer.increment(task_id) for task_id in range(6)])
    logging.info("Number is now: %d", incrementer.number)

    """
    Let's have a look at a slightly more useful example. Imagine that we want to run 
    `run_coroutines` concurrently in four Tasks. Each Task will always complete A 
    first, then B, and finally C - each coroutine depends on the previous one (not 
    really the case here, but let's imagine).
    
    Now, consider the following constraint:
    only one Task should be running coroutine B at a time. It could be a call to a 
    slow server, that we should avoid bombarding with requests. The following code 
    clearly does not comply with that constraint.
    """
    logging.info("\n\nSECOND EXAMPLE\n")
    await asyncio.gather(*[run_coroutines(task_id) for task_id in [1, 2, 3]])


configure_logging()
asyncio.run(main())
