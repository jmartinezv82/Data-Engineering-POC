# Data-Engineering-POC

Para iniciar el proyecto se require python 3.x, pip y virtualenv.

## Virtualenv
Crear virtualenv
```bash
Mac/Linux: python3 -m venv venv
Windows: py -3 -m venv venv
```

Iniciar virtualenv
```bash
Mac/Linux: . venv/bin/activate
Windows: venv\Scripts\activate
```
## Desarrollo
Para desarrollo se debe crear un archivo `.env` en el root de la app y setear las siguientes variables:
```commandline
API=https://api.spaceflightnewsapi.net/v3
MINUTES_CRONJOB=30
MONGO_USER=
MONGO_PASSWORD=
MONGO_URL=
```

## Instalar dependencias

```bash
pip3 install -r requirements.txt
```

## Iniciar proyecto
```bash
python3 api.py
```

## desactivar virtualenv

```bash
deactivate
```

## Url de app desplegada en heroku

https://data-engineering-poc.herokuapp.com/