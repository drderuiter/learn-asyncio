### Tasks

If we had only coroutines and no Tasks, we could only write sequential programs. We found that out the hard way in the previous chapter. The "other things" that the event loop may run while awaiting a coroutine: they're Tasks. Creating a Task is simple enough:

```python
task = asyncio.create_task(my_coroutine_function())
```

Creating a Task using `asyncio.create_task()` does two things:

- it schedules the Task to _run soon_, meaning that the coroutine that was passed will _run soon_. How soon? As soon as something else is awaited! If no `await` keyword occurs after `create_task()` was called, the event loop won't get the chance to ever start the Task. In the examples, you'll find an exception to that rule.
- it returns a Task object, which can be used to
    1. `await` the Task, which does the same as awaiting a coroutine: the coroutine in which the Task is awaited halts until the Task is done;
    2. get optional results from the Task - whatever was returned by the coroutine that the Task wraps.
    