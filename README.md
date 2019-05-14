# POC Flask Rest API with a Dash application
This repository contains code for deploying a proof-of-concept Flask Rest API which is being called from a separate Dash application. A Logistic Regression model was trained on the Iris data set and the model is deployed using Flask. The Flask server is running using Gunicorn and Meinheld for optimal performance.

The apps are deployed as Azure web services on the following two links:

[Dash app](http://irisrestapp.azurewebsites.net)

[Flask rest API](http://irisrest.azurewebsites.net?key=a7444d96)

In the latter the key is the API key needed to access the service.

This work builds on the work of other repositories:

[Flask Rest API](https://github.com/amirziai/sklearnflask)

[Flask API Key](https://github.com/ericsopa/flask-api-key)

[Gunicorn Meinheld Docker image](https://github.com/tiangolo/meinheld-gunicorn-docker)