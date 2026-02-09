import json, os, time
from pathlib import Path

STORE_DIR = Path("runs")
STORE_DIR.mkdir(exist_ok=True)

def save_run(payload: dict) -> str:
    run_id = f"{int(time.time())}"
    path = STORE_DIR / f"{run_id}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return run_id

def list_runs():
    files = sorted(STORE_DIR.glob("*.json"), reverse=True)
    return [f.stem for f in files]

def load_run(run_id: str) -> dict:
    path = STORE_DIR / f"{run_id}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
