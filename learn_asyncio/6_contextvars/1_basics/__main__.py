import asyncio
import logging
from learn_asyncio import configure_logging
import contextvars

dummy_var = contextvars.ContextVar("dummy", default="default-value")


async def my_coroutine(task_id: int):
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())
    dummy_var.set(f"coroutine {task_id} was here")
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())


def my_function(task_id: int) -> contextvars.Token:
    """Log the value of the `dummy_var` context var and set a value on it.

    Returns:
        A contextvars token, which can be used to undo the change.
    """
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())
    token = dummy_var.set(f"function {task_id} was here")
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())
    return token


async def main():

    """
    As you can see, the ContextVar acts as sort of a global variable. Any piece of
    code in the module can access it and write to it.
    """
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())

    dummy_var.set("some-value")
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())

    await my_coroutine(1)
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())

    dummy_var.set("some-other-value")
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())
    token = my_function(2)
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())

    """
    When changing a context variable, the `set()` method returns a token that can be 
    used to restore the original value. This has nothing to do with asyncio, but is
    pretty useful.
    """
    dummy_var.reset(token)
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())

configure_logging()
asyncio.run(main())
