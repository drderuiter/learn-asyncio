# As completed
So, `asyncio.gather` looks pretty great. However, what if one of the tasks finishes way earlier than the rest? Let's say you are downloading three files of different sizes - it feels like a waste not to start processing the first file while the others are still downloading. With `asyncio.gather`, you have to wait until all the passed tasks are done. You could tell so from the order of the logging statements from the previous exercise.

Luckily, `asyncio.as_completed` exists. There is also `asyncio.wait` for slightly more fine-grained control, but we won't go into that now.
