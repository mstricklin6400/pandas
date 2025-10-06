Pandas assignment — simple steps

What is in this folder
- `pandas_assignment.ipynb` — a simple Jupyter notebook with examples.
- `pandas_assignment.py` — a short script that does the same things as the notebook.
 - `data/titanic.csv` — a small CSV file so you can run the examples without downloading anything.
- `requirements.txt` — Python packages to install.

How to use (easy)
1. Edit your info in the files:
	- Open `pandas_assignment.ipynb` or `pandas_assignment.py` and change the placeholder name `YOUR_FULL_NAME` to your real name.
2. Install Python packages (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Run the script (PowerShell):

```powershell
python pandas_assignment.py
```

Or open `pandas_assignment.ipynb` in Jupyter or VS Code and run the notebook cells.

How to push to GitHub (short commands)
1. Create a new empty repository on GitHub (give it a name).
2. In PowerShell, run:

```powershell
git init
git add .
git commit -m "Add pandas assignment"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
git push -u origin main
```

Replace `<YOUR_USERNAME>` and `<REPO_NAME>` with your GitHub username and the repo name you created.

If you prefer the GitHub CLI and it is installed, you can use:

```powershell
git init
git add .
git commit -m "Add pandas assignment"
gh repo create <YOUR_USERNAME>/<REPO_NAME> --public --source=. --remote=origin
git push -u origin main
```

Notes
 - The CSV is small so the examples run quickly.
- Change the names/ages in the notebook or script to match your own information before submitting.

If you want, I can help check your files before you push them.