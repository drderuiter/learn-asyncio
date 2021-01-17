# Wait
This function allows for even more fine-grained control over what is happening. Often, `asyncio.as_completed` will be enough. To demonstrate why this method can still be useful, here is a very specific example.

Imagine that you are downloading a large file. There are multiple mirrors that serve the file, and some might be very slow. So, you decide to download both at the same time. As soon as one is finished, you might as well stop the other.

In the example, you'll see a function that can help you achieve this. It uses `asyncio.wait` internally. It also introduces a new concept, namely _cancelling_ a running Task. Feel free to skip - this example is somewhat advanced.
