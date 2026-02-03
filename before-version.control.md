# Before Version Control

### Understanding the Problem
Before version control systems, managing scripts or projects was manual and error-prone:
* Making copies of files before changes
* Renaming files with dates or versions
* Emailing updates to team members
Tracking who changed what or why was difficult, leading to confusion and errors.

### Why Version Control is Needed
Version control is essential because:
* Scripts and automation evolve over time
* Configuration details change frequently
* Mistakes need safe reversal
Manual copies don’t scale; version control automates tracking, history, and rollbacks.

### Primitive Version Control Example
Without version control, undoing changes in a script that checks computer health is hard. With version control, you can safely rollback, test, and avoid repeated errors.

### Diff and Patch Commands
Tools like `diff` and `patch` allowed tracking changes:
* `diff` compares two files, highlighting only modified lines
* `<` shows lines from the original file
* `>` shows lines from the new file

Example:

```bash
diff file_v1.txt file_v2.txt
```

### Python Example
```python
# rearrange1.py
import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
```

```python
# rearrange2.py
import re

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
```

```bash
diff rearrange1.py rearrange2.py
```

```diff
6c6
<     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
---
>     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
```

### Applying Changes
Generate a patch and apply it:

```bash
diff -u old_file.py new_file.py > changes.patch
patch old_file.py < changes.patch
```

This reduces manual edits and errors, especially in large projects.

## Tools Beyond `diff`

* `wdiff` – word-by-word comparison
* Graphical tools: `meld`, `KDiff3`, `vimdiff` – highlight differences side by side

These ideas form the foundation for modern version control systems like Git.
