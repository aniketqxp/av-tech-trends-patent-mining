from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterator

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_jsonl(path: Path | str) -> Iterator[Dict[str, Any]]:
    """Yield one JSON object per line from a JSONL file."""
    path = Path(path)
    with path.open('r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                yield json.loads(line)


def load_patents(filename: str = 'av_patentdata.jsonl') -> list[Dict[str, Any]]:
    """Load the main patent dataset from the data directory."""
    path = DATA_DIR / filename
    return list(load_jsonl(path))
