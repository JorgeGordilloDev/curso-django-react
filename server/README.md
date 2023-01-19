# Instrucciones para arrancar el servidor

#### Desde la terminal, acceder a la carpeta `server/` y crear el entorno virtual

```ps
python -m venv .venv
```

#### Activar el entorno virtual

```ps
# windows
.\.venv\Scripts\activate

# linux
source .\.venv\bin\activate
```

#### Instalar las dependencias

```ps
pip install -r .\requirements.txt
```

#### Crear base de datos en postgres con el nombre 'todolist_db'

#### Verificar en la configuración que las credenciales de la base de datos sean las correctas

#### Aplicar migraciones en la base de datos

```ps
python .\manage.py migrate
```

#### Crear super usuario

```ps
python .\manage.py createsuperuser
```

#### Arrancar servidor de desarrollo

```ps
python .\manage.py runserver
```
