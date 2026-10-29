# Kopitiam — Streamlit package

A Singapore kopitiam drink-ordering app: splash screen, Coffee / Tea /
Drinks tabs, cup size, Hot / Bua Siow / Peng, Siu Dai / Gah Dai /
Kosong sweetness, quantity, order view with table number, and
confirmation.

## Files

- `app.py` — Streamlit entry point. It loads `kopitiam.html` and
  renders it in the page. No server-side order storage: orders live
  in the browser, as in the original app.
- `kopitiam.html` — the complete ordering app (HTML / CSS / JS).
- `requirements.txt` — `streamlit` only.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this folder to GitHub (as the root of a repository, or as a
   folder — if it is a folder, pick that path as the app path below).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, pick the repository, branch, and main file
   `app.py` (or `<folder>/app.py` if it is in a subfolder).
4. Click **Deploy**.

## Deploy to GitHub (from this package)

If you received this as a folder, create a new repository on GitHub
and push it, for example:

```bash
git init
git add .
git commit -m "Add Kopitiam ordering app for Streamlit"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```
