# Tools

Four tools you just installed in [1-Setup](../1-Setup/setup.md). Before using them for real work, it helps to know what each one actually *is* — not just the install steps. Ten minutes per section, plain language, no jargon dump.

---

## VS Code

**What is it?**
A code editor — a program for writing and organizing code. Think of it like a word processor, but built for code: it understands Python syntax, catches typos before you run anything, and lets you run your code without leaving the window.

**What it does**

- **Explorer panel** (left sidebar) — shows every file and folder in your project, like a file browser built into the editor.
- **Integrated terminal** (`` Ctrl+` ``) — a command line living inside VS Code, so you don't need to alt-tab to a separate terminal app.
- **Syntax highlighting** — colors your code so keywords, strings, and variables are visually distinct, making mistakes easier to spot.
- **Run/Debug** — a ▶️ button that runs your `.py` file, plus a debugger that lets you pause code mid-run and inspect what every variable holds.

**Why we need it**
You could technically write Python in Notepad and run it by typing commands manually — people did for decades. VS Code just removes friction: it tells you about errors *before* you run the code, and it puts editing, running, and terminal all in one window instead of three.

**Simple example**

1. In the Explorer panel, create a file called `hello.py`.
2. Type:
   ```python
   name = "world"
   print(f"Hello, {name}!")
   ```
3. Open the integrated terminal (`` Ctrl+` ``) and run it:
   ```powershell
   python hello.py
   ```
4. You should see `Hello, world!` printed in the terminal panel — written and run without leaving the window.

---

## Git

**What is it?**
A version control system — a program that tracks every change ever made to your files, and lets you go back to any earlier version. It runs entirely on your own computer (GitHub, next, is the online part).

**What it does**

- **`git status`** — shows what's changed since your last save point.
- **`git add <file>`** — marks a file as ready to be saved ("staged").
- **`git commit -m "message"`** — actually saves a snapshot of your staged changes, with a note describing what changed.
- **`git log`** — shows the full history of snapshots, oldest project memory to newest.
- **`git push`** / **`git pull`** — send your snapshots to GitHub, or fetch snapshots someone (or your other machine) put there.

**Why we need it**
Without it, "saving versions" usually means files like `analysis_v2_FINAL_reallyfinal.py`. Git replaces that mess with a real history: every commit is a labeled checkpoint you can compare against or revert to, so breaking something is never permanent — you can always go back.

**Simple example**

```powershell
# after editing hello.py
git status                        # "hello.py has changes"
git add hello.py                  # stage it
git commit -m "Add hello.py"      # save a checkpoint with a message
git log                           # see it in the history
```

If you mess up `hello.py` beyond repair tomorrow, that commit is still there — you haven't lost the working version.

---

## Claude Code

**What is it?**
An AI pair-programmer that runs inside VS Code (or a terminal). You describe what you want in plain English, and it reads your code, suggests changes, explains errors, or writes code alongside you.

**What it does**

- **Answers questions about your code** — "why is this loop only running once?" — by actually reading the file, not guessing from a description.
- **Explains errors** — paste a traceback and ask what it means and why it happened.
- **Suggests or writes code** — for a well-scoped task, it can draft a function for you to review and edit.
- **Runs commands for you** — with your approval, it can run terminal commands like `git status` or `python hello.py` directly.

**Why we need it**
Getting stuck used to mean searching forums for an error message and hoping someone hit the same bug. Claude Code looks at *your actual code* and *your actual error*, so the answer is specific to your situation instead of a generic forum post from 2014.

**The ground rule for this course:** Claude is for getting unstuck, not for skipping the thinking. Ask it to explain *why* something is broken before asking it to fix it — the exercises are only useful if you did them.

**Simple example**

Open the Claude Code panel in VS Code and ask:

```
Why does this print 0 forever instead of stopping at 5?

count = 0
while count < 5:
    print(count)
```

Claude will point out that `count` never changes inside the loop, so `count < 5` stays true forever — the fix is adding `count += 1` inside the loop body.

---

## Vim (optional)

**What is it?**
A different *way of typing* inside the editor — a set of keybindings, not a separate program. It's a VS Code extension you installed in Setup, so you already have it; nothing runs unless you turn it on.

**What it does**
Normal text editors have one mode: you click somewhere and type. Vim splits editing into modes:

- **Normal mode** — the default. Letters are commands, not text. `j`/`k` move down/up a line, `dd` deletes a line, `x` deletes a character.
- **Insert mode** — press `i` to enter it; now typing works like any normal editor. `Esc` goes back to Normal mode.
- **Command mode** — press `:` from Normal mode to type a command, like `:w` (save) or `:q` (quit) or `:wq` (save and quit).

**Why we need it**
You don't — this is the one tool in this list that's genuinely optional. Once memorized, Vim lets people edit code without touching the mouse or arrow keys, which is faster for experienced users. It's included here because it's one of the four extensions in Setup and you'll see it mentioned; feel free to disable it (Extensions → Vim → **Disable**) and skip straight to the others.

**Simple example**

With Vim enabled, open `hello.py` and:

1. Press `Esc` to make sure you're in Normal mode.
2. Press `i` to enter Insert mode, type a line, then press `Esc` to return to Normal mode.
3. Press `dd` to delete the line you just typed.
4. Type `:wq` and press Enter to save and close the file.

If step 2 feels awkward — you tried to type and letters didn't appear as text — that's Normal mode intercepting them as commands. That's the whole learning curve in one sentence.
