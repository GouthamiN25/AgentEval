# scoring.py (optional improved safe_parse_json)
import json
import math

DIMENSIONS = [
    "reasoning_quality",
    "decision_consistency",
    "collaboration_mindset",
    "bias_awareness",
    "failure_handling",
]

def safe_parse_json(text: str) -> dict:
    cleaned = text.strip()
    # Remove markdown fences if present
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.replace("json", "", 1).strip()

    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("No JSON object found.")

    payload = cleaned[start:end + 1]
    data = json.loads(payload)

    for d in DIMENSIONS:
        if d not in data or "score" not in data[d] or "justification" not in data[d]:
            raise ValueError(f"Missing keys for {d}.")
        if not isinstance(data[d]["score"], int) or not (1 <= data[d]["score"] <= 5):
            raise ValueError(f"Invalid score for {d}.")
    if "overall_summary" not in data:
        raise ValueError("Missing overall_summary.")
    return data

def overall_score(data: dict, weights: dict | None = None) -> float:
    weights = weights or {d: 1.0 for d in DIMENSIONS}
    total_w = sum(weights.values())
    return sum(data[d]["score"] * weights[d] for d in DIMENSIONS) / total_w

def radar_series(data: dict):
    values = [data[d]["score"] for d in DIMENSIONS]
    values += values[:1]
    angles = [n / float(len(DIMENSIONS)) * 2 * math.pi for n in range(len(DIMENSIONS))]
    angles += angles[:1]
    return angles, values

