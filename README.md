# FastAPI Pretty Girl

A simple FastAPI web application that displays a compliment for a "pretty girl".

## Libraries Used
* **FastAPI** — Web framework
* **Uvicorn** — ASGI server
* **Jinja2** — HTML templating

## Note on Deployment
The live version is hosted on a **Free Tier** (Render.com). This means the server goes to "sleep" after inactivity. **The first load might take around 50 seconds** while the server wakes up.

## How to run
```bash
pip install -r requirements.txt
uvicorn main:app --reload