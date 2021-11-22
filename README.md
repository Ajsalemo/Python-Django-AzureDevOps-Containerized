# Python-Django-AzureDevOps-Containerized

A Containerized Django application with Bootstrap that displays some pre-defined images from Unsplash. Deployed using Azure DevOps pipelines. This repository can also be deployed to [Azure Container Apps](https://docs.microsoft.com/en-us/azure/container-apps/).

Steps to run:
- This can be ran and deployed with and without containerization.
- An Unsplash API key is needed. This is free of charge. [Link](https://unsplash.com/developers)
- You can use the existing Azure Database for PostreSQL connection in `unsplash/settings.py` -> `DATABASES` or switch this out for a database provider of your choice.
- Replace the environment variables for the above as needed.
- If using this to try out [Azure Container Apps](https://docs.microsoft.com/en-us/azure/container-apps/), update the needed values in `container-apps-deployment/deploy.json` prior to deployment.

![Imgur](https://imgur.com/qGR1ak2.png)
