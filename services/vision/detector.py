import random
from typing import Dict, Any, Optional
from services.vision.scenario_loader import _load_scenarios

def detect_products(image_path: Optional[str] = None) -> Dict[str, Any]:
    """Orquesta la detección simulada de productos en una imagen.

    Args:
        image_path (Optional[str], optional): La ruta de la imagen a analizar. 
            Actualmente es ignorado ya que se utiliza una simulación. 
            Por defecto es None.

    Returns:
        Dict[str, Any]: Un diccionario que representa el escenario detectado,
        conteniendo su descripción y los productos identificados.
    """
    print("📸 Analizando imagen para detección de productos...")
    escenarios = _load_scenarios()
    escenario = random.choice(escenarios)
    print(f"✅ Detección simulada: {escenario['descripcion']}")
    return escenario
