import asyncio
import logging
from time import sleep

LOGGER = logging.getLogger(__name__)


async def my_coroutine_function() -> int:
    LOGGER.info("Calculating The Answer...")
    sleep(0.1)
    LOGGER.info("Done!")
    return 42


async def main():
    my_task = asyncio.create_task(my_coroutine_function())
    # await my_task  # Spoilers: how does uncommenting influence the execution order?
    LOGGER.info("Type of my_task: %s", type(my_task))

    """
    Note how the Task runs after this line, even though we did not use the await 
    keyword. But we did reach the end of main() - that gave the event loop the 
    opportunity to start the Task.
    """


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d - line %(lineno)2s: %(funcName)30s() - %(message)s",
    datefmt="%H:%M:%S",
)

asyncio.run(main())
