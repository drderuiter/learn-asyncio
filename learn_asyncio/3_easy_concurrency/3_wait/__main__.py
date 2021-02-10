import asyncio
import logging
from asyncio import Task
from collections.abc import Iterable
from typing import Optional

from learn_asyncio import configure_logging


async def wait_with_cancel(
    tasks: Iterable[Task], cancelling_tasks: Iterable[Task]
) -> Optional[Task]:
    """Wait for `tasks` and conditionally cancel them.

    Args:
        tasks: Tasks to wait for.
        cancelling_tasks: If any of these Tasks is done, all other pending tasks are
            cancelled. Should be a subset of `tasks`.

    Returns:
        The Task that caused cancellation, if any; else None.
    """
    # The "wait" function returns a Task when given a Task, but hints at a Future.
    done: Task
    pending: Task

    while True:
        # Wait for the first task to complete, then go on.
        done, pending = await asyncio.wait(tasks, return_when="FIRST_COMPLETED")

        # If not just one, but all tasks are done, return.
        if not pending:
            return

        # If a "cancelling_task" is done, cancel all pending tasks and return.
        for done_task in done:
            if done_task in cancelling_tasks:
                for pending_task in pending:
                    pending_task.cancel()
                await asyncio.wait(pending)  # Make sure that cancellation is done.
                return done_task

        # If the task that is done was not a "cancelling_task", await the pending tasks.
        tasks = pending


async def download_file(task_id: int, file_size: int):
    logging.info("Task %d started", task_id)
    await asyncio.sleep(file_size)
    logging.info("Task %d done", task_id)
    return f"file from Task {task_id}"


async def main():
    tasks = {
        asyncio.create_task(download_file(1, 3)),
        asyncio.create_task(download_file(2, 1)),
    }

    cancelling_task = await wait_with_cancel(tasks, tasks)
    if cancelling_task:
        logging.info(
            "Remaining tasks were cancelled, because %s completed",
            cancelling_task.get_name(),
        )
        tasks.remove(cancelling_task)
        for task in tasks:
            logging.info(
                "Was %s indeed cancelled? - %s", task.get_name(), task.cancelled()
            )

    """
    Another example. Now, only task 4 can cancel task 3, but not the other way around.
    """
    logging.info("\n\nEXAMPLE 2\n")
    task_3 = asyncio.create_task(download_file(3, 1))
    task_4 = asyncio.create_task(download_file(4, 3))

    cancelling_task = await wait_with_cancel({task_3, task_4}, {task_4})
    assert cancelling_task is None


configure_logging()
asyncio.run(main())
