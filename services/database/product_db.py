from typing import Dict, Any

product_database: Dict[str, Dict[str, Any]] = {
    # Refrigerados
    "Leche Entera": {
        "id": "PROD001", "nombre": "Leche Entera", "categoria": "Refrigerados",
        "precio": 1.20, "unidad": "litro", "stock_minimo": 5, "stock_maximo": 30, "tiempo_reposicion": 2,
        "historial_ventas": [25, 28, 30, 22, 26, 25, 29, 30, 27, 24, 25, 28, 30, 26, 25, 28, 29, 24, 25, 28]
    },
    "Yogur Natural": {
        "id": "PROD002", "nombre": "Yogur Natural", "categoria": "Refrigerados",
        "precio": 0.55, "unidad": "unidad", "stock_minimo": 8, "stock_maximo": 60, "tiempo_reposicion": 2,
        "historial_ventas": [40, 45, 42, 38, 50, 41, 44, 46, 39, 42, 45, 48, 41, 43, 40, 45, 47, 42, 41, 44]
    },
    "Queso Fresco": {
        "id": "PROD003", "nombre": "Queso Fresco", "categoria": "Refrigerados",
        "precio": 2.80, "unidad": "pieza", "stock_minimo": 4, "stock_maximo": 20, "tiempo_reposicion": 3,
        "historial_ventas": [15, 12, 14, 16, 18, 15, 13, 14, 15, 16, 12, 14, 15, 16, 14, 15, 13, 14, 15, 16]
    },
    "Mantequilla": {
        "id": "PROD004", "nombre": "Mantequilla", "categoria": "Refrigerados",
        "precio": 1.95, "unidad": "tarrina", "stock_minimo": 4, "stock_maximo": 25, "tiempo_reposicion": 4,
        "historial_ventas": [18, 20, 19, 22, 21, 18, 20, 19, 20, 21, 19, 18, 20, 22, 19, 21, 20, 18, 19, 20]
    },
    "Fiambre Pavo": {
        "id": "PROD005", "nombre": "Fiambre Pavo", "categoria": "Refrigerados",
        "precio": 3.50, "unidad": "paquete", "stock_minimo": 3, "stock_maximo": 18, "tiempo_reposicion": 2,
        "historial_ventas": [12, 15, 14, 13, 16, 15, 14, 12, 13, 15, 14, 13, 16, 14, 15, 13, 12, 14, 15, 13]
    },
    "Crema de Leche": {
        "id": "PROD006", "nombre": "Crema de Leche", "categoria": "Refrigerados",
        "precio": 0.90, "unidad": "brik", "stock_minimo": 5, "stock_maximo": 35, "tiempo_reposicion": 3,
        "historial_ventas": [20, 22, 25, 21, 24, 23, 22, 25, 21, 23, 24, 22, 25, 21, 23, 22, 24, 25, 21, 23]
    },
    "Huevos M": {
        "id": "PROD007", "nombre": "Huevos M", "categoria": "Refrigerados",
        "precio": 2.50, "unidad": "docena", "stock_minimo": 3, "stock_maximo": 20, "tiempo_reposicion": 1,
        "historial_ventas": [18, 19, 17, 20, 19, 18, 17, 19, 20, 18, 17, 19, 20, 18, 17, 19, 18, 17, 20, 19]
    },

    # Conservas
    "Atún en Aceite": {
        "id": "PROD008", "nombre": "Atún en Aceite", "categoria": "Conservas",
        "precio": 1.60, "unidad": "lata", "stock_minimo": 10, "stock_maximo": 80, "tiempo_reposicion": 7,
        "historial_ventas": [5, 4, 6, 5, 7, 4, 5, 6, 5, 4, 6, 5, 7, 4, 5, 6, 5, 4, 6, 5]
    },
    "Tomate Triturado": {
        "id": "PROD009", "nombre": "Tomate Triturado", "categoria": "Conservas",
        "precio": 0.75, "unidad": "bote", "stock_minimo": 12, "stock_maximo": 100, "tiempo_reposicion": 7,
        "historial_ventas": [8, 7, 9, 8, 10, 7, 8, 9, 8, 7, 9, 8, 10, 7, 8, 9, 8, 7, 9, 8]
    },
    "Judías Blancas": {
        "id": "PROD010", "nombre": "Judías Blancas", "categoria": "Conservas",
        "precio": 1.10, "unidad": "bote", "stock_minimo": 8, "stock_maximo": 60, "tiempo_reposicion": 7,
        "historial_ventas": [4, 3, 5, 4, 6, 3, 4, 5, 4, 3, 5, 4, 6, 3, 4, 5, 4, 3, 5, 4]
    },
    "Aceitunas Verdes": {
        "id": "PROD011", "nombre": "Aceitunas Verdes", "categoria": "Conservas",
        "precio": 1.40, "unidad": "bote", "stock_minimo": 6, "stock_maximo": 50, "tiempo_reposicion": 10,
        "historial_ventas": [3, 2, 4, 3, 5, 2, 3, 4, 3, 2, 4, 3, 5, 2, 3, 4, 3, 2, 4, 3]
    },
    "Sardinas en Aceite": {
        "id": "PROD012", "nombre": "Sardinas en Aceite", "categoria": "Conservas",
        "precio": 1.80, "unidad": "lata", "stock_minimo": 8, "stock_maximo": 60, "tiempo_reposicion": 7,
        "historial_ventas": [4, 5, 3, 4, 6, 5, 4, 3, 4, 5, 3, 4, 6, 5, 4, 3, 4, 5, 3, 4]
    },
    "Maíz Dulce": {
        "id": "PROD013", "nombre": "Maíz Dulce", "categoria": "Conservas",
        "precio": 0.95, "unidad": "lata", "stock_minimo": 6, "stock_maximo": 50, "tiempo_reposicion": 7,
        "historial_ventas": [5, 6, 4, 5, 7, 6, 5, 4, 5, 6, 4, 5, 7, 6, 5, 4, 5, 6, 4, 5]
    },

    # Bebidas
    "Agua Mineral": {
        "id": "PROD014", "nombre": "Agua Mineral", "categoria": "Bebidas",
        "precio": 0.60, "unidad": "botella", "stock_minimo": 15, "stock_maximo": 100, "tiempo_reposicion": 3,
        "historial_ventas": [25, 30, 28, 32, 29, 27, 30, 28, 31, 29, 26, 30, 28, 32, 29, 27, 30, 28, 31, 29]
    },
    "Café Molido": {
        "id": "PROD015", "nombre": "Café Molido", "categoria": "Bebidas",
        "precio": 4.50, "unidad": "paquete", "stock_minimo": 3, "stock_maximo": 25, "tiempo_reposicion": 5,
        "historial_ventas": [12, 14, 13, 15, 12, 11, 14, 13, 15, 12, 11, 14, 13, 15, 12, 11, 14, 13, 15, 12]
    },
    "Zumo de Naranja UHT": {
        "id": "PROD016", "nombre": "Zumo de Naranja UHT", "categoria": "Bebidas",
        "precio": 1.35, "unidad": "brik", "stock_minimo": 8, "stock_maximo": 60, "tiempo_reposicion": 5,
        "historial_ventas": [18, 20, 19, 22, 20, 18, 19, 21, 20, 18, 19, 21, 20, 18, 19, 21, 20, 18, 19, 21]
    },
    "Refresco Cola": {
        "id": "PROD017", "nombre": "Refresco Cola", "categoria": "Bebidas",
        "precio": 1.20, "unidad": "lata", "stock_minimo": 10, "stock_maximo": 80, "tiempo_reposicion": 4,
        "historial_ventas": [22, 25, 23, 26, 24, 22, 23, 25, 24, 22, 23, 25, 24, 22, 23, 25, 24, 22, 23, 25]
    },
    "Cerveza 1905": {
        "id": "PROD018", "nombre": "Cerveza 1905", "categoria": "Bebidas",
        "precio": 1.10, "unidad": "botella", "stock_minimo": 6, "stock_maximo": 50, "tiempo_reposicion": 5,
        "historial_ventas": [15, 18, 16, 19, 17, 15, 16, 18, 17, 15, 16, 18, 17, 15, 16, 18, 17, 15, 16, 18]
    },

    # Panadería
    "Pan de Molde": {
        "id": "PROD019", "nombre": "Pan de Molde", "categoria": "Panadería",
        "precio": 1.40, "unidad": "paquete", "stock_minimo": 10, "stock_maximo": 50, "tiempo_reposicion": 1,
        "historial_ventas": [15, 18, 16, 19, 17, 15, 16, 18, 17, 15, 16, 18, 17, 15, 16, 18, 17, 15, 16, 18]
    },
    "Baguette": {
        "id": "PROD020", "nombre": "Baguette", "categoria": "Panadería",
        "precio": 0.90, "unidad": "unidad", "stock_minimo": 12, "stock_maximo": 60, "tiempo_reposicion": 1,
        "historial_ventas": [20, 25, 22, 26, 24, 20, 22, 25, 24, 20, 22, 25, 24, 20, 22, 25, 24, 20, 22, 25]
    },
    "Croissant": {
        "id": "PROD021", "nombre": "Croissant", "categoria": "Panadería",
        "precio": 0.75, "unidad": "unidad", "stock_minimo": 8, "stock_maximo": 40, "tiempo_reposicion": 1,
        "historial_ventas": [12, 15, 13, 16, 14, 12, 13, 15, 14, 12, 13, 15, 14, 12, 13, 15, 14, 12, 13, 15]
    },

    # Despensa
    "Arroz": {
        "id": "PROD022", "nombre": "Arroz", "categoria": "Despensa",
        "precio": 1.80, "unidad": "kg", "stock_minimo": 10, "stock_maximo": 60, "tiempo_reposicion": 4,
        "historial_ventas": [15, 14, 16, 15, 17, 14, 15, 16, 15, 14, 16, 15, 17, 14, 15, 16, 15, 14, 16, 15]
    },
    "Aceite de Oliva": {
        "id": "PROD023", "nombre": "Aceite de Oliva", "categoria": "Despensa",
        "precio": 4.20, "unidad": "litro", "stock_minimo": 8, "stock_maximo": 40, "tiempo_reposicion": 4,
        "historial_ventas": [8, 7, 9, 8, 10, 7, 8, 9, 8, 7, 9, 8, 10, 7, 8, 9, 8, 7, 9, 8]
    },
    "Azúcar": {
        "id": "PROD024", "nombre": "Azúcar", "categoria": "Despensa",
        "precio": 1.50, "unidad": "kg", "stock_minimo": 10, "stock_maximo": 50, "tiempo_reposicion": 3,
        "historial_ventas": [12, 11, 13, 12, 14, 11, 12, 13, 12, 11, 13, 12, 14, 11, 12, 13, 12, 11, 13, 12]
    },
    "Harina de Trigo": {
        "id": "PROD025", "nombre": "Harina de Trigo", "categoria": "Despensa",
        "precio": 1.20, "unidad": "kg", "stock_minimo": 10, "stock_maximo": 60, "tiempo_reposicion": 3,
        "historial_ventas": [14, 13, 15, 14, 16, 13, 14, 15, 14, 13, 15, 14, 16, 13, 14, 15, 14, 13, 15, 14]
    }
}
