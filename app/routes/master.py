from fastapi import Request, Response, APIRouter,status
from fastapi_redis_cache import cache
from middlewares.auth import VerifyTokenRoute
from fastapi.responses import JSONResponse
from models.master import User
import random

master_routes = APIRouter(route_class=VerifyTokenRoute)

@master_routes.get("/",status_code=status.HTTP_200_OK,name= "index")
def index(request: Request,response: Response):
    dbRead = request.state.db["read"]
    user = dbRead.query(User).first()
    return {"number": random.randint(0,10000) , "user" : user}


# @master_routes.get("/test/{id_user}")
# @cache(expire=3)
# def test(request: Request, id_user:int, response: Response):

#     if request.headers.get("uid_client"):


#         uid_client = request.state.uid_client
#         id_user_req = request.state.id_user
#         return {'id_user': id_user_req, 'uid_client': uid_client} #database = request.state.database
    
#     if request.headers.get("Authorization", ""):
#         #username = request.state.username
#         sessions = request.state.sessions
#         id_user_req = request.state.id_user 
#         id_client = request.state.id_client
#         id_user_adm = request.state.id_user_adm
#         uid = request.state.uid

#         print(sessions['read'])
#         session_r = sessions['read']
#         client = session_r.query(User).filter(User.id_user == id_user).first()
#         print(client)
#         return { "id_user": id_user_req, "id_client": id_client, "id_user_adm": id_user_adm, "uid": uid }
#     return JSONResponse(status_code=401, content={"message": "Unauthorized"})
