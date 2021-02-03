# Basics

In this example, we will look at the basic behavior of the `ContextVar`. Nothing here specifically requires `asyncio`, but it is good to know that the two may work together without any adjustments.

We'll see how the `ContextVar` can be used similarly to a global variable, and how any changes to it may be undone using the `Token` returned by the `set()` method.
