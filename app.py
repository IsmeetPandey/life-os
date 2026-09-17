from __future__ import annotations

import sqlite3
from datetime import date
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, field_validator

DB = Path(__file__).with_name("lifeos.db")
app = FastAPI(title="Life OS", version="0.2.0")

HTML = '''<!doctype html><html><meta name="viewport" content="width=device-width,initial-scale=1"><title>Life OS</title><style>body{font-family:system-ui;background:#0a0e13;color:#eef;margin:0}main{max-width:900px;margin:40px auto;padding:24px}input,button{padding:11px;border-radius:9px;border:1px solid #27313d;background:#111821;color:#fff}button{cursor:pointer}.row{display:flex;gap:8px;flex-wrap:wrap}section{margin-top:18px;padding:18px;border:1px solid #27313d;border-radius:14px}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.card{padding:14px;border:1px solid #27313d;border-radius:10px}.muted{color:#909cab}@media(max-width:700px){.grid{grid-template-columns:1fr 1fr}}</style><main><small>LIFE OS / MVP</small><h1>Track inputs. Inspect outcomes.</h1><p class=muted>A local-first personal feedback system for recording daily inputs and observing patterns.</p><section><div class=row><input id=g placeholder="Activity"/><input id=t type=number min=0 placeholder="minutes"/><button id=add>Add entry</button></div></section><section><h2>Today</h2><div id=today class=grid></div></section><section><h2>Observations</h2><div id=analysis>Loading…</div></section></main><script>const e=x=>String(x??'').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c]));async function load(){const r=await fetch('/api/summary');const d=await r.json();if(!r.ok)throw Error(d.detail||'Could not load summary');document.querySelector('#today').innerHTML=Object.entries(d.today).map(([k,v])=>`<div class=card><small class=muted>${e(k)}</small><h2>${e(v)} min</h2></div>`).join('')||'<div class=muted>No entries yet.</div>';document.querySelector('#analysis').innerHTML=d.analysis.map(x=>`<p>${e(x)}</p>`).join('')}document.querySelector('#add').onclick=async()=>{const goal=document.querySelector('#g').value.trim(),minutes=Number(document.querySelector('#t').value);if(!goal||!Number.isInteger(minutes)||minutes<0||minutes>1440)return;const r=await fetch('/api/entries',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({goal,minutes})});if(!r.ok)return;document.querySelector('#g').value='';document.querySelector('#t').value='';load()};load().catch(()=>document.querySelector('#analysis').textContent='Could not load observations.');</script></html>'''


def con() -> sqlite3.Connection:
    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS entries(id INTEGER PRIMARY KEY, day TEXT NOT NULL, goal TEXT NOT NULL, minutes INTEGER NOT NULL)")
    c.commit()
    return c


class Entry(BaseModel):
    goal: str = Field(min_length=1, max_length=80)
    minutes: int = Field(ge=0, le=1440)

    @field_validator("goal")
    @classmethod
    def non_blank_goal(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Activity cannot be blank")
        return value


@app.get("/", response_class=HTMLResponse)
async def index() -> str:
    return HTML


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/entries")
async def add_entry(x: Entry) -> dict[str, bool]:
    with con() as c:
        c.execute("INSERT INTO entries(day,goal,minutes) VALUES(?,?,?)", (date.today().isoformat(), x.goal, x.minutes))
    return {"ok": True}


@app.get("/api/summary")
async def summary() -> dict[str, object]:
    with con() as c:
        rows = c.execute(
            "SELECT goal,SUM(minutes) FROM entries WHERE day=? GROUP BY goal ORDER BY SUM(minutes) DESC",
            (date.today().isoformat(),),
        ).fetchall()
        days = c.execute("SELECT COUNT(DISTINCT day) FROM entries").fetchone()[0]
    return {
        "today": dict(rows),
        "analysis": [f"{days} distinct day(s) recorded.", "Record consistently before drawing conclusions from the data."],
    }
