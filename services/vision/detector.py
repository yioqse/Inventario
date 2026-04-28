import random
from typing import Dict, Any
from services.vision.scenario_loader import _load_scenarios

def detect_products(image_path: str = None) -> Dict[str, Any]:
    """
    Orquesta la detección simulada de productos en una imagen.
    """
    print("📸 Analizando imagen para detección de productos...")
    escenarios = _load_scenarios()
    escenario = random.choice(escenarios)
    print(f"✅ Detección simulada: {escenario['descripcion']}")
    return escenario
