Although in some cases both methods `getValue()` and `value()` are interchangeable, you have to use `value()` method for strings and `getValue()` method for numbers.

> In your case there are three methods available for accessing `Enumeration_Knob` values and one method for setting new ones:

-   **`getValue()` brings you a number** (an index of enum's chosen pair)

-   **`value()` brings you a string** (a name of enum's chosen pair)

-   **`values()` brings you a list of all the strings** (all names)

-   **`setValue()` sets a new value for a knob** (you can use index or name here)


> You can use `getValue()` method for getting numeric properties like `scale` or `rotate`:

```python
nuke.toNode('Transform1').knob('rotate').getValue()

nuke.toNode('Transform1')['rotate'].getValue()

nuke.selectedNode()['rotate'].getValue()
```

To print all the knob's names and corresponding values of the selected node use this method:

```python
print(nuke.selectedNode())
```

> For pulldown menus 3 main methods are used – `getValue()`, `value()` and `values()` as well as `setValue()` method:

**_getValue()_**

```python
g = nuke.toNode('Transform1')['filter'].getValue()
print(g)

# getValue() method brings properties' index (because it's enumerator)
# If your filter="Notch" getValue() brings 7.0 – i.e. eight element

# Result: 7.0
```

**_value()_**

```python
v = nuke.toNode('Transform1')['filter'].value()
print(v)

# value() method brings a name of a chosen filter

# Result: Notch
```

**_values()_**

```python
vv = nuke.toNode('Merge1')['bbox'].values()
print(vv)

# values() method brings a list of all strings stored in enum

# Result: ['union', 'intersection', 'A', 'B']
```

**_setValue()_**

```python
s1 = nuke.toNode('Merge2')['operation'].setValue(0)

# setValue() method sets a new existing value in enum with index 0

# Result: atop

s2 = nuke.toNode('Merge3')['operation'].setValue("xor")

# setValue() method sets a new existing value in enum with name "xor"

# Result: xor
```
