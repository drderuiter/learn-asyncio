import asyncio
import logging
from learn_asyncio import configure_logging


class DownloadException(Exception):
    """An exception that may occur during a file download."""


async def download_file(task_id: int, file_size: int):
    logging.info("Task %d started", task_id)
    await asyncio.sleep(file_size)
    logging.info("Task %d done", task_id)
    return f"file from Task {task_id}"


async def main():
    coroutines = [download_file(1, 3), download_file(2, 1)]

    """
    asyncio.as_completed will yield as soon as one of our scheduled coroutines 
    finishes. It will do so again and again, until all the passed awaitables are done. 
    Feels a bit weird that you still have to await the returned coroutine? That's 
    because the function packages them in an extra "layer".
    
    The source code of as_completed function is actually a great place to learn a bit 
    more about the inner workings of Asyncio.
    """
    for coroutine in asyncio.as_completed(coroutines):
        logging.info("Type: %s", coroutine)
        earliest_result = await coroutine
        logging.info("Coroutine returned '%s'", earliest_result)


configure_logging()
asyncio.run(main())
