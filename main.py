from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# CORS configuration

@app.get("/")
async def welecome():
    try:
        
        return {"message": "Hello, World!!!!!"}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/test")
async def welecome():
    try:
        
        return {"message": "Bienvenue a l'API FastAPI!"}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))