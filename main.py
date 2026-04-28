import sys
import os
from flask import Flask, render_template

# Asegurar que el directorio principal está en el PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.routes import api_bp

app = Flask(__name__)

# Registrar los endpoints
app.register_blueprint(api_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Configurar stdout para soportar UTF-8 en Windows, o quitar emojis
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 60)
    print("📦 SISTEMA DE INVENTARIO INTELIGENTE - REFACTORIZADO")
    print("=" * 60)
    print("🌐 Servidor disponible en: http://localhost:5005")
    print("📝 Presiona Ctrl+C para detener")
    print("=" * 60)
    app.run(debug=True, port=5005, host='0.0.0.0', threaded=True)