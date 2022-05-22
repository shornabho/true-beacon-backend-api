# TrueBeacon Full Stack Coding Assignment - Backend API

Backend API built using FastAPI for TrueBeacon Full Stack Coding Assignment.

## Setup Guide

### Install Python 🐍

Go to [Python Downloads Page](https://www.python.org/downloads/) and install the latest version of Python 3.x.x for your environment. Ensure that you add Python to your path during installation.

**Recommended:** Python 3.8.2 and above.

#### Check the version of `python` 🗒️

After a successful installation, you should be able to run:

Windows:

```bash
python --version
```

Mac/Linux:

```bash
python3 --version
```

This should give return your Python 3.x.x version.

#### Check the version of `pip` 🗒️

Windows:

```bash
pip --version
```

Mac/Linux:

```bash
pip3 --version
```

If you are prompted to upgrade the version of `pip` run the following:
Windows:

```bash
pip install --upgrade pip
```

Mac/Linux:

```bash
pip3 install --upgrade pip
```

### Install `virtualenv` 🏝️

You need to install the `virtualenv` package in the global Python 3 installation to create the virtual environment for our project later on.

Windows:

```bash
pip install virtualenv
```

Mac/Linux:

```bash
pip3 install virtualenv
```

Now check if `virtualenv` is in the path by running:

```bash
virtualenv --version
```

## Setup the Source Code 💻

### Clone the Github repository 🌐

```bash
git clone https://github.com/shornabho/true-beacon-backend-api.git
```

You may need to setup a personal access token in your Github account and have access to the repository https://github.com/shornabho/true-beacon-backend-api with that account in order to clone the project.

### Create Python 3 Virtual Environment 🏝️🐍

Make sure you are in the cloned project's root folder:

```bash
cd true-beacon-backend-api/
```

Then, to create the Virtual Environment for the project, inside the project root folder, run:

```bash
virtualenv venv
```

You should see a folder called `venv` created inside the project root folder.

### Activate Virtual Environment 🏝️ 🏃

Inside the project root folder, activate the virtual environment by running:

Windows:

```bash
.\venv\Scripts\activate
```

Mac/Linux:

```bash
source ./venv/bin/activate
```

Once the virtual environment is activated, you should see a `(venv)` prefixed to the terminal prompt.

### Install Dependencies 🧑‍🤝‍🧑

With the virtual environment activated, let's again update the version of `pip` in the virtual environment:

```bash
pip install --upgrade pip
```

To install the Python pacakges in the virtual environment, run:

```bash
pip install -r requirements.txt
```

This may take some time to complete and should install all the Python packages listed in the `requirements.txt` file in the project root folder in the `venv` virtual environment.

Once completed, you can run `pip list` to list all the packages installed in the virtual environment.

### Create a `.env` File :lock:

The project should have a `.env` file to store the environment secrets. You may create a file named `.env` (no extensions) directly in your project root folder either from the GUI File Explorer (Windows) or from your CLI (Mac/Linux) with `touch .env`.

Paste the contents of the `.env` file as shared securely directly into the file and save it.

## Run the Development Server 🏃‍♂️

Ensure that the virtual environment is activated, otherwise run the following command in your project root folder:

Windows:

```bash
.\venv\Scripts\activate
```

Mac/Linux:

```bash
source ./venv/bin/activate
```

With the virtual environment activated, run:

```bash
uvicorn app.main:app --reload
```

The development server should be running by default on port `8000`.

To view the Swagger UI Documentation for the API navigate to http://localhost:8000/docs.

---

**Creator:** [Swarnava Ghosh](https://shornabho.com)
