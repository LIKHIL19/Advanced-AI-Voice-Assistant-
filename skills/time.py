from datetime import datetime

def current_time() -> str:
    now = datetime.now()
    # f‑string to avoid platform‑specific '%-d'
    return f"It’s {now.strftime('%H:%M')} on {now.strftime('%A')}, {now.strftime('%B')} {now.day}, {now.year}."
