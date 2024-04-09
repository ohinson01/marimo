# Copyright 2024 Marimo. All rights reserved.
from __future__ import annotations

from starlette.requests import Request

from marimo import _loggers
from marimo._server.router import APIRouter
from marimo._snippets.snippets import Snippets, read_snippets

LOGGER = _loggers.marimo_logger()

# Router for documentation
router = APIRouter()


_SNIPPETS: list[Snippets] = []


@router.get("/snippets")
async def load_snippets(
    request: Request,
) -> Snippets:
    del request
    if not _SNIPPETS:
        _SNIPPETS.append(await read_snippets())
    return _SNIPPETS[0]
