from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import random

# Create your views here.


def random_package():
    url = "https://pypi.org/simple/"
    headers = {"Accept": "application/vnd.pypi.simple.v1+html"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        projects = response.text

        soup = BeautifulSoup(projects, "html.parser")
        project_links = soup.find_all("a")
        project_names = [link.text for link in project_links]

        if project_names:
            random_project = random.choice(project_names)
            print(f"pypi.org/project/{random_project}/")
        else:
            print("No projects found.")
    else:
        print("Failed to fetch projects:", response.status_code, response.text)
