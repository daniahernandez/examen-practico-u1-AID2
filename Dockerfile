FROM python:3.9-slim

WORKDIR /app

# Copiar requirements primero (para cache de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar TODOS los archivos del proyecto
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
#"materia": "Automatización de Infraestructura Digital II",
    #"profesor": "Froylan Alonso Pérez Alanis",
    #"alumno": "Dania Lizeth Meza Hernandez",
    #"titulo": "Herramientas de Automatización en DevOps"