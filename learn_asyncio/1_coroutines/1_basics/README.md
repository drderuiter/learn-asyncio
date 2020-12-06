# Coroutines - Basics

Use this file to see for yourself how:

- a coroutine is created by calling a coroutine function;
- it an then be awaited using `await`.

Often, awaiting a coroutine is done on the same line that calls the coroutine function.

Note the usage of `asyncio.run()`, which serves as an entry point for the asynchronous program. It creates an event loop and "awaits" `main()`. Your code should have one of these entrypoints, or mayble a couple if you have a few isolated parts in your code where you use `asyncio`.
