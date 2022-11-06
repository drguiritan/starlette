from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import PlainTextResponse,JSONResponse
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

async def index(request:Request):
    sid = request.path_params.get("id")
    sname = request.query_params.get("sname") or "no query inputted"
    
    return PlainTextResponse(content=f"Hello student {sname} ")


async def json_out(request:JSONResponse):
    return JSONResponse(content={'msg':'Hello World'})
    
async def html_enpoint(request:Request):
    sname = "Jordan"
    context={'request':request,'msg':sname}
    return templates.TemplateResponse("index.html" , context)

routes = [
    Route('/{id:int}',endpoint = index),
    Route('/api',endpoint = json_out),
    Route('/html',endpoint = html_enpoint)
]


app = Starlette (
    debug = True,
    routes = routes    
)