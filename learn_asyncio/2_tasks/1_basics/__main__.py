import asyncio
import logging
from time import sleep

from learn_asyncio import configure_logging


async def my_coroutine_function() -> int:
    logging.info("Calculating The Answer...")
    sleep(0.1)
    logging.info("Done!")
    return 42


async def main():
    my_task = asyncio.create_task(my_coroutine_function())
    "Spoilers: how does uncommenting influence the execution order?"
    # await my_task
    logging.info("Type of my_task: %s", type(my_task))

    """
    Note how the Task runs after this line, even though we did not use the await 
    keyword. But we did reach the end of main() - that gave the event loop the 
    opportunity to start the Task.
    """


configure_logging()
asyncio.run(main())
