# Python Lab 3 – Advanced Patterns

Two pattern programs that combine loops with space and star arithmetic.

## Files

| File | Description |
|---|---|
| `diamond_hollow.py` | Hollow diamond. The top half grows, the bottom half shrinks, with only the border stars printed |
| `pattern_butterfly.py` | Butterfly. Stars grow on both sides with a widening gap, then shrink back |

## Run

```bash
python diamond_hollow.py
python pattern_butterfly.py
```

Both use `n = 5`. Change `n` at the top of the file to resize the output.

## Concepts

Leading-space calculation, an inner gap of `2*i - 1` spaces, and mirrored upper and lower halves using two loops (one counting up, one counting down).
