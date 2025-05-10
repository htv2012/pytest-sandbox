import inspect
import io
import reprlib
import textwrap


def explore(obj, label: str):
    attributes_buffer = io.StringIO()
    methods_buffer = io.StringIO()

    repr_format = reprlib.Repr(maxstring=160)

    print(f"\n# Explore {obj.__class__.__name__} object")

    for name, value in inspect.getmembers(obj):
        if name.startswith("_"):
            continue
        if callable(value):
            methods_buffer.write(f"\n{name}{inspect.signature(value)}\n")
            if doc := inspect.getdoc(value):
                doc = textwrap.indent(doc, "  ")
                methods_buffer.write(f"{doc}\n")
        else:
            value_repr = repr_format.repr(value)
            attributes_buffer.write(f"\n{name} = {value_repr}\n")
    if attributes := attributes_buffer.getvalue():
        print("\n## Attributes")
        print(attributes)

    if methods := methods_buffer.getvalue():
        print("\n## Methods")
        print(methods)
