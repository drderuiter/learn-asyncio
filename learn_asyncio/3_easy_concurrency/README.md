# Easy concurrency

So far, we have been awaiting Task objects in order to do multiple things at the same time. The function `asyncio.create_task()` is considered high-level, but it still feels a bit cumbersome. In this section we'll explore some convenience methods.
