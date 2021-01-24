import asyncio
import logging
from time import sleep

from learn_asyncio import configure_logging


def non_awaitable_io_bound_function(task_id: int, seconds: int):
    logging.info("Task %d started", task_id)
    sleep(seconds)
    logging.info("Task %d done", task_id)
    return f"result from Task {task_id}"


async def main():

    """
    This is of course a bad idea. The functions do run, synchronously, because
    they are evaluated before `gather` is called. That function, however, expects
    awaitables - instead, it receives strings.
    """
    try:
        await asyncio.gather(
            non_awaitable_io_bound_function(1, 2),
            non_awaitable_io_bound_function(2, 4),
        )
    except TypeError as e:
        logging.error("Caught a TypeError: %s", e)

    """
    Luckily, we can cheat. Asyncio can run run a function in a thread, and await not 
    the function, but the thread as a whole. In Python, only one thread can run at a 
    time. So, this mechanism cannot be used to speed up calculations. But to complete an
    IO bound task, a thread does not need to run all the time: it only needs to check
    if the task (sleeping, in this case) is done every now and then.
    """
    await asyncio.gather(
        asyncio.to_thread(non_awaitable_io_bound_function, 3, 1),
        asyncio.to_thread(non_awaitable_io_bound_function, 4, 2),
        asyncio.to_thread(non_awaitable_io_bound_function, 5, 3),
        asyncio.to_thread(non_awaitable_io_bound_function, 6, 4),
    )


configure_logging()
asyncio.run(main())
