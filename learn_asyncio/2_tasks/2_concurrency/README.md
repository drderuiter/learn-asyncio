# Tasks - Concurrency

In this example, we'll finally see concurrency. We achieve it by creating two Tasks, which both perform an awaitable, I/O bound task. Sleeping, in this example. Note the time that it takes to run each Task. The non-blocking coroutines run at the same time!

If you uncommented the line in the previous exercise and made sure you understood what was going on, you won't find the order of the logging statements surprising.

We also find that starting a Task is no guarantee for seeing it finish. Luckily, we can await it.
