# Python Lab 5 – Menu-Driven Programs and Logic

Programs built around `while` loops, conditionals and functions, plus written sections on the logic behind them.

## Programs

| File | Description |
|---|---|
| `atm.py` | PIN-protected ATM simulation (balance, deposit, withdraw, exit). Withdrawals are rejected if the amount exceeds the balance |
| `grade.py` | Menu to enter marks for 5 subjects, then view the average and grade (A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, else F) |
| `hint.py` | Guessing game (1–100, 10 attempts). Each wrong guess costs 10 points and shows a high/low hint plus even/odd and multiple-of-5 hints |
| `rev_guessing.py` | Reverse guessing game. You think of a number and the computer finds it with binary search from your `H`, `L` or `C` feedback |
| `combined.py` | One main menu that combines the ATM, grade calculator and guessing game as functions |

## Written Sections

| File | Content |
|---|---|
| `section_a.md` | Section A: concept check |
| `section_b.md` | Section B: trace the logic (ATM balance table, reverse-guessing walkthrough) |
| `section_d.md` | Section D: analysis (binary search efficiency, validation order, hints, loop control) |

## Run

```bash
python atm.py
python combined.py
```

## Concepts

- State kept outside the loop so it persists between menu choices
- `break` exits only the innermost loop
- Binary search needs at most 7 guesses for 1–100
- Check the balance **before** subtracting, so it never goes negative
