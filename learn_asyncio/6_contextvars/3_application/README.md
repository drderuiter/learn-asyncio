# Application

Here is a nice use case for `ContextVar`s. We will use it so that each coroutine may log from which parent Task it was called.

It is a useful technique in, for example, a web service that was built on `asyncio`. As you by now can imagine, such a service is capable of dealing with multiple incoming requests at the same time. If each incoming request carries, or is assigned, a unique ID and is handled within its own Task, all the log lines can clearly state to which incoming request they belong.
