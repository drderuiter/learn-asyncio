import asyncio
import logging
from learn_asyncio import configure_logging
import contextvars

dummy_var = contextvars.ContextVar("dummy", default="default-value")


async def inner_inner_coroutine():
    logging.info("I was called from task %d", dummy_var.get())
    await asyncio.sleep(0.01)


async def inner_coroutine():
    logging.info("I was called from task %d", dummy_var.get())
    await asyncio.sleep(0.01)
    await inner_inner_coroutine()


async def outer_coroutine(task_id):
    logging.info("Started for Task %d", task_id)
    """As soon as the request comes in, it sets the ContextVar."""
    dummy_var.set(task_id)

    """All coroutines and Tasks will know which request is currently running."""
    await asyncio.create_task(inner_coroutine())
    await inner_coroutine()


async def main():

    """Each call to `outer_coroutine` mimics an incoming request."""
    await asyncio.gather(*[outer_coroutine(i) for i in [1, 2, 3]])


configure_logging()
asyncio.run(main())
