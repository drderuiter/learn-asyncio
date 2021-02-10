import asyncio
import logging

from learn_asyncio import configure_logging


async def waiter(event: asyncio.Event, task_id: int):
    logging.info("Task %d started and is waiting for the event", task_id)
    await event.wait()
    logging.info("Task %d received the event", task_id)
    await asyncio.sleep(1)
    logging.info("Task %d finished", task_id)


async def main():
    event = asyncio.Event()

    """
    We must start the Tasks using `create_task`, and not by awaiting the coroutine or
    `gather`. If we did that, `main` would be blocked - and then it would be 
    impossible to set (= fire) the event. 
    """
    tasks = [asyncio.create_task(waiter(event, task_id)) for task_id in [1, 2, 3]]

    await asyncio.sleep(2)
    event.set()

    "Why is this await necessary? Have a look at section 2.2 if you forgot!"
    await asyncio.gather(*tasks)


configure_logging()
asyncio.run(main())
