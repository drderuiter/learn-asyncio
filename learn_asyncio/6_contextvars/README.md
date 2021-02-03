# contextvars

Context variables provide an alternative for global values, when using them is not feasible due to concurrency. You might think: why would I need globals? Let's consider an example.

Imagine that you built a web service using a framework that uses `asyncio`. Because your web framework is asynchronous, it can process multiple requests at the same time. (_At the same time_ meaning interwoven: accept request A, then request B, perform a next step on A, accept request C, return the response for A, et cetera) It would be nice to be able to access certain properties of the incoming request, such as the exact URL parameters, at any point in your code. Passing the these properties around to every function that you use will become cumbersome very quickly - could you use a global variable? However, when you are working on requests A, B and C, what should the value of the global variable be? Should it contain the details on request A, B or C? The `contextvars` module is here to help.

The example above was very specific, and the reason for that is that it is just a great use case. Using `asyncio` and derived packages to create a web app is beyond the scope of this tutorial, but hopefully the example is still clear enough.
