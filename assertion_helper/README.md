When we write a function which helps with the assertion, we don't want the
assertion failure trace-back to show the helper. Instead, we want to it
to show the caller. Pytest provides a global variable `__tracebackhide__`
for this purpose.
