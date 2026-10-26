"""Search helpers for the notes MCP server."""

from __future__ import annotations

from notes_store import Note, NotesStore


def search_notes(store: NotesStore, query: str, limit: int = 20) -> list[Note]:
    """Return notes whose text or tags contain the query (case-insensitive)."""
    q = query.strip()
    if not q:
        return []
    matches = [n for n in store.list_all() if n.matches_query(q)]
    # Prefer shorter, more recent notes when many match.
    matches.sort(key=lambda n: (len(n.text), n.created_at), reverse=True)
    return matches[:limit]


def format_search_results(notes: list[Note]) -> list[str]:
    """Format notes for MCP tool output."""
    return [
        f"[{i}] {n.text}" + (f" (tags: {', '.join(n.tags)})" if n.tags else "")
        for i, n in enumerate(notes)
    ]
