from importlib import resources

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/privacy")
async def privacy():
    file_path = resources.files("webapp.views") / 'privacy.html'

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return HTMLResponse(content=content)


@router.get("/about", response_class=HTMLResponse)
async def get_about_page():
    file_path = resources.files("webapp.views") / 'about.html'

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return HTMLResponse(content=content)