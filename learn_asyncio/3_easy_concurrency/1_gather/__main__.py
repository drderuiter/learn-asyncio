import asyncio
import logging

from learn_asyncio import configure_logging


class DownloadException(Exception):
    """An exception that may occur during a file download."""


async def download_file(task_id: int, file_size: int, raise_error: bool = False):
    logging.info("Task %d started", task_id)
    if raise_error:
        raise DownloadException("Download failed")
    await asyncio.sleep(file_size)
    logging.info("Task %d done", task_id)
    return f"file from Task {task_id}"


async def main():
    """Download 3 large files, concurrently, using gather."""

    "Run three coroutines without having to create Tasks explicitly. Easy!"
    for result in await asyncio.gather(
        download_file(1, 1), download_file(2, 3), download_file(3, 2)
    ):
        logging.info("Coroutine returned '%s', with type: %s, ", result, type(result))

    """
    What happens if one of the coroutines raises an exception? Let's see. We await 
    two times; the first time, we make use of the `return_exceptions` option that 
    `gather` provides.
    
    The call to `gather` returns a so-called Future. See the extensive breakdown below. 
    Once this Future is awaited, all coroutines are wrapped in a Task and awaited 
    together. Only when all Tasks are done is the awaiting of the Future done as well. 
    """
    coroutines = [download_file(4, 1), download_file(5, 3, True)]
    future = asyncio.gather(*coroutines, return_exceptions=True)
    assert isinstance(future, asyncio.Future)
    logging.info("Calling asyncio.gather() returns a %s", type(future))
    results = await future
    for result in results:
        logging.info("Coroutine returned '%s', with type: %s, ", result, type(result))

    """
    The download failed, and the exception was returned by `gather` but not raised.
    Now, let's see what happens without the `return_exceptions` argument.
    """
    try:
        for result in await asyncio.gather(
            download_file(6, 1), download_file(7, 3, True)
        ):
            logging.info(
                "Coroutine returned '%s', with type: %s, ", result, type(result)
            )
    except DownloadException as e:
        logging.warning("Caught an exception: %s", e)

    """
    It is perfectly possible to "nest" calls to `gather`. For those paying attention:
    that means that `gather` accepts not only coroutines, but also Futures.
    """
    await asyncio.gather(
        asyncio.gather(download_file(8, 1), download_file(9, 1)),
        asyncio.gather(download_file(10, 1), download_file(11, 1)),
    )


configure_logging()
asyncio.run(main())
