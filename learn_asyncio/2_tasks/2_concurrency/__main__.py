import asyncio
import logging
from time import sleep

from learn_asyncio import configure_logging


async def blocking_coroutine():
    logging.info("Start ...")
    sleep(1)
    logging.info("... done!")


async def non_blocking_coroutine():
    logging.info("Start ...")
    await asyncio.sleep(1)
    logging.info("... done!")


async def main():

    """
    Creating a Task also schedules it. If the task wraps a blocking coroutine (without
    any await keywords), the task must be finished before something else can run.
    """
    asyncio.create_task(blocking_coroutine())
    logging.info("This line runs before the first task actually starts")
    asyncio.create_task(blocking_coroutine())
    "Ignore the returned Task objects for now; we'll use them later."
    task_1 = asyncio.create_task(non_blocking_coroutine())
    task_2 = asyncio.create_task(non_blocking_coroutine())
    logging.info("This line too!")

    """
    As you can see, all tasks started, but only the blocking ones finished. The
    program finished while the non-blocking coroutines were in the middle of their
    non-blocking sleep. How to make sure they finish? Try out 3 potential solutions:
    
    Note: whichever line we uncomment: it will run BEFORE any task starts.
    """

    "1. Why does this only work if the argument > 1.5?"
    # await asyncio.sleep(1.6)

    "2. This won't work: during blocking sleep, the tasks won't run."
    # sleep(1.6)

    """
    3. This is obviously the best solution: we halt main() until both tasks are 
    completed. No need to know upfront how long the longest task will take! But, 
    we only start to await task 2 after task 1 is completed, which seems random.
    """
    # await task_1
    # await task_2


configure_logging()
asyncio.run(main())
