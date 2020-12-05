# Awaitables

Awaitables are objects that can be _awaited_. Awaiting an awaitable is done using the `await` keyword:

```python
await < awaitable >
print("done awaiting")
```

The `await` keyword may only be used in coroutine functions. While awaiting, control is passed to the event loop. This has two main implications:

- While the awaitable is being awaited, the event loop can order other _tasks_ to start or continue execution. We'll address `Tasks` in a bit.
- The `await` keyword "blocks" execution in the coroutine where it was invoked. The string "done awaiting" will indeed only be printed when the awaiting is completed, and then _only after the event loop passes back control_. Read this again and again; people who start with `asyncio` are
  often confused by the order of execution.

## Awaitable types

- coroutines
- Tasks
- (Futures)

### Coroutines

Returned by calling coroutine functions:

```python
async def my_coroutine_function():
    return
```

### Tasks

If we had only coroutines and no Tasks, we could only write sequential programs, as we can without `asyncio`. Tasks make it possible to write concurrent code. Create a task:

```python
task = asyncio.create_task(my_coroutine_function())
```

Creating a task does two things:

- _schedule_ the task, meaning schedule running the coroutine that was passed: as soon as the event loop can, it will pass control to the task so that it starts running. If the creation of the task is followed by blocking code (lines that do not begin with `await`), those will be executed first.
  That is what is meant by "as soon as the event loop can";
- return a Task object, which can be used to
    1. `await` the Task: only continue in a certain coroutine until the Task is completed (meanwhile, the event loop can pass control to other Tasks); 
    2. get optional results from the Task.
  