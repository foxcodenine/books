# Node.js Interview Practice

## The only explanation to practise now


> Node.js runs JavaScript mainly on one thread. When it starts an I/O operation, such as a database query or file read, it does not stop and wait. The operating system or libuv handles the waiting. When the result is ready, the event loop runs the callback. This allows Node.js to handle many I/O operations efficiently, but CPU-heavy JavaScript can block the main thread.

## A more natural version

This may be easier to say aloud:

> Node.js is good at handling many requests because it does not wait for I/O operations to finish. For example, while it is waiting for a database response, it can handle another request. libuv and the operating system manage the I/O, and the event loop runs the callback when the result is ready. However, a large CPU calculation can block the main JavaScript thread.

## An easy restaurant analogy

It is like a restorant with a single resturant. The waiter take the order, give it to the kitchen and go to take other orders, with out waiting for the food to be ready. When the food is done the waiter serves. The wait does not stands at the kitchen door till the food is ready, it keep taking orders and serving food. 

---

What is a blocking operation?

A blocking operation makes the program wait and do notting, while a non-blocking  one let's it keep working while the task is turned in the backgroung.

---

Why anyone would choose a blocking operation?

Blocking is much simpler to code and to maintain. If you're just write a thiny script to move one file and you don't really need the complexity of non-blocking code, or speed, you might chosse a blocking operation.
