# Coroutines

Coroutines are one of the two types (there are more - we won't discuss them here) of objects that can be _awaited_. We'll address the other type, the Task, in the next chapter. A coroutine can be obtained by calling a coroutine function:

```python
async def my_coroutine_function():
  print("Let's create a coroutine.")
  return


my_coroutine = my_coroutine_function()
```

Note that calling a coroutine function doesn't do anything else than returning a coroutine! Running the example would not print anything. It is when we _await_ the coroutine that the code in the function finally runs. Awaiting a coroutine - or a Task - is done using the `await` keyword:

```python
await my_coroutine
print("done awaiting")
```

The `await` keyword may only be used in coroutine functions. You might wonder how we get the first coroutine running - we'll find out in the first example. While awaiting, "control is passed to the event loop". That means:

- As soon as a coroutine is awaited, the code that was written in the coroutine function starts to run;
- The `await` keyword "blocks" execution in the coroutine where it was invoked. The string "done awaiting" will indeed only be printed when the awaiting is completed, and then _only after the event loop passes back control_. Read this again and again; people who start with `asyncio` are
  often confused by the order of execution.
- While the coroutine is being awaited, the event loop can "do other things".
