FROM python:3.10-slim 
# here workdir is important so everything will not be copied to the root file folder
WORKDIR /app  
# copy needed since we do not have requriements.txt in our file system 
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/app_solution.py .
#COPY fake_model.py .
COPY pipeline.joblib .  

COPY . .
CMD ["python", "app_solution.py"]