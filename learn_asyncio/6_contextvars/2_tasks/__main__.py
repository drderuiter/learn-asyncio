import asyncio
import logging
from learn_asyncio import configure_logging
import contextvars

dummy_var = contextvars.ContextVar("dummy", default="default-value")


async def inner_coroutine(task_id):
    logging.info(
        "Task %d: value of '%s' is now '%s'", task_id, dummy_var.name, dummy_var.get()
    )
    dummy_var.set(f"inner coroutine {task_id} was here")
    """
    (Un)comment this sleep line to convince yourself that it does not effect the 
    value of `dummy_var` at any point, especially when called through `gather`.
    """
    await asyncio.sleep(0.001)
    logging.info(
        "Task %d: value of '%s' is now '%s'", task_id, dummy_var.name, dummy_var.get()
    )


async def my_coroutine(task_id):
    logging.info(
        "Task %d: value of '%s' is now '%s'", task_id, dummy_var.name, dummy_var.get()
    )
    dummy_var.set(f"coroutine {task_id} was here")
    logging.info(
        "Task %d: value of '%s' is now '%s'", task_id, dummy_var.name, dummy_var.get()
    )

    """
    Let's nest some Tasks! Nothing new here: changes created by the Task that runs 
    the inner_coroutine are not visible for my_coroutine. The inner_coroutine WILL 
    see the value set by my_coroutine, as it receives the context as it was at the 
    moment that its Task was created. 
    """
    await asyncio.create_task(inner_coroutine(task_id))
    "This logging line will NOT print the value set by the inner coroutine."
    logging.info("Value of '%s' is now '%s'", dummy_var.name, dummy_var.get())

    "Without a Task, inner_coroutine can modify the context."
    await inner_coroutine(task_id)
    "This logging line WILL print the value set by the inner coroutine."
    logging.info("Value of '%s' is now '%s'", dummy_var.name, dummy_var.get())


async def main():

    """
    Follow the log statements precisely to see what is going on: each
    Task starts with the context as it was at the moment that the Task was created.
    If the Task makes any changes to the context, that is visible within the
    Task, but the changes remain isolated.
    """
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())

    await asyncio.create_task(my_coroutine(1))
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())

    """
    Remember: `gather` simply creates Tasks in a convenient way. We'll call the inner
    coroutine directly to avoid getting lost in the logging jungle. Note how the 
    Tasks don't see each other's values. Try to (un)comment the `sleep()` call in the
    `inner_coroutine` to see that switching from Task to Task is perfectly possible 
    without the contexts interfering.
    """
    logging.info("\n\nEXAMPLE 2 - gather\n")
    await asyncio.gather(*[inner_coroutine(i) for i in [1, 2, 3]])
    logging.info("Value of '%s' is now %s", dummy_var.name, dummy_var.get())


configure_logging()
asyncio.run(main())
