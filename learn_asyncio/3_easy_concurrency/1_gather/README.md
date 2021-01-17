# Gather
`asyncio.gather` will likely become your favorite `asyncio` function. It is extremely simple to use. Just pass one or more _awaitables_ and await the returned Future. Lots of new terminology here.

An _awaitable_ is an object that can be used in an `await` expressions. Some tutorials start by giving these definitions right away, but for a beginner, they don't mean to much. There are three kind of awaitables, two of which you are familiar with already: **coroutines**, **Tasks** and **Futures**.

Futures are low-level objects, and an `asyncio` user typically won't have to deal with them explicitly. Think of them as a somewhat more raw form of Tasks.
