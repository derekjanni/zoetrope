# Zoetrope

This is a simple tool for creating unittest code stubs from a python file. Use it
by typing:

```python
zoetrope "relative_path/to/my/file.py"
```

The result is that zoetrope will print something like:

```python
import unittest
import a_custom_class

class TestModule(unittest.TestCase): # tests for module methods

    def test_a_function(): # will use name of function in place of 'a_function'
        pass


    def test_2():
        pass

class TestClass(unittest.TestCase): # a class contained in the target module

    def test_a_function(): # tests a class method or instance method
        pass

```

## Future Development

This framework is fairly customizable and it is simple to make templates
for pytest or other unittesting frameworks
