# GradeOps

## Local Setup Guide

### 1. Clone the Repo
Open your terminal and clone the repo to your local machine:
```bash
git clone https://github.com/exharmonic/grade-ops
cd grade-ops
```

### 2. Setup a virtual environment
In your terminal, run:
#### Windows:
```bash 
python -m venv .venv
.venv\Scripts\activate
```
#### Git bash:
```bash
source .venv/Scripts/activate
```
#### macOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies
**Within the virtual environment**, run:
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables (.env)
For security, passwords and secrets are not uploaded to GitHub, they must instead be stored in a `.env` file.

Copy the `.env.example` file and name the new file `.env`
Now, update the `.env` file with your local PostgresSQL `user`, `password` and a preferred secret_key.
#### Generating a random secret key
In your terminal, run:
```bash
openssl rand -hex 32
```
Copy the output and use that as the secret_key

### 5. Setup the Database
Ensure that your local PostgresSQL server is running.
#### SQL shell (psql)
```sql
CREATE DATABASE gradeops_db;
```
Or you can simply, open your `pgAdmin`, and create a database `gradeops_db` manually

### 6. Run the FastAPI server
In your terminal, run:
```bash
uvicorn app.main:app --reload
```
The server will start on http://127.0.0.1:8000