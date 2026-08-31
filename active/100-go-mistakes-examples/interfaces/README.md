# Interfaces in Go

Do not create an interface just because you can.

An interface is useful when it makes the code simpler or more flexible.

## Good uses for interfaces

### 1. Common behavior

Different types can share the same behavior.

For example, files, network connections, and strings can all provide data through `io.Reader`.

See [common behavior](01-common-behavior-with-reader-writer/).

### 2. Decoupling

An interface lets code depend on what something does instead of how it does it.

For example, a service can store a customer without knowing whether the customer is stored in MySQL, a file, or memory.

See [decoupling](02-decoupling/).

### 3. Restricting behavior

A small interface gives code access to only the methods it needs.

For example, code that only needs to read a value can receive an interface with `Get()` but no `Set()`.

See [restricting behavior](03-restricting-behavior/).

## Main lesson

Start with concrete types. Create an interface when there is a clear reason for it.

Keep interfaces small and define them close to the code that uses them.
