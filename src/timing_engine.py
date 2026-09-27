from __future__ import annotations

import re
import time


TIMESTAMP_RE = re.compile(r"^(?:(\d+):)?(\d{1,2})(?:\.(\d{1,3}))?$")


def parse_timestamp(value: str | int | float) -> float:
    if isinstance(value, (int, float)):
        return float(value)

    text = value.strip()
    match = TIMESTAMP_RE.match(text)
    if not match:
        raise ValueError(f"Invalid timestamp: {value!r}")

    minutes = int(match.group(1) or 0)
    seconds = int(match.group(2))
    fraction = match.group(3) or "0"
    milliseconds = int(fraction.ljust(3, "0")[:3])
    return minutes * 60 + seconds + milliseconds / 1000


class Timeline:
    def __init__(self) -> None:
        self.started_at = time.perf_counter()

    @property
    def elapsed(self) -> float:
        return time.perf_counter() - self.started_at

    def wait_until(self, target: float) -> None:
        remaining = target - self.elapsed
        if remaining > 0:
            time.sleep(remaining)
