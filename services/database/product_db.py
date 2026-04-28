from typing import Dict, Any, List

product_database: Dict[str, Dict[str, Any]] = {
    # Refrigerados
    "Leche": {
        "id": "PROD001", "nombre": "Leche", "categoria": "Refrigerados",
        "precio": 1.20, "unidad": "litro", "stock_minimo": 5,
        "stock_maximo": 30, "tiempo_reposicion": 2,
        "historial_ventas": [3, 4, 5, 2, 6, 4, 5, 3, 4, 6, 5, 4, 3, 5, 4, 6, 3, 5, 4, 5]
    },
    "Huevos": {
        "id": "PROD002", "nombre": "Huevos", "categoria": "Refrigerados",
        "precio": 2.50, "unidad": "docena", "stock_minimo": 3,
        "stock_maximo": 20, "tiempo_reposicion": 1,
        "historial_ventas": [2, 3, 2, 4, 3, 2, 3, 4, 2, 3, 4, 2, 3, 2, 4, 3, 2, 3, 2, 4]
    },
    "Yogur": {
        "id": "PROD003", "nombre": "Yogur", "categoria": "Refrigerados",
        "precio": 1.50, "unidad": "pack", "stock_minimo": 8,
        "stock_maximo": 40, "tiempo_reposicion": 2,
        "historial_ventas": [5, 6, 5, 7, 6, 5, 6, 7, 5, 6, 7, 5, 6, 5, 7, 6, 5, 6, 5, 7]
    },
    "Queso": {
        "id": "PROD004", "nombre": "Queso", "categoria": "Refrigerados",
        "precio": 4.50, "unidad": "cuña", "stock_minimo": 4,
        "stock_maximo": 15, "tiempo_reposicion": 3,
        "historial_ventas": [1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 1, 3, 2, 1, 2, 1, 3]
    },
    "Mantequilla": {
        "id": "PROD005", "nombre": "Mantequilla", "categoria": "Refrigerados",
        "precio": 2.10, "unidad": "pastilla", "stock_minimo": 5,
        "stock_maximo": 25, "tiempo_reposicion": 2,
        "historial_ventas": [2, 1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1]
    },
    
    # Conservas
    "Atún": {
        "id": "PROD006", "nombre": "Atún", "categoria": "Conservas",
        "precio": 3.20, "unidad": "pack", "stock_minimo": 10,
        "stock_maximo": 50, "tiempo_reposicion": 4,
        "historial_ventas": [4, 5, 4, 6, 5, 4, 5, 6, 4, 5, 6, 4, 5, 4, 6, 5, 4, 5, 4, 6]
    },
    "Tomate Frito": {
        "id": "PROD007", "nombre": "Tomate Frito", "categoria": "Conservas",
        "precio": 0.80, "unidad": "brick", "stock_minimo": 15,
        "stock_maximo": 60, "tiempo_reposicion": 2,
        "historial_ventas": [8, 9, 8, 10, 9, 8, 9, 10, 8, 9, 10, 8, 9, 8, 10, 9, 8, 9, 8, 10]
    },
    "Maíz": {
        "id": "PROD008", "nombre": "Maíz", "categoria": "Conservas",
        "precio": 1.10, "unidad": "lata", "stock_minimo": 8,
        "stock_maximo": 40, "tiempo_reposicion": 3,
        "historial_ventas": [3, 2, 4, 3, 2, 3, 4, 3, 2, 3, 4, 3, 2, 4, 3, 2, 3, 4, 3, 2]
    },
    "Guisantes": {
        "id": "PROD009", "nombre": "Guisantes", "categoria": "Conservas",
        "precio": 0.95, "unidad": "lata", "stock_minimo": 6,
        "stock_maximo": 30, "tiempo_reposicion": 3,
        "historial_ventas": [2, 3, 2, 4, 3, 2, 3, 4, 2, 3, 4, 2, 3, 2, 4, 3, 2, 3, 2, 4]
    },
    "Espárragos": {
        "id": "PROD010", "nombre": "Espárragos", "categoria": "Conservas",
        "precio": 2.80, "unidad": "lata", "stock_minimo": 4,
        "stock_maximo": 20, "tiempo_reposicion": 4,
        "historial_ventas": [1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 1, 3, 2, 1, 2, 1, 3]
    },

    # Bebidas
    "Agua": {
        "id": "PROD011", "nombre": "Agua", "categoria": "Bebidas",
        "precio": 0.60, "unidad": "botella", "stock_minimo": 15,
        "stock_maximo": 100, "tiempo_reposicion": 1,
        "historial_ventas": [10, 12, 11, 9, 13, 10, 12, 11, 10, 14, 12, 11, 10, 13, 11, 12, 10, 11, 12, 13]
    },
    "Refresco": {
        "id": "PROD012", "nombre": "Refresco", "categoria": "Bebidas",
        "precio": 1.20, "unidad": "lata", "stock_minimo": 12,
        "stock_maximo": 80, "tiempo_reposicion": 2,
        "historial_ventas": [8, 10, 9, 11, 10, 8, 9, 11, 10, 9, 11, 8, 10, 9, 11, 10, 8, 9, 10, 11]
    },
    "Cerveza": {
        "id": "PROD013", "nombre": "Cerveza", "categoria": "Bebidas",
        "precio": 0.80, "unidad": "lata", "stock_minimo": 20,
        "stock_maximo": 120, "tiempo_reposicion": 2,
        "historial_ventas": [15, 18, 16, 20, 17, 15, 18, 16, 20, 17, 18, 15, 16, 20, 17, 18, 15, 16, 20, 17]
    },
    "Zumo": {
        "id": "PROD014", "nombre": "Zumo", "categoria": "Bebidas",
        "precio": 1.50, "unidad": "brick", "stock_minimo": 8,
        "stock_maximo": 40, "tiempo_reposicion": 3,
        "historial_ventas": [4, 5, 4, 6, 5, 4, 5, 6, 4, 5, 6, 4, 5, 4, 6, 5, 4, 5, 4, 6]
    },
    "Vino": {
        "id": "PROD015", "nombre": "Vino", "categoria": "Bebidas",
        "precio": 4.50, "unidad": "botella", "stock_minimo": 5,
        "stock_maximo": 25, "tiempo_reposicion": 4,
        "historial_ventas": [2, 3, 2, 4, 3, 2, 3, 4, 2, 3, 4, 2, 3, 2, 4, 3, 2, 3, 2, 4]
    },

    # Panadería
    "Pan": {
        "id": "PROD016", "nombre": "Pan", "categoria": "Panadería",
        "precio": 0.90, "unidad": "barra", "stock_minimo": 10,
        "stock_maximo": 50, "tiempo_reposicion": 1,
        "historial_ventas": [8, 10, 9, 7, 11, 8, 10, 9, 8, 12, 10, 9, 8, 11, 9, 10, 8, 9, 10, 11]
    },
    "Croissant": {
        "id": "PROD017", "nombre": "Croissant", "categoria": "Panadería",
        "precio": 1.10, "unidad": "unidad", "stock_minimo": 5,
        "stock_maximo": 30, "tiempo_reposicion": 1,
        "historial_ventas": [5, 6, 5, 7, 6, 5, 6, 7, 5, 6, 7, 5, 6, 5, 7, 6, 5, 6, 5, 7]
    },
    "Ensaimada": {
        "id": "PROD018", "nombre": "Ensaimada", "categoria": "Panadería",
        "precio": 1.30, "unidad": "unidad", "stock_minimo": 4,
        "stock_maximo": 20, "tiempo_reposicion": 1,
        "historial_ventas": [3, 4, 3, 5, 4, 3, 4, 5, 3, 4, 5, 3, 4, 3, 5, 4, 3, 4, 3, 5]
    },
    "Baguette": {
        "id": "PROD019", "nombre": "Baguette", "categoria": "Panadería",
        "precio": 1.00, "unidad": "barra", "stock_minimo": 8,
        "stock_maximo": 40, "tiempo_reposicion": 1,
        "historial_ventas": [6, 7, 6, 8, 7, 6, 7, 8, 6, 7, 8, 6, 7, 6, 8, 7, 6, 7, 6, 8]
    },
    "Palmera": {
        "id": "PROD020", "nombre": "Palmera", "categoria": "Panadería",
        "precio": 1.20, "unidad": "unidad", "stock_minimo": 5,
        "stock_maximo": 25, "tiempo_reposicion": 1,
        "historial_ventas": [4, 5, 4, 6, 5, 4, 5, 6, 4, 5, 6, 4, 5, 4, 6, 5, 4, 5, 4, 6]
    },

    # Despensa
    "Arroz": {
        "id": "PROD021", "nombre": "Arroz", "categoria": "Despensa",
        "precio": 1.80, "unidad": "kg", "stock_minimo": 10,
        "stock_maximo": 60, "tiempo_reposicion": 4,
        "historial_ventas": [3, 4, 3, 5, 4, 3, 4, 5, 3, 4, 5, 3, 4, 3, 5, 4, 3, 4, 3, 5]
    },
    "Pasta": {
        "id": "PROD022", "nombre": "Pasta", "categoria": "Despensa",
        "precio": 1.10, "unidad": "paquete", "stock_minimo": 12,
        "stock_maximo": 70, "tiempo_reposicion": 3,
        "historial_ventas": [5, 6, 5, 7, 6, 5, 6, 7, 5, 6, 7, 5, 6, 5, 7, 6, 5, 6, 5, 7]
    },
    "Aceite": {
        "id": "PROD023", "nombre": "Aceite", "categoria": "Despensa",
        "precio": 4.20, "unidad": "litro", "stock_minimo": 8,
        "stock_maximo": 40, "tiempo_reposicion": 4,
        "historial_ventas": [2, 3, 2, 4, 3, 2, 3, 2, 4, 3, 2, 3, 2, 4, 3, 2, 3, 4, 2, 3]
    },
    "Harina": {
        "id": "PROD024", "nombre": "Harina", "categoria": "Despensa",
        "precio": 1.20, "unidad": "kg", "stock_minimo": 10,
        "stock_maximo": 60, "tiempo_reposicion": 3,
        "historial_ventas": [3, 4, 3, 5, 4, 3, 4, 5, 3, 4, 5, 3, 4, 3, 5, 4, 3, 4, 3, 5]
    },
    "Azúcar": {
        "id": "PROD025", "nombre": "Azúcar", "categoria": "Despensa",
        "precio": 1.50, "unidad": "kg", "stock_minimo": 10,
        "stock_maximo": 50, "tiempo_reposicion": 3,
        "historial_ventas": [4, 5, 4, 6, 5, 4, 5, 6, 4, 5, 6, 4, 5, 4, 6, 5, 4, 5, 4, 6]
    }
}
