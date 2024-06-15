import os
import joblib
from fastapi import Body, Depends, FastAPI
from typing import Annotated, List
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class PredictRequest(BaseModel):
    passwords: List[str]


class PredictResponse(BaseModel):
    prediction: List[float]


_model = None


def get_model():
    global _model
    if _model is None:
        _path = os.getenv("MODEL_PATH", "pipeline.joblib")
        with open(_path, "rb") as f:
            _model = joblib.load(f)

    return _model


@app.post("/predict")
def predict(
    data: Annotated[PredictRequest, Body()], model=Depends(get_model)
) -> PredictResponse:
    prediction = model.predict(data.passwords)
    return PredictResponse(prediction=prediction)


@app.get("/health")
def health():
    return "OK"


def main():
    uvicorn.run(app, host="0.0.0.0")


if __name__ == "__main__":
    main()
