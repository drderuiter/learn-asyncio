import asyncio
import logging
from time import sleep

from learn_asyncio import configure_logging


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
    logging.info("Calculating The Answer...")
    sleep(0.5)
    return 42


async def main():
    logging.info("Type of my_coroutine_function: %s", type(my_coroutine_function))
    my_coroutine = my_coroutine_function()
    logging.info("Type of my_coroutine: %s", type(my_coroutine))

    result = await my_coroutine
    assert result == await my_coroutine_function() == 42


configure_logging()
asyncio.run(main())  # The entrypoint for asyncio programs.
