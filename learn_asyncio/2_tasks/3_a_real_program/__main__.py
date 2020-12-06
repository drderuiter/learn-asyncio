import asyncio
import logging

from learn_asyncio import configure_logging


async def download_file(task_id: int, file_size: int):
    logging.info("Task %d started", task_id)
    "Alternatively, use the actual Task name by uncommenting the next line."
    # logging.info("%s started", asyncio.current_task().get_name())
    await asyncio.sleep(file_size)
    logging.info("Task %d done", task_id)
    return f"file from Task {task_id}"


async def main():
    """Download 3 large files, concurrently."""
    task_1 = asyncio.create_task(download_file(1, 3))
    task_1.set_name("my Task 1")
    task_2 = asyncio.create_task(download_file(2, 5))
    task_2.set_name("my Task 2")
    task_3 = asyncio.create_task(download_file(3, 4))
    task_3.set_name("my Task 3")

    tasks = [task_1, task_2, task_3]

    for task in tasks:
        await task
        "How much time is between the log statements, if Task 1 takes the longest? Why?"
        logging.info("Awaited %s", task.get_name())

        "For even more details, uncomment the following lines. What is Task-1?"
        # logging.info(
        #     "Still running: %s",
        #     ", ".join([task.get_name() for task in asyncio.all_tasks()]),
        # )
        # logging.info("Currently running: %s", asyncio.current_task().get_name())

    for task in tasks:
        logging.info('Result: "%s"', task.result())


configure_logging()
asyncio.run(main())
