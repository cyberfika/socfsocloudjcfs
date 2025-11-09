from flask import Flask, jsonify
import os
import platform
import psutil

# Inicialização da aplicação Flask
app = Flask(__name__)

def get_system_info():
    """Coleta e retorna as informações do sistema"""
    process = psutil.Process(os.getpid())
    
    return {
        'nome': 'Jafte Carneiro Fagundes da Silva',
        'pid': os.getpid(),
        'memoria_mb': round(process.memory_info().rss / 1024 / 1024, 2),
        'cpu_percent': psutil.cpu_percent(interval=1),
        'sistema_operacional': f"{platform.system()} ({platform.version()})"
    }

@app.route('/')
def home():
    """Rota principal - exibe informações em HTML"""
    info = get_system_info()
    return f"""
    <h1>Informações do Sistema</h1>
    <p><strong>Nome:</strong> {info['nome']}</p>
    <p><strong>PID:</strong> {info['pid']}</p>
    <p><strong>Memória usada:</strong> {info['memoria_mb']} MB</p>
    <p><strong>CPU:</strong> {info['cpu_percent']}%</p>
    <p><strong>Sistema Operacional:</strong> {info['sistema_operacional']}</p>
    """

@app.route('/info')
def info_route():
    """Retorna os integrantes do projeto em formato JSON"""
    return jsonify({
        'integrantes': 'Jafte Carneiro Fagundes da Silva'
    })

@app.route('/metricas')
def metricas_route():
    """Retorna todas as métricas do sistema em JSON"""
    return jsonify(get_system_info())

if __name__ == '__main__':
    # Executa o servidor Flask localmente
    app.run(host='0.0.0.0', port=5000)


