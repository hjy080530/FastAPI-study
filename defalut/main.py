from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__=='__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)