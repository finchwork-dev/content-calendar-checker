#!/usr/bin/env python3
"""Content calendar checker (finch-002, AI agent). Usage: python3 calendar_check.py calendar.csv [YYYY-MM-DD]
CSV columns: date,title,channel,status. Prints overdue items and posts per week/channel."""
import csv,sys,datetime as d,collections
today=d.date.fromisoformat(sys.argv[2]) if len(sys.argv)>2 else d.date.today()
rows=list(csv.DictReader(open(sys.argv[1])))
print("OVERDUE:")
for r in rows:
    dt=d.date.fromisoformat(r["date"])
    if dt<today and r["status"]!="Published":print(f'  {r["date"]} {r["title"]} [{r["channel"]}] {r["status"]}')
c=collections.Counter((d.date.fromisoformat(r["date"]).isocalendar()[1],r["channel"]) for r in rows)
print("PER WEEK/CHANNEL:")
for (w,ch),n in sorted(c.items()):print(f"  week {w} {ch}: {n}")
