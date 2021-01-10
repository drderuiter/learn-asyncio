# learn-asyncio

Learn how to work with Python's asyncio library.

## Quick start

- Clone the repository;
- Read the README files here, or in your favorite viewer;
- Run the examples:
  ```shell
   cd <path_to>/learn-asyncio && python -m learn_asyncio.1_coroutines.1_basics
  ```
  or use your favorite IDE;
- Modify, experiment, hack, discover, learn!

## Why this tutorial

Aren't there enough already? There are a lot, but the majority focuses on learning its syntax rather than on what is actually going on. Also, this is typically a subject that should be learnt by _doing_, rather than reading a huge blog post or three.

## Why learn `asyncio`?

`Asyncio` is a library to write _concurrent_ code. Concurrent code can have multiple units run in parallel, and out-of-order, resulting in a speed improvement. As an example, consider downloading multiple large files at the same time, rather than one by one.

### Types of concurrency

Not all types of tasks that a program could perform can be parallelized with `asyncio`. For some tasks, such as heavy mathematical computations, the time it takes to complete them is determined principally by the CPU. Such a task is said to be _CPU bound_, and `asyncio` cannot be used to speed
things up. For other tasks, the CPU is not the limiting factor. When downloading a file, the CPU is mostly idle, waiting for the download to finish. Programs with a lot of such _I/O bound_ tasks can be made to run much faster using `asyncio`.

#### IO bound tasks

Consider a cook that has two pots with stew on the stove. They occasionally need stirring, but the cook is mostly waiting. Each pot needs to stew for hours, so the preparation time can mostly be ignored. The cook does not care if he works on two or three stews: it will take him about the same amount
of time.

This is a crude analogy for how `asyncio` can perform multiple tasks concurrently. Just as the cook can only stir in one pot at a time, __the CPU will only handle one task at a time__. That is fine, as for I/O bound tasks, we anticipate that we'll be waiting most of the time. Downloading five files
could like this: 1) initiate download 1 - 5 sequentially 2) wait until one is done 3) process that download and wait for the next. Note that we don't need to know which download will finish first.

`Asyncio` can be used to parallelize IO bound tasks. The library that performs the heavy lifting does have to support `asyncio` in order for this to work. There is another way, threading, that does not have this requirement. We will discuss threading in a bit.

#### CPU bound tasks

This time, the cook has to prepare sushi. Each piece requires all of his attention to perfect. Making ten sushi takes twice as long as making five. Context switching won't help him.

Similary, `asyncio` cannot be used to speed up CPU bound tasks. The problem is that, as stated before, __the CPU will always run one task at a time__. It is _waiting_ that can be parallelized, not _calculating_.

### Other means of achieving concurrency

#### Multiprocessing

Speeding up CPU bound tasks in Python is hard, because Python can use only one CPU core (Google for the _global interpreter lock_ or GIL if you want to read more). Using the `multiprocessing` library, it is possible to bypass this limitation and use more than one core, but it comes with overhead and
complexity. Often it is better to use libraries that are capable of using multiple cores because they are simply written in something else than Python. When working with larce matrices, for example, `numpy` is your super fast friend.

Let's consider the cooking analogy. `multiprocessing` allows the cook to clone himself, so he and his clones can work on more than one piece of sushi at a time. It is messy business, but it works.

#### Threading

In Python, threading can only be used to speed up I/O bound programs, since only a single thread can run at a time. The idea is to create multiple threads that each handle a task. This technique cannot be used to speed up CPU bound programs. We won't go into detail about what a thread exactly is.

To complete the analogy (it gets _really_ bad here): threads in Python are like clones of the cook, but __only one of them can move at a time__. It won't help to speed up the sushi-making process, and it seems like an overly complicated solution to make three pots of stew at the same time.

##### Threading vs `asyncio`

Which should you choose when dealing with multiple I/O bound tasks? Asyncio:

- requires libraries to be created with `asyncio` in mind;
- scales very well with the number of concurrent tasks.

Threading:

- has fewer restrictions on libraries, but they should be thread-safe;
- scales badly with the number of concurrent tasks.

There is one other major difference, which will become more clear during the tutorial. `asyncio` uses _cooperative multitasking_, while threading uses _preemptive multitasking_. With `asyncio`, the application itself decides when a context switch is made from one task to another. The programmer
writes keywords in the code, indicating that a task might take a while and that it is time to see if something else can be picked up. With threading, the operating system decides on which task to work at each time. Which way is better is up for debate, but a program written using `asyncio` surely
tells a lot about how the programmer intended concurrency to play a role in the program.

### Summary

Concurrency means having your program do multiple things at the same time. Some tasks are bound by the CPU, while others are bound by external systems. Each type of task can be parallelized, but requires a different approach:

- Use `multiprocessing` to speed up CPU bound programs, if no specialized libraries are available. Don't use it to speed up I/O bound programs, as it is overkill and comes with overhead.
- Use `asyncio` or threading to speed up I/O bound programs. Both have their use, but since this is an `asyncio` tutorial... use the former if you can.

## Chapters

1. Coroutines
2. Tasks
3. Gather
4. Wait

