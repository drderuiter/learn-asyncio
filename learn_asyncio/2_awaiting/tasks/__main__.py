import asyncio
import logging
from time import sleep

LOGGER = logging.getLogger(__name__)


async def blocking_coroutine():
    LOGGER.info("Start ...")
    sleep(0.5)
    LOGGER.info("... done!")


async def non_blocking_coroutine():
    LOGGER.info("Start ...")
    # Control is passed to the event loop... but it has nothing else to run!
    await asyncio.sleep(0.5)
    LOGGER.info("... done!")


async def main():
    # Creating a Task also schedules it. If the task wraps a blocking coroutine,
    # the task must be finished before something else can run.
    asyncio.create_task(blocking_coroutine())
    LOGGER.info("This line runs before the first task actually starts")
    asyncio.create_task(blocking_coroutine())
    # Ignore the returned Task objects for now; we'll use them later.
    task_1 = asyncio.create_task(non_blocking_coroutine())
    task_2 = asyncio.create_task(non_blocking_coroutine())
    LOGGER.info("This line too!")

    """
    As you can see, all tasks started, but only the blocking ones finished. The
    program finished while the non-blocking coroutines were in the middle of their
    non-blocking sleep. How to make sure they finish? Try one of:
    """
    # Note: whichever we uncomment: the next line will run BEFORE any task starts!

    # await asyncio.sleep(1.6)  # Why does this only work if the argument > 1.5?
    # sleep(1.6) # This won't work: during blocking sleep, the tasks won't run.
    # await task_1; await task_2

    """
    The third solution is obviously the best: we halt main() until both tasks are 
    completed. No need to know upfront how long the longest task will take! But, 
    we only start to await task 2 after task 1 is completed.
    """


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d - line %(lineno)2s: %(funcName)30s() - %(message)s",
    datefmt="%H:%M:%S",
)

asyncio.run(main())
