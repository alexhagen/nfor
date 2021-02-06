# nfor

`nfor` is a little library for doing nested for loops in python.  In some
grid search problems, you get some terrible code that looks like

```python
for x in xs:
    for y in ys:
        for z in zs:
            for b in bs:
                for c in cs:
                    for d in ds:
                        function(x, y, z, b, c, d)
```

If you think that's ugly, then `nfor` is for you.  It replaces the above
code with

```python
for x, y, z, b, c, d in nfor.nfor(xs, ys, zs, bs, cs, ds):
    function(x, y, z, b, c, d)
```

## Installation

`nfor` can easily be installed with

```
pip install nfor
```