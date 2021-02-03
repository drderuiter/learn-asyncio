# Synchronization

The title of this section is a bit abstract. We will look at two of `asyncio`'s _synchronization primitives_: the `Lock` and the `Event`. They are tools that allow the developer to control how multiple Tasks work together.

In the previous section, we saw the dangers of using a shared resource in multiple threads. When multiple concurrent entities share a single resource, there is always a potential danger. We can and will create the same situation that we saw in the last section, this time using only `asyncio`.

The `threading` module offers the `Lock`, which can be used to guarantee exclusive access to a shared resource. Since asyncio might have to deal with the same problem, it offers its own version of the `Lock`. In fact, all of `asyncio`'s synchronization primitives are based on those of the threading module.

We will also look at the `Event`, which can be used to notify multiple Tasks that something has happened.
