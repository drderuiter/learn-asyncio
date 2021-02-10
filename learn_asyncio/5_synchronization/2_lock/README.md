# Lock

To deal with the problem from the previous subsection, we'll finally use a `Lock`. Conceptually, it is very simple: only one Task may acquire it at a time. Other Tasks will simply wait until it is their turn.

The incrementer in the previous was incredibly poorly designed. It would be easy to make the incrementing operation atomic; in fact, you could do so by commenting a single line in the example.

Still, it can be useful to guarantee exclusive access, and there might be other situations where it is desirable that tasks do not interfere with each other. For example, when only one Task should interact with an external system at a time. It might even simply be useful because the resource cannot handle too many incoming requests at the same time.
