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
    await asyncio.sleep(0.5)  # In a real program: await download_large_file()
    LOGGER.info("... done!")


async def main():
    # These "await" lines run in order. Awaiting passes control to the event loop,
    # but it "blocks" main() like a normal line of code would.
    await blocking_coroutine()
    await blocking_coroutine()
    await non_blocking_coroutine()
    await non_blocking_coroutine()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d - line %(lineno)2s: %(funcName)30s() - %(message)s",
    datefmt="%H:%M:%S",
)

asyncio.run(main())
