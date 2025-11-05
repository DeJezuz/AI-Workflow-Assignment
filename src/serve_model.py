"""
Minimal FastAPI service for model inference (demo). Replace with secure, authenticated endpoints in production.
"""
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/health')
async def health():
    return {'status':'ok'}

@app.post('/predict')
async def predict(payload: dict):
    # Payload should contain precomputed features
    # WARNING: This is a placeholder that returns a random score
    import random
    return {'risk_score': random.random()}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
