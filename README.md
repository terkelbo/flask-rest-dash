# POC Flask Rest API with a Dash application
This repository contains code for deploying a proof-of-concept Flask Rest API which is being called from a separate Dash application. A Logistic Regression model was trained on the Iris data set and the model is deployed using Flask. The Flask server is running using Gunicorn and Meinheld for optimal performance.

Both apps can be deployed to a similar or two different webservices where the Dash app can call the Flask rest API from. To call the Flask rest API the API key needs to be appended to the POST argument which is found in the code.

This work builds on the work of other repositories:

[Flask Rest API](https://github.com/amirziai/sklearnflask)

[Flask API Key](https://github.com/ericsopa/flask-api-key)

[Gunicorn Meinheld Docker image](https://github.com/tiangolo/meinheld-gunicorn-docker)
