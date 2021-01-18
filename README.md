# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Access to Trello API

Before creating the app, you will need to navigate to [Trello](https://trello.com/en) and create an account. 

You will also need permissions to use the Trello API. To do so, navigate to the [Trello developer API keys page](https://trello.com/app-key). Copy the key and generated token, and then create two variables to store the key and token in your .env file. Ensure you are logged into your Trello account to access the key/token. 

You will also need to download [Postman](https://www.postman.com/downloads/) to use the key/token for API testing. 

## Designing the App

The App uses Trello API to create a board that sections a list of action items based upon their status (i.e. To Do, Doing and Done).

Refer to the [Trello REST API documentation](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/) to build API requests within Postman. The responses from the API calls are used to create a board, create three cards and their status, and create functionality to show when a card is marked as complete. 

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the App on a Virtual Machine (VM)

This project uses the Vagrant file to run the app within a VM. To do so, download the following sofware: [Virtual Box](https://www.virtualbox.org/), and [Vagrant](https://www.vagrantup.com/). 

Then open up a terminal window in this current project folder, and type: 

```bash
vagrant up
```
First time set up of the VM will take several minutes to download the image and set up configurations. 

Use CTRL+C to end the Vagrant session. 