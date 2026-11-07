# Python Lab 7 – Dictionaries

Menu-driven database programs that use dictionaries and nested dictionaries, plus written sections.

## Programs

| File | Description |
|---|---|
| `Student_databse.py` | Student records (roll no → name and marks). Add, update, delete, show. Reports: averages, topper, subject-wise highest, students below 40, grade groups |
| `Employee_Database.py` | Employee records (ID → name, dept, salary). Add, update salary, delete, search. Reports: department payroll and head count, highest paid per department, salary ranking, a 10% raise preview for salaries under 50,000, highest-average department |
| `Library_System.py` | Books with copies and issued-to lists. Add, issue (max 2 books per member), return, search. Reports: books by author, members holding more than one book, unavailable books, never-issued books |
| `Phone_directory.py` | Contacts with multiple phones, email and city. Add, add number, update, delete, search by partial name. Validates 10-digit numbers and blocks duplicates. Reports: reverse lookup, contacts by city, contacts with multiple numbers |
| `word_frequency.py` | Word counts for a paragraph: top N words, words appearing once, inverted frequency dictionary, words grouped by length, single-word search |

## Written Sections

| File | Content |
|---|---|
| `Part_b.md` | Part B: predict the output (references, shallow copy, comprehensions, `setdefault`, and more) |
| `Part_c.md` | Part C: short reasoning (assignment vs shallow vs deep copy, hashable keys, `d[key]` vs `get`, `update()`, deleting while iterating, inverting a dictionary, dict vs list lookup) |

## Run

```bash
python Student_databse.py
python word_frequency.py
```

Each program starts with sample data, so the reports work straight away.

## Concepts

Nested dictionaries, dictionary comprehensions, `get()`, `setdefault()`, `items()`, sorting with `key=lambda`, and average O(1) lookup through hashing.
