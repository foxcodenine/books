# Node.js Design Patterns — Chapter 1
## Simple Interview Notes

## Chapter in one sentence

Node.js is built to handle many I/O operations efficiently by using **non-blocking I/O**, an **event loop**, and handlers such as callbacks.

---

## 1. The “Node way”

Node.js encourages code that is small, simple, and focused.

### Small core

Node.js keeps its built-in platform relatively small. Many features are provided by packages from the wider ecosystem.

### Small modules

A module should do one clear job.

Benefits:

- easier to understand
- easier to test
- easier to maintain
- easier to reuse

### Small surface area

A module should expose only what other code really needs.

```js
export function calculateTotal(items) {
  // internal details stay private
}
```

A small public API is harder to misuse and easier to change internally.

### Simplicity and pragmatism

Node.js usually prefers a simple working solution over a complicated “perfect” design.

A good summary is:

> Keep modules focused, APIs small, and designs practical.

---

## 2. Why I/O matters

**I/O** means input/output operations such as:

- reading a file
- querying a database
- receiving network data
- calling another API
- waiting for user input

I/O is much slower than normal CPU and memory operations. The CPU often has nothing useful to do while waiting for an I/O result.

---

## 3. Blocking I/O

With blocking I/O, the thread waits until the operation finishes.

```text
data = socket.read()
print(data)
```

While `socket.read()` is waiting, that thread cannot handle other work.

A traditional server can use one thread per connection, but this can waste resources because every thread uses memory and causes context switching.

### Interview answer

> Blocking I/O stops the current thread until the operation completes.

---

## 4. Non-blocking I/O

With non-blocking I/O, the request returns immediately. The program can continue doing other work while waiting.

A simple implementation could repeatedly check every resource, but this creates **busy waiting**:

```text
check socket A
check socket B
check file A
repeat
```

This wastes CPU because most resources are usually not ready.

### Interview answer

> Non-blocking I/O allows the program to start an operation and continue running instead of waiting for the result.

---

## 5. Event demultiplexer

An **event demultiplexer** watches many resources and reports only the ones that are ready.

Instead of repeatedly asking:

> Is the socket ready now?

The application asks the operating system:

> Tell me when this socket is ready.

The program can efficiently handle many I/O resources using one event loop thread.

Examples of operating-system mechanisms mentioned in the chapter:

- Linux: `epoll`
- macOS: `kqueue`
- Windows: IOCP

---

## 6. The reactor pattern

The **reactor pattern** is at the heart of Node.js asynchronous I/O.

The main idea is:

> Associate a handler with an I/O operation. Run that handler when the operation becomes ready or completes.

In Node.js, a handler is commonly a callback.

```js
readFile("data.txt", (error, data) => {
  // this function is the handler
});
```

### Simple flow

1. The application requests an I/O operation.
2. It also provides a handler.
3. The request returns immediately.
4. The application continues running.
5. When the I/O operation is ready or complete, an event is queued.
6. The event loop executes the associated handler.
7. The handler returns control to the event loop.

A handler may also start another asynchronous operation.

```text
Request I/O
    ↓
Continue other work
    ↓
I/O event becomes ready
    ↓
Event enters the queue
    ↓
Event loop runs the handler
```

### Interview definition

> The reactor pattern handles I/O by waiting for events from observed resources and dispatching each event to its associated handler.

---

## 7. The event loop

The **event loop** repeatedly processes ready events and executes their handlers.

JavaScript handlers normally run one at a time on the main event-loop thread.

Node.js exits when there are no active operations or events left to process. Open servers, sockets, timers, and pending I/O can keep it running.

### Important interview point

Node.js is often called single-threaded because the event loop runs JavaScript on one main thread.

However, that does **not** mean the entire Node.js runtime uses only one thread. Background threads can be used when necessary.

---

## 8. What is libuv?

**libuv** is the low-level I/O engine used by Node.js.

It provides a common interface across different operating systems and implements important parts of the asynchronous model.

libuv provides support for:

- the event loop
- asynchronous I/O
- event queues
- operating-system event mechanisms
- background threads for operations that cannot be handled as non-blocking OS events

For example, regular filesystem files do not support the same non-blocking behaviour on every operating system, so libuv may use a separate thread.

### Interview definition

> libuv is the cross-platform C library that provides Node.js with its event loop and low-level asynchronous I/O support.

---

## 9. Main parts of Node.js

The chapter presents Node.js as a combination of these main parts:

### V8

The JavaScript engine that executes JavaScript.

### libuv

The low-level I/O engine that supports the event loop and asynchronous operations.

### Bindings

The bridge that exposes lower-level functionality to JavaScript.

### Core JavaScript API

The built-in Node.js modules and high-level APIs used by applications.

```text
Your application
      ↓
Node.js core JavaScript API
      ↓
Bindings
      ↓
libuv and operating system

V8 executes the JavaScript
```

---

## 10. Node.js JavaScript vs browser JavaScript

Both environments execute JavaScript, but they provide different APIs.

### Browser

- has `window`
- has `document`
- has the DOM
- runs in a restricted environment for security

### Node.js

- has no browser DOM
- normally has no `window` or `document`
- can access files, networks, processes, environment variables, and other operating-system services

Examples of Node.js APIs:

- `fs` — filesystem
- `net` and `dgram` — TCP and UDP
- `http` and `https` — servers and clients
- `crypto` — encryption and hashing
- `child_process` — other processes
- `process.env` — environment variables
- `process.argv` — command-line arguments

---

## 11. Modules

Node.js has two main module styles.

### CommonJS

```js
const fs = require("node:fs");
```

### ES modules

```js
import fs from "node:fs";
```

Modules help divide an application into small, reusable pieces.

---

## 12. Native code and WebAssembly

Node.js can use modules written in compiled languages such as C, C++, or Rust through native bindings.

This can be useful for:

- reusing existing native libraries
- accessing hardware and low-level operating-system features
- improving performance for CPU-heavy work

Node.js can also run WebAssembly modules.

---

## 13. TypeScript with Node.js

TypeScript adds static types to JavaScript and can catch errors before the program runs.

TypeScript normally needs to be converted into JavaScript before execution.

Common tools mentioned in the chapter:

- `tsc`
- `ts-node`
- `tsx`
- `@types/node`

`@types/node` provides type definitions for Node.js APIs such as `fs`, `http`, `process`, and `Buffer`.

For production, pre-compiling TypeScript avoids transpiling it every time the application starts.

---

# Interview questions and answers

## Why is Node.js good for I/O-heavy applications?

Because it can handle many concurrent I/O operations without blocking one thread for each connection.

## What is blocking I/O?

It stops the current thread until the operation finishes.

## What is non-blocking I/O?

It starts an operation and returns control immediately, allowing other work to continue.

## What is busy waiting?

Repeatedly checking whether resources are ready, which wastes CPU time.

## What is an event demultiplexer?

A mechanism that watches many I/O resources and reports which ones are ready.

## What is the reactor pattern?

A pattern where each I/O operation has a handler that is executed when the related event is processed.

## What is the event loop?

The mechanism that processes ready events and executes their handlers.

## Is Node.js single-threaded?

JavaScript normally runs on one main event-loop thread, but Node.js can use background threads for some operations.

## What is libuv?

The cross-platform C library that provides Node.js with its event loop and asynchronous I/O support.

## What is V8?

The JavaScript engine that executes Node.js JavaScript code.

## What is the difference between Node.js and browser JavaScript?

Node.js has access to operating-system resources but does not normally provide browser objects such as `window`, `document`, or the DOM.

---

# 30-second revision

- Node.js prefers small, simple, focused modules.
- I/O is slow and should not block the main JavaScript thread.
- Busy waiting wastes CPU.
- An event demultiplexer reports only ready I/O resources.
- The reactor pattern associates each I/O operation with a handler.
- The event loop runs handlers when their events are ready.
- libuv provides the event loop and cross-platform I/O layer.
- V8 executes JavaScript.
- Bindings connect JavaScript to lower-level functionality.
- Node.js can access files, networks, processes, and other OS services.
