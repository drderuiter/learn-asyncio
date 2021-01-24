# Threading

So far, all the Tasks that we awaited (= ran) were either coroutines or `asyncio.sleep`. Those were of course placeholders for more complicated coroutines that you might write yourself, and that use actual methods from packages written to be used with `asyncio`.

What if you want to perform an IO bound task, but the library you require was not written to work with `asyncio`? A normal function cannot be awaited. Running it synchronously now feels a bit sluggish...

In this section we'll combine `asyncio` with threading in order to run non-awaitable, IO bound tasks asynchronously.
