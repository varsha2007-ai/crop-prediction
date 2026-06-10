# from fastapi import FastAPI, Request, Form, Depends
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel
# import uvicorn
# from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
#
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
#
#
# class InputData(BaseModel):
#     N: float
#     P: float
#     K: float
#     pH: float
#     rainfall: float
#     temperature: float
#     Area_in_hectares: float
#     State_Name: str
#     Crop_Type: str
#     Crop: str
#
#
# @app.get("/", response_class=HTMLResponse)
# async def home_page(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
#
#
# @app.get("/predict", response_class=HTMLResponse)
# async def get_prediction_form(request: Request):
#     return templates.TemplateResponse("form.html", {"request": request})
#
#
# @app.post("/predict", response_class=HTMLResponse)
# async def predict_datapoint(
#     request: Request,
#     N: float = Form(...),
#     P: float = Form(...),
#     K: float = Form(...),
#     pH: float = Form(...),
#     rainfall: float = Form(...),
#     temperature: float = Form(...),
#     Area_in_hectares: float = Form(...),
#     State_Name: str = Form(...),
#     Crop_Type: str = Form(...),
#     Crop: str = Form(...)
# ):
#     # Convert form data to CustomData format
#     data = CustomData(
#         N=N, P=P, K=K, pH=pH, rainfall=rainfall, temperature=temperature,
#         Area_in_hectares=Area_in_hectares, State_Name=State_Name, Crop_Type=Crop_Type, Crop=Crop
#     )
#
#     new_data = data.get_data_as_dataframe()
#     predict_pipeline = PredictPipeline()
#     print("---------->predict_pipeline:",predict_pipeline)
#     pred = predict_pipeline.predict(new_data)
#     print("---------->pred:",pred)
#
#     production = round(pred[0], 2)
#     yield_value = round(production / data.Area_in_hectares, 2)
#
#     final_result = f"Predicted Crop Production: {production} tons"
#     yield_result = f"Predicted Yield: {yield_value} tons/hectare"
#
#     return templates.TemplateResponse("index.html", {
#         "request": request,
#         "final_result": final_result,
#         "yield_result": yield_result
#     })
#
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=5002)

######################



from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.pipeline.prediction_pipeline import PredictPipeline
from pydantic import BaseModel
import pandas as pd
from fastapi.staticfiles import StaticFiles



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class CustomData(BaseModel):
    N: float
    P: float
    K: float
    pH: float
    rainfall: float
    temperature: float
    Area_in_hectares: float
    State_Name: str
    Crop_Type: str
    Crop:str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("welcome_page.html", {"request": request})

@app.get("/form", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post('/predict')
async def predict_yield(request: Request, N: float = Form(...), P: float = Form(...), K: float = Form(...), pH: float = Form(...),
                       rainfall: float = Form(...), temperature: float = Form(...), Area_in_hectares: float = Form(...),
                       State_Name: str = Form(...), Crop_Type: str = Form(...), Crop: str = Form(...)):
    data = CustomData(
        N=N,
        P=P,
        K=K,
        pH=pH,
        rainfall=rainfall,
        temperature=temperature,
        Area_in_hectares=Area_in_hectares,
        State_Name=State_Name,
        Crop_Type=Crop_Type,
        Crop=Crop
    )

    new_data = data.dict()
    print("-----------> new data:",new_data)
    new_data = pd.DataFrame([new_data])
    print("----------->  data frame:",new_data)

    predict_pipeline = PredictPipeline()
    print("-----------> predict pipeline:", predict_pipeline)

    pred, model_name, score = predict_pipeline.predict(new_data)
    print("-----------> Prediction:", pred, "Model Name:", model_name, "Score:", score)

    production = round(pred[0], 2)
    yield_value = round(production / data.Area_in_hectares, 2)

    model_details = f"Best model :{model_name} and accuracy score {score}"

    final_result = f"Predicted Crop Production: {production} tons"
    yield_result = f"Predicted Yield: {yield_value} tons/hectare"

    return templates.TemplateResponse("predict.html", {"request": request, "form_data": new_data.to_dict(orient="records")[0],"model_details": model_details,"final_result": final_result, "yield_result": yield_result})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5002)
