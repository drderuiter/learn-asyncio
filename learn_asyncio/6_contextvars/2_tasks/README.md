# Tasks

When using ContextVars in combination with Tasks, the behavior changes
drastically. A Task can see the context as it was when the Task was created. It can change it, too. The key difference: any changes made to the context by the Task will remain isolated in the Task.
