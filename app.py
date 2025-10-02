from flask import Flask, render_template

app = Flask(__name__)

# Datos reutilizables
site_data = {
    "materia": "Automatización de Infraestructura Digital II",
    "profesor": "Froylan Alonso Pérez Alanis",
    "alumno": "Dania Lizeth Meza Hernandez",
    "titulo": "Herramientas de Automatización en DevOps"
}

@app.route('/')
def home():
    return render_template('index.html', data=site_data)

@app.route('/devops')
def devops():
    contenido = """
    <div class="row">
        <div class="col-md-6">
            <h3>¿Qué es DevOps?</h3>
            <p>DevOps es una cultura que combina desarrollo (Dev) y operaciones (Ops) para acelerar el ciclo de vida del software.</p>
            
            <h4>Beneficios:</h4>
            <ul>
                <li>✅ Entrega continua</li>
                <li>✅ Colaboración mejorada</li>
                <li>✅ Automatización de procesos</li>
                <li>✅ Monitoreo continuo</li>
            </ul>
        </div>
        <div class="col-md-6">
            <h4>Principios de DevOps:</h4>
            <div class="card bg-light">
                <div class="card-body">
                    <p class="card-text">
                        • Colaboración entre equipos<br>
                        • Automatización de pipelines<br>
                        • Medición y monitoreo<br>
                        • Mejora continua
                    </p>
                </div>
            </div>
        </div>
    </div>
    """
    return render_template('base.html', titulo="DevOps", contenido=contenido, data=site_data)

@app.route('/herramientas')
def herramientas():
    herramientas_lista = [
        {"nombre": "Docker", "categoria": "Contenerización", "icono": "fa-docker"},
        {"nombre": "Jenkins", "categoria": "CI/CD", "icono": "fa-cogs"},
        {"nombre": "GitHub Actions", "categoria": "CI/CD", "icono": "fa-github"},
        {"nombre": "Kubernetes", "categoria": "Orquestación", "icono": "fa-ship"},
        {"nombre": "Terraform", "categoria": "IaC", "icono": "fa-cloud"},
        {"nombre": "Ansible", "categoria": "Configuración", "icono": "fa-play-circle"}
    ]
    return render_template('herramientas.html', herramientas=herramientas_lista, data=site_data)

@app.route('/infraestructura')
def infraestructura():
    diagrama = """
    <div class="text-center">
        <h4>Arquitectura de Infraestructura</h4>
        <div class="infra-estructura mt-4">
            <div class="nube">🌐 Internet</div>
            <div class="flecha">↓</div>
            <div class="balanceador">⚖️ Load Balancer</div>
            <div class="flecha">↓</div>
            <div class="servidores">
                <div class="servidor">🖥️ Servidor Web 1</div>
                <div class="servidor">🖥️ Servidor Web 2</div>
                <div class="servidor">🖥️ Servidor Web 3</div>
            </div>
            <div class="flecha">↓</div>
            <div class="base-datos">🗃️ Base de Datos</div>
        </div>
    </div>
    """
    return render_template('base.html', titulo="Infraestructura", contenido=diagrama, data=site_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)