# Python Lab 2 – Loops and Patterns

Pattern-printing programs using `for` loops, nested loops and string multiplication.

## Files

| File | Pattern | Size |
|---|---|---|
| `Pattern1.py` | Solid square of `*` | 5 × 5 |
| `Pattern2.py` | Right-angled triangle that grows from 1 to 10 stars | 10 rows |
| `Pattern3.py` | Centered pyramid (1, 3, 5, … stars per row) | 10 rows |
| `Pattern4.py` | Wide figure with a full top bar and a widening gap in the middle | 10 rows |
| `Pattern5.py` | Hourglass or bow-tie: full bar, gap narrowing then widening, full bar | `count = 5` |
| `Pattern6.py` | Square of concentric number rings (4 on the outside down to 1 in the center) | 7 × 7 |

## Run

```bash
python Pattern1.py
```

The size is set by the `count` variable at the top of each file. Change it to resize the pattern.

## Concepts

`range()`, nested `for` loops, `print(..., end=" ")`, repeating strings with `*`, and `min()` for distance from the border (Pattern 6).
