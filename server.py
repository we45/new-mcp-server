"""A tiny notes MCP server built with FastMCP."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("notes")

_NOTES: list[str] = []


@mcp.tool()
def add_note(text: str) -> str:
    """Store a note and return a confirmation."""
    _NOTES.append(text)
    return f"Added note #{len(_NOTES)}: {text!r}"


@mcp.tool()
def list_notes() -> list[str]:
    """Return all stored notes."""
    return list(_NOTES)


if __name__ == "__main__":
    mcp.run()
