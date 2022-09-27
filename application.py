from typing import List, Dict
import random

"""
Implementación del proyecto de Aerolinea: 
Estimar las ventas por pasajes de cada vuelo comercial
"""


def main():
    """
    Función principal del módulo application
    """

    # Capacity = 168
    # Premium =  24
    # Economic = 144
    # propuesta comprobar la capacidad
    # Ver perdidas en lugar de ganancia 
    # total = economicos*preciode asientos 

    
    flights: List[Dict[str, str | int | float]] = [
        {
            "cod_ruta": "LIM - AYA",
            "name": "Lima - Ayacucho",
            "base_price": 55.19,
            "economic_price":8,
            "premiun_price":16, 
            "min_economic_sales": 120,
            "max_economic_sales": 130,
            "min_premium_sales": 10,
            "max_premium_sales": 20,
        },
        {
            "cod_ruta": "LIM - CUS",
            "name": "Lima - Cusco",
            "base_price": 136.51,
            "economic_price":8,
            "premiun_price":16, 
            "min_economic_sales": 130,
            "max_economic_sales": 144,
            "min_premium_sales": 15,
            "max_premium_sales": 24,
        },
        {
            "cod_ruta": "LIM - ARE",
            "name": "Lima - Arequipa",
            "base_price": 90.59,
            "economic_price":8,
            "premiun_price":16, 
            "min_economic_sales": 115,
            "max_economic_sales": 138,
            "min_premium_sales": 16,
            "max_premium_sales": 22,
        },
        {
            "cod_ruta": "LIM - TAR",
            "name": "Lima - Tarapoto",
            "base_price": 71.89,
            "economic_price":8,
            "premiun_price":16, 
            "min_economic_sales": 100,
            "max_economic_sales": 120,
            "min_premium_sales": 12,
            "max_premium_sales": 18,
        },
        {
            "cod_ruta": "AYA - LIM",
            "name": "Ayacucho - Lima",
            "base_price": 40.42,
            "economic_price":7,
            "premiun_price":16, 
            "min_economic_sales": 100,
            "max_economic_sales": 115,
            "min_premium_sales": 10,
            "max_premium_sales": 15,
        },
        {
            "cod_ruta": "CUS - LIM",
            "name": "Cusco - Lima",
            "base_price": 124.32,
            "economic_price":7,
            "premiun_price":16, 
            "min_economic_sales": 105,
            "max_economic_sales": 120,
            "min_premium_sales": 14,
            "max_premium_sales": 20,
        },
        {
            "cod_ruta": "ARE - LIM",
            "name": "Arequipa - Lima",
            "base_price": 86.59,
            "economic_price":7,
            "premiun_price":16, 
            "min_economic_sales": 100,
            "max_economic_sales": 110,
            "min_premium_sales": 13,
            "max_premium_sales": 28,
        },
        {
            "cod_ruta": "TAR - LIM",
            "name": "Tarapoto - Lima",
            "base_price": 68.42,
            "economic_price":7,
            "premiun_price":16, 
            "min_economic_sales": 90,
            "max_economic_sales": 105,
            "min_premium_sales": 10,
            "max_premium_sales": 15,
        }
    ]

    # costo de pasaje economico
    """
    precio venta = precio base + valor de asiento economico
    """
    # costo de pasaje premiun
    """
    precio venta = precio base + valor de asiento premiun
 
    """

    #  precio venta final = precio venta + precio venta*18/100

    print('Hola')
    # print(flights)


if __name__ == "__main__":
    main()
