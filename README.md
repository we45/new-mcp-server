# new-mcp-server

A tiny [MCP](https://modelcontextprotocol.io) server exposing a notes tool set,
built with FastMCP. Demo project.

## Tools
- `add_note(text, tags?)` - store a note with optional comma-separated tags
- `list_notes()` - list stored notes with indices
- `update_note(index, text)` - edit a note in place
- `delete_note(index)` - remove a note
- `search_notes_tool(query, limit?)` - search notes by text or tags

## Run
```bash
uv run python server.py
```

