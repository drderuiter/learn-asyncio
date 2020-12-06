import asyncio
import logging
from time import sleep
LOGGER = logging.getLogger(__name__)


async def my_coroutine_function() -> int:
    """Return an integer, obtained by some blocking calculations.

    Notes:
        - The actual return type is Coroutine[Any, Any, int]. When the coroutine is
          awaited, it indeed returns an integer. IDEs such as Pycharm automatically
          wrap the return type in a coroutine type, because it would get messy
          otherwise. See it for yourself by opening the documentation for this function
          changing the type hint.
        - Nothing is ever awaited in this coroutine function! We might have used a
          normal function just as well...

    Returns:
        The Answer to the Ultimate Question of Life, The Universe, and Everything.
    """
    LOGGER.info("Calculating The Answer...")
    sleep(0.5)
    return 42


async def main():
    LOGGER.info("Type of my_coroutine_function: %s", type(my_coroutine_function))
    my_coroutine = my_coroutine_function()
    LOGGER.info("Type of my_coroutine: %s", type(my_coroutine))

    result = await my_coroutine
    assert result == await my_coroutine_function() == 42


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d - line %(lineno)2s: %(funcName)30s() - %(message)s",
    datefmt="%H:%M:%S"
)

asyncio.run(main())  # The entrypoint for asyncio programs.
