# Docs for deployment

This is the fast pipeline to ship the ml model to production with CI-CD and on free hosting on render.com. 

## Flowchart of system ## 
![frame](https://github.com/Alaboy19/model-serving-github-actions-render/assets/47283347/e47fea91-beb3-491e-828c-42c66fe13edc)

## Steps to reproduce the workflow ##

1. Build any simple model (in my case it is a just prediction of usage of specific password per million user, password[”string”] → number[”float”])
2. Build web-service based on FastAPI and dependency injection for model binary 
3. Write simple health test for web-service 
4. Package it to simple docker image and push it to dockerhub 
5. Write ci-cd.yml for github actions workflow that automates linting and testing the microservice, building and pushing the image to docker registry 
6. Execute the workflow for one time so your image pushed to docker registry 
7. Go to [render.com](http://render.com) → create account →new → web-service→”Deploy an existing image from a registry” → give image url for image pushed from your [dockerhub.com](http://dockerhub.com) registy →select free cpu server hosting → when hosted, get the RENDER_DEPLOY_HOOK secret for this service, you need this for next step in ci-cd.yml for automatic deploying of the service from github actions whenever new change pushed to the repo
8. Write deploy step in ci-cd that triggers the hook as a last step after lint, test and build_push steps in ci-cd 
9. When deployed, [render.com](http://render.com) provides endpoint of service in this format, [https://{image_name_on_dockerregistry}.onrender.com](https://fastapi-webservice-retrain-01.onrender.com/)
10. Go to this service with route /docs and test manually your service for /predict and /health routes. 

## Steps to reprocude the code ##

1. Either activate a venv and install dependencies with pip install -r requirments.txt OR you can install poetry and run poetry install
2. Generate token for access to your dockerhub account 
3. On github actions serctets → add repo secrets for DOCKERHUB_USER, DOCKERHUB_TOKEN, RENDEP_DEPLOY_HOOK.




