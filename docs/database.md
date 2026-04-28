# BLOQUE 4 — Base de Datos Ampliada: 25

Productos

La empresa Markettalento gestiona 25 productos organizados en 5 categorías. El archivo
services/database/product_db.py debe contener exactamente esta base de datos. Está estructurada como un dict de Python con type hints explícitos en la declaración.

# 4.1 — Categoría: Refrigerados (frío)

ID Nombre Precio €
Unidad
Stk.Min
Stk.Max
T.Repos (días)
1 Leche Entera 1.20 litro 5 30 2
2 Yogur Natural 0.55 unidad 8 60 2
3 Queso Fresco 2.80 pieza 4 20 3
4 Mantequilla 1.95 tarrina 4 25 4
5 Fiambre Pavo 3.50 paquete 3 18 2
6 Crema de Leche 0.90 brik 5 35 3
7 Huevos M 2.50 docena 3 20 1

# 4.2 — Categoría: Conservas

ID Nombre Precio €
Unidad
Stk.Min
Stk.Max
T.Repos (días)
8 Atún en Aceite 1.60 lata 10 80 7
9 Tomate Triturado 0.75 bote 12 100 7
10 Judías Blancas 1.10 bote 8 60 7
11
Aceitunas
Verdes 1.40 bote 6 50 10
12 Sardinas en
Aceite 1.80 lata 8 60 7
13 Maíz Dulce 0.95 lata 6 50 7

# 4.3 — Categoría: Bebidas

ID Nombre Precio €
Unidad
Stk.Min
Stk.Max
T.Repos (días)
14 Agua Mineral 0.60 botella 15 100 3
15 Café Molido 4.50 paquete 3 25 5
16 Zumo de
Naranja UHT 1.35 brik 8 60 5
17 Refresco Cola 1.20 lata 10 80 4
18 Cerveza 1905 1.10 botella 6 50 5

# 4.4 — Categoría: Panadería

ID Nombre Precio €
Unidad
Stk.Min
Stk.Max
T.Repos (días)
19 Pan de Molde 1.40 paquete 10 50 1
20 Baguette 0.90 unidad 12 60 1
21 Croissant 0.75 unidad 8 40 1

# 4.5 — Categoría: Despensa

ID Nombre Precio €
Unidad
Stk.Min
Stk.Max
T.Repos (días)
22 Arroz 1.80 kg 10 60 4
23 Aceite de Oliva 4.20 litro 8 40 4
24 Azúcar 1.50 kg 10 50 3
25 Harina de Trigo 1.20 kg 10 60 3

Nota: El historial de ventas de cada producto debe ser una lista de 20 enteros representando las unidades vendidas por día. Los valores deben ser coherentes con la categoría: los Refrigerados
tienen alta rotación diaria, las Conservas menor rotación. Define los valores tú mismo con criterio y documenta el criterio elegido en docs/Final.md.
