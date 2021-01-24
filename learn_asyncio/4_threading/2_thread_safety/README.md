# Thread safety

When working with more than a single thread, thread safety is something to consider. What is thread-safety? Thread safety has, in principle, nothing to do with `asyncio`. However, by using `asyncio.to_thread`, we are now multithreading. In a later section we'll encounter a similar problem _without_ the use of any threads.

In the example, we look at an example thread-unsafe code. The unsafe class in question is an _incrementer_: it stores an internal number, and has a single method to increment it. Of course, you won't be using `asyncio` with threading to increment a number.

What _might_ happen, however, is the following. Imagine that you have a favorite package to connect to your database. The package does not contain any awaitable methods, but now that you've seen `asyncio.to_thread`, you can't wait to bombard your database with 100 concurrent requests. However, as soon as you run your code, you get mysterious errors. Turns out, your library was never meant to be used in more that one thread.
