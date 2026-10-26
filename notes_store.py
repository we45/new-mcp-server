"""In-memory note storage for the notes MCP server."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Note:
    """A single stored note with metadata."""

    text: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    tags: list[str] = field(default_factory=list)

    def matches_query(self, query: str) -> bool:
        q = query.lower()
        haystack = " ".join([self.text, *self.tags]).lower()
        return q in haystack


class NotesStore:
    """Simple append-only in-memory note store."""

    def __init__(self) -> None:
        self._notes: list[Note] = []

    def add(self, text: str, tags: list[str] | None = None) -> Note:
        if not text.strip():
            raise ValueError("note text cannot be empty")
        note = Note(text=text.strip(), tags=tags or [])
        self._notes.append(note)
        return note

    def list_all(self) -> list[Note]:
        return list(self._notes)

    def delete(self, index: int) -> Note:
        if index < 0 or index >= len(self._notes):
            raise IndexError(f"note index out of range: {index}")
        return self._notes.pop(index)

    def update(self, index: int, text: str) -> Note:
        if index < 0 or index >= len(self._notes):
            raise IndexError(f"note index out of range: {index}")
        if not text.strip():
            raise ValueError("note text cannot be empty")
        self._notes[index].text = text.strip()
        return self._notes[index]

    def __len__(self) -> int:
        return len(self._notes)
