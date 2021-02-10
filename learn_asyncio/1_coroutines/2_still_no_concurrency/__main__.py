import asyncio
import logging
from time import sleep

from learn_asyncio import configure_logging


async def blocking_coroutine():
    logging.info("Start ...")
    sleep(0.5)
    logging.info("... done!")


async def non_blocking_coroutine():
    logging.info("Start ...")
    "Control is passed to the event loop... but it has nothing else to run!"
    await asyncio.sleep(0.5)  # In a real program: await download_large_file()
    logging.info("... done!")


async def main():

    """
    These "await" lines run in order. Awaiting something suspends the execution of
    the coroutine from in which it is done - `main()`, in this case - much like a
    normal function call would.
    """
    await blocking_coroutine()
    await blocking_coroutine()
    await non_blocking_coroutine()
    await non_blocking_coroutine()


configure_logging()
asyncio.run(main())
