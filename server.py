# from fastapi import FastAPI, HTTPException, Request
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
#
#
# app = FastAPI()
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
#
# @app.post("/receive-token")
# async def receive_token(request: Request):
#     print(1)
#     try:
#         data = await request.json()
#         print(f'Received data: {data}')
#     except Exception as e:
#         print(f'Error processing request: {e}')
#         raise HTTPException(status_code=500, detail="Internal Server Error")
#
#
# @app.get("/")
# async def test():
#     print("test")
#
#
# @app.get("")
# async def test2():
#     print("test")
#
#
# # @app.options("")
# # async def options1():
# #     print("options1")
# #
# #
# # @app.options("/")
# # async def options2():
# #     print("options2")
# #
# #
# # @app.options("/{id}")
# # async def ids(id):
# #     print(id)
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)


from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://your-angular-app-domain.com",
    "https://kdk-server.loca.lt"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/receive-token")
async def receive_token(request: Request):
    print("POST request received at /receive-token")
    try:
        data = await request.json()
        print(f'Received data: {data}')
        return JSONResponse(content={"status": "success", "message": "Data received"})
    except Exception as e:
        print(f'Error processing request: {e}')
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
async def root():
    print("GET request received at /")
    return {"message": "Hello World"}


@app.options("")
async def option1():
    print("option1")


@app.options("/")
async def option2():
    print("option2")


@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    print(f"OPTIONS request received for path: {full_path}")
    return JSONResponse(content={"status": "success"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
