# Setup

Get the environment working before touching data science. Do these eight steps in order — each one assumes the previous one finished. Instructions are for **Windows 10/11 with PowerShell**; Mac/Linux differences are called out where they matter.

Total time: about 45–60 minutes, most of it downloads.

---

## Step 1 — Install Python

Python is the language the whole course is written in. Install the interpreter first, because VS Code and the virtual environment both need it to already exist.

**Option A — from PowerShell (fastest).** Open the Start menu, type `PowerShell`, press Enter, and run:

```powershell
winget install --id Python.Python.3.12 -e --source winget
```

**Option B — from the website.** Go to [python.org/downloads](https://www.python.org/downloads/) and download the Windows installer for 3.12.x. When the installer opens:

- ✅ Check **"Add python.exe to PATH"** at the bottom of the first screen. This is the single most-skipped step and the cause of nearly every "python is not recognized" error later.
- Click **Install Now**.
- If offered, click **Disable path length limit** at the end.

**Verify.** Close PowerShell and open a *new* one (PATH changes only apply to new terminals), then:

```powershell
python --version
pip --version
```

You should see `Python 3.12.x` and a pip version. Two common Windows failures:

- **A Microsoft Store page opens instead.** Windows ships a fake `python` stub. Fix it: Settings → Apps → **Advanced app settings** → **App execution aliases** → turn **off** `python.exe` and `python3.exe`. Then reopen PowerShell.
- **`python : The term 'python' is not recognized`.** PATH wasn't set. Either rerun the installer and choose *Modify* → check *Add to PATH*, or use the launcher `py --version` instead.

*Mac:* `brew install python@3.12`, or download the macOS installer from python.org. *Linux:* `sudo apt install python3 python3-venv python3-pip`.

---

## Step 2 — Create a GitHub account

GitHub hosts code online and tracks its history — "version control." It's how you save progress, see what changed and when, and never lose work to an accidental delete.

1. Go to [github.com/join](https://github.com/join).
2. Enter an email you actually check, pick a username (it becomes part of your public URL, so keep it professional), and set a strong password.
3. Verify the email GitHub sends you — the account isn't usable until you do.
4. Turn on two-factor authentication when prompted (Settings → Password and authentication → Two-factor authentication). GitHub requires it for contributors, and setting it up now avoids being locked out mid-course.

Free tier is all you need. Nothing to pay for here.

---

## Step 3 — Create a Claude account and subscribe to Pro

Claude Code is the AI pair-programmer you'll use inside VS Code in Step 6. It needs a paid plan — the free tier won't run it.

1. Go to [claude.ai](https://claude.ai) and sign up (Google sign-in or email + verification code).
2. Once signed in, open the account/profile menu in the bottom-left corner → **Settings** → **Billing** (or click **Upgrade**).
3. Choose **Pro** (~$20/month, cheaper billed annually) and complete checkout.
4. Confirm it worked: your plan should read **Pro** in Settings → Billing.

Keep this login handy — in Step 6 the Claude Code extension will ask you to sign in with it.

---

## Step 4 — Install Git

Git is the program that actually does the version control on your machine; GitHub (Step 2) is just where it syncs to. In PowerShell:

```powershell
winget install --id Git.Git -e --source winget
```

Accept any UAC prompt. When it finishes, **close PowerShell and open a new one**, then verify:

```powershell
git --version
```

You should see something like `git version 2.47.0.windows.1`.

Now tell Git who you are — every commit you make gets stamped with this, so use the same email as your GitHub account:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

*Mac:* `brew install git` (or `xcode-select --install`). *Linux:* `sudo apt install git`.

---

## Step 5 — Install VS Code

VS Code is the editor you'll write Python in. Either:

```powershell
winget install --id Microsoft.VisualStudioCode -e --source winget
```

…or download it from [code.visualstudio.com](https://code.visualstudio.com/) and run the installer. If you use the installer, check **"Add to PATH"** and both **"Open with Code"** context-menu options — they make later steps one click instead of several.

Launch VS Code, then open the integrated terminal — this is the terminal you'll use for the rest of setup:

- `` Ctrl+` `` on Windows/Linux, `` Cmd+` `` on Mac, or menu **Terminal → New Terminal**.

Confirm the tools from the previous steps are visible from *inside* VS Code:

```powershell
python --version
git --version
```

If either one isn't found, fully quit VS Code (close every window) and reopen it — VS Code only picks up PATH changes on a cold start.

---

## Step 6 — Install the VS Code extensions

Open the Extensions panel: the squares icon in the left sidebar, or `Ctrl+Shift+X`. Search each name, then click **Install**:

| Extension | Publisher | What it gives you |
|---|---|---|
| **Python** | Microsoft | Syntax highlighting, IntelliSense, virtual-env detection, notebook support |
| **Python Debugger** | Microsoft | Breakpoints and step-through debugging (usually installed automatically with Python — install it explicitly if not) |
| **Claude Code** | Anthropic | The AI pair-programmer, in a side panel |
| **Vim** | vscodevim | Modal editing keybindings |

Two notes:

- **Claude Code** — after installing, open its panel and sign in with the Claude account from Step 3. It'll open a browser window to authorize, then hand control back to VS Code.
- **Vim** — this changes how typing works: you start in *normal* mode, and press `i` to type. Press `Esc` to get back to normal mode, and `:w` + Enter to save. If it's disorienting mid-course, disable it (Extensions → Vim → **Disable**) and re-enable later; nothing in the course depends on it.

Reload VS Code when prompted (`Ctrl+Shift+P` → **Developer: Reload Window**).

---

## Step 7 — Clone the repo

Cloning downloads this project and wires it to GitHub so you can push your work back.

**7a. Create an SSH key** (this is what proves to GitHub that it's you — no password typing). In the VS Code terminal:

```powershell
ssh-keygen -t ed25519 -C "you@example.com" (use your actual email address)
```

Press Enter to accept the default location (`C:\Users\<you>\.ssh\id_ed25519`). A passphrase is optional — Enter twice to skip it.

**7b. Start the SSH agent and add the key.** Run PowerShell **as Administrator** for the first line only (Start menu → right-click PowerShell → Run as administrator):

```powershell
Set-Service ssh-agent -StartupType Automatic
Start-Service ssh-agent
```

Then back in the normal VS Code terminal:

```powershell
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

**7c. Copy the public key to your clipboard:**

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard
```

**7d. Add it to GitHub.** Go to [github.com/settings/keys](https://github.com/settings/keys) → **New SSH key** → Title: `My laptop` → Key type: **Authentication Key** → paste into the Key box → **Add SSH key**.

**7e. Test the connection:**

```powershell
ssh -T git@github.com
```

Type `yes` at the fingerprint prompt. Success looks like: `Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.` That "does not provide shell access" line is expected, not an error.

**7f. Clone.** Pick where the project should live, then clone:

```powershell
cd $env:USERPROFILE\Documents
git clone git@github.com:mkohanim/data-science-tutorial.git
cd data-science-tutorial
```

Then open it in VS Code: **File → Open Folder** → select `data-science-tutorial` (or run `code .` from the terminal).

> **SSH giving you trouble?** Skip 7a–7e and clone over HTTPS instead — it works immediately and you can set up SSH later:
> ```powershell
> git clone https://github.com/mkohanim/data-science-tutorial.git
> ```

---

## Step 8 — Create the virtual environment and install dependencies

A virtual environment ("venv") is a private copy of Python for this project. It keeps this project's packages from colliding with any other project's. The `.venv/` folder is already in `.gitignore`, so it never gets committed.

From the repo root (`data-science-tutorial`), in the VS Code terminal:

**8a. Create it:**

```powershell
python -m venv .venv
```

**8b. Activate it:**

```powershell
.venv\Scripts\Activate.ps1
```

*Mac/Linux:* `source .venv/bin/activate`

Your prompt should now start with `(.venv)`. If PowerShell refuses with *"running scripts is disabled on this system"*, allow local scripts once:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

…then run the activate command again. (Using Git Bash or `cmd` instead? Use `source .venv/Scripts/activate` or `.venv\Scripts\activate.bat`.)

**8c. Install the dependencies:**

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

That pulls in pandas, numpy, matplotlib, scikit-learn, and jupyter. Expect a few minutes.

**8d. Point VS Code at the venv** so the editor, debugger, and notebooks all use it: `Ctrl+Shift+P` → **Python: Select Interpreter** → choose the one labeled `.venv` (`.\.venv\Scripts\python.exe`).

**8e. Verify everything:**

```powershell
python -c "import pandas, numpy, sklearn, matplotlib; print('all good')"
```

If that prints `all good`, setup is done.

> **Every new terminal session:** `cd` into the repo and run `.venv\Scripts\Activate.ps1` again. Activation doesn't persist between terminals. If you ever see `ModuleNotFoundError: No module named 'pandas'`, that's the reason 90% of the time — you forgot to activate.
