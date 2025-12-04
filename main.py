from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI(title="Live Weather Dashboard")

@app.get("/", response_class=HTMLResponse)
def home():
    cities = ["London", "Tokyo", "New York", "Paris", "Sydney", "Dubai", "Mumbai", "Lagos", "Toronto", "São Paulo"]
    html = '<h1 style="text-align:center; color:#2c3e50; font-family:Arial;">Live Weather Dashboard</h1>'
    html += '<div style="max-width:700px; margin:auto;"><ul style="font-size:24px; line-height:2.8;">'

    for city in cities:
        try:
            data = requests.get(f"https://wttr.in/{city}?format=j1").json()
            temp = data["current_condition"][0]["temp_C"]
            desc = data["current_condition"][0]["weatherDesc"][0]["value"]
            html += f'<li style="background:#f8f9fa; margin:12px; padding:15px; border-radius:12px;">'
            html += f'<strong>{city}</strong>: {temp}°C — {desc}</li>'
        except:
            html += f"<li><strong>{city}</strong>: Loading…</li>"

    html += "</ul><p style='text-align:center; color:gray;'>Made by tkottai-hoshin • No API key needed</p></div>"
    return html
