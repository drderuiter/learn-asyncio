import asyncio
import logging

from learn_asyncio import configure_logging


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


async def run_coroutines(lock: asyncio.Lock, task_id: int):
    await coroutine_a(task_id)
    async with lock:
        logging.info("Task %d acquired the lock", task_id)
        await coroutine_b(task_id)
    await coroutine_c(task_id)


async def main():

    """
    Create the lock. This must be done in a coroutine - or at least, in a context
    where the event loop is known (= not at the top of the module).
    """
    lock_a_b = asyncio.Lock()

    """Note how only one task runs coroutine B at a time."""
    await asyncio.gather(*[run_coroutines(lock_a_b, task_id) for task_id in [1, 2, 3]])


configure_logging()
asyncio.run(main())
