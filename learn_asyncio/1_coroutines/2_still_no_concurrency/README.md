# Coroutines - Still no concurrency

In this example we have:

- A coroutine function without an `await` keyword. It is absolutely useless. After it has started to run, it will finish entirely without ever giving control to the event loop. We might as well have used a normal function instead. (Note that there is a chance for the event loop to run something else right before the coroutine starts, when it is awaited - but this construct is still pretty useless.)
- A coroutine with an _async sleep_. This coroutine, when it runs, will wait on the sleep command for some time. The sleep command symbolizes some awaitable, I/O bound task like sending an HTTP request. While sleeping (or downloading a file), the event loop is free to do other things.

You'll quickly find that everything in the example still runs very much synchronously. Even though we an awaitable I/O bound task, we simply have nothing for the event loop to do while waiting on it.
