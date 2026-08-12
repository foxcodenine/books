# Node.js Chapter 1 — Interview Questions

## 1. Why is Node.js good for handling many connections?

Node.js uses **non-blocking I/O**. When one request is waiting for a database, file, or network response, Node.js can work on other requests instead of waiting.

This allows it to handle many connections efficiently with one event-loop thread.

> **Key phrase:** Node.js does not waste the main thread waiting for I/O.

This makes Node.js particularly suitable for I/O-heavy systems such as:

- APIs
- Web servers
- Real-time applications
- Network services

---

## 2. What is the event loop?

The event loop is the mechanism that checks which asynchronous operations are ready and executes their callbacks.

It processes one JavaScript callback at a time and then moves to the next one.

> **Simple version:** The event loop waits for events and runs the correct callback when an operation is ready.

### Example

```js
fs.readFile("file.txt", () => {
  console.log("File ready");
});
```

The event loop runs the callback after the file operation is ready.

---

## 3. What does non-blocking I/O mean?

Non-blocking I/O means that Node.js starts an I/O operation without stopping the JavaScript thread to wait for it.

Node.js continues doing other work, and the result is handled later when it becomes available.

### Example

```js
fs.readFile("file.txt", callback);

console.log("Node can continue");
```

Node.js does not wait at `readFile()` before continuing.

> **Key phrase:** Start the operation now, handle the result later.

---

## 4. What is libuv?

libuv is the low-level C library used by Node.js for its event loop and asynchronous I/O.

It hides the differences between operating systems and gives Node.js a consistent way to handle:

- File operations
- Network operations
- Timers
- Other asynchronous tasks

Different operating systems use different mechanisms:

```text
Linux   → epoll
macOS   → kqueue
Windows → IOCP
```

Node.js uses libuv instead of handling every operating system separately.

> **Key phrase:** libuv is the asynchronous I/O engine underneath Node.js.

---

## 5. Why can CPU-heavy code be a problem in Node.js?

JavaScript normally runs on the single event-loop thread.

If one function performs a long CPU-heavy calculation, the event loop cannot process other callbacks or requests until that calculation finishes.

### Example

```js
app.get("/slow", (req, res) => {
  performHugeCalculation();
  res.send("Finished");
});
```

While `performHugeCalculation()` is running, other requests may have to wait.

### Key difference

```text
Waiting for a database       → Node.js can handle other work
Heavy JavaScript calculation → The main thread stays busy
```

For CPU-heavy work, Node.js can use **worker threads** or another process so that the event loop remains responsive.

---

# Combined Interview Answer

> Node.js runs JavaScript mainly on one event-loop thread. It uses non-blocking I/O, so while an operation is waiting for a file, database, or network response, Node.js can handle other requests. libuv provides the event loop and asynchronous I/O support across different operating systems. This works very well for I/O-heavy applications, but CPU-heavy JavaScript can block the event loop and delay other requests.
