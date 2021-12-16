# SATUDATA 

## Requirements.

Python >= 3.7

## Installation & Usage

### Create Python Environment

```bash
python3 -m venv <env_name>
source <env_name>/bin/activate
```

```bash
pip3 install -r requirements.txt
```
### Run API

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

## Alembic
#### Upgrade DB to latest revision
```bash
alembic upgrade head
```
#### Autogenerate revision
```bash
alembic revision --autogenerate -m "<revision_message>"
```
#### Generate SQL script
```bash
alembic upgrade <revision_id> --sql
```