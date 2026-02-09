# Python and Pip Installation Troubleshooting Guide

## "command not found: pip" Error

If you see this error, it means pip isn't installed or Python can't find it. Try these solutions:

### Solution 1: Use pip3 instead of pip

On many systems, especially Mac and Linux, you need to use `pip3`:

```bash
pip3 --version
```

If this works, use `pip3` everywhere the assignment says `pip`:
```bash
pip3 install -r requirements.txt
```

### Solution 2: Use python -m pip

This tells Python to run pip as a module:

```bash
python -m pip --version
```

or

```bash
python3 -m pip --version
```

If this works, install packages like this:
```bash
python -m pip install -r requirements.txt
```

or

```bash
python3 -m pip install -r requirements.txt
```

### Solution 3: Install pip

If none of the above work, you may need to install pip.

**On Windows:**
1. pip should come with Python by default
2. If missing, reinstall Python from python.org and check "Add Python to PATH"
3. Make sure to check "pip" during installation

**On Mac:**
```bash
# If you have Homebrew
brew install python3

# Or download from python.org
```

**On Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3-pip
```

**On Linux (Fedora/CentOS):**
```bash
sudo dnf install python3-pip
```

---

## "command not found: python" Error

### Solution: Use python3 instead

On Mac and Linux, try:
```bash
python3 --version
```

If this works, use `python3` everywhere instead of `python`:
```bash
python3 app.py
```

---

## Virtual Environment Issues

### "venv\Scripts\activate" not working on Windows

Try one of these:

**PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

If you get a security error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

**Command Prompt (cmd):**
```cmd
venv\Scripts\activate.bat
```

**Git Bash on Windows:**
```bash
source venv/Scripts/activate
```

### "source venv/bin/activate" not working on Windows

This is for Mac/Linux. On Windows use:
```cmd
venv\Scripts\activate
```

---

## "ModuleNotFoundError: No module named 'flask'" After Installing

This usually means:
1. You installed packages in one Python environment but are running from another
2. You forgot to activate your virtual environment

**Solution:**
1. Make sure your virtual environment is activated (you should see `(venv)` in your terminal)
2. Reinstall packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Port Already in Use (Port 5000)

If you see "Address already in use" when running Flask:

**Solution 1: Kill the process using the port**

**On Mac/Linux:**
```bash
lsof -ti:5000 | xargs kill -9
```

**On Windows:**
```cmd
netstat -ano | findstr :5000
taskkill /PID [PID_NUMBER] /F
```

**Solution 2: Use a different port**

Edit `app.py` and change:
```python
app.run(debug=True, port=5000)
```
to:
```python
app.run(debug=True, port=5001)
```

Then visit http://localhost:5001

---

## Import Errors After Installation

### "ImportError: cannot import name 'Flask'"

**Cause:** You might have a file named `flask.py` in your project folder

**Solution:** Rename or delete any file called `flask.py`

### "ModuleNotFoundError: No module named 'requests'"

**Solution:** Make sure you installed all requirements:
```bash
pip install -r requirements.txt
```

---

## Quick Reference Commands

Here are the commands that should work on most systems:

### Check Python version:
```bash
python --version
# or
python3 --version
```

### Create virtual environment:
```bash
python -m venv venv
# or
python3 -m venv venv
```

### Activate virtual environment:
```bash
# Windows Command Prompt
venv\Scripts\activate

# Windows PowerShell
venv\Scripts\Activate.ps1

# Mac/Linux
source venv/bin/activate
```

### Install packages:
```bash
python -m pip install -r requirements.txt
# or
python3 -m pip install -r requirements.txt
# or
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```

### Run the application:
```bash
python app.py
# or
python3 app.py
```

---

## Still Having Issues?

1. **Check your Python installation:**
   - Make sure Python is installed: `python --version` or `python3 --version`
   - Should be Python 3.8 or higher

2. **Try without virtual environment:**
   - Skip the venv steps
   - Install directly: `pip install Flask requests`
   - Run: `python app.py`

3. **Ask for help:**
   - Post in the course discussion forum
   - Include:
     - Your operating system (Windows/Mac/Linux)
     - The exact error message
     - What command you ran
     - Output of `python --version` or `python3 --version`

4. **Attend office hours** for one-on-one troubleshooting