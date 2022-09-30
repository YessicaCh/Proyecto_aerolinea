from typing import List, Dict
from model.flights import Flight
import random

"""
Implementación del proyecto de Aerolinea: 
Estimar las ventas por pasajes de cada vuelo comercial
"""
def create_list_flights():
    flights: List[Dict[str, str | int | float]] = [
        {
            "cod_ruta": "LIM - AYA",
            "name": "Lima - Ayacucho",
            "base_price": 55.19,
            "economic_price":8,
            "premiun_price":16, 
            "min_economic_seat": 120,
            "max_economic_seat": 130,
            "min_premium_seat": 10,
            "max_premium_seat": 20,
        },
        {
            "cod_ruta": "LIM - CUS",
            "name": "Lima - Cusco",
            "base_price": 136.51,
            "economic_price":8,
            "premiun_price":16, 
            "min_economic_seat": 130,
            "max_economic_seat": 144,
            "min_premium_seat": 15,
            "max_premium_seat": 24,
        },
        {
            "cod_ruta": "LIM - ARE",
            "name": "Lima - Arequipa",
            "base_price": 90.59,
            "economic_price":8,
            "premiun_price":16, 
            "min_economic_seat": 115,
            "max_economic_seat": 138,
            "min_premium_seat": 16,
            "max_premium_seat": 22,
        },
        {
            "cod_ruta": "LIM - TAR",
            "name": "Lima - Tarapoto",
            "base_price": 71.89,
            "economic_price":8,
            "premiun_price":16, 
            "min_economic_seat": 100,
            "max_economic_seat": 120,
            "min_premium_seat": 12,
            "max_premium_seat": 18,
        },
        {
            "cod_ruta": "AYA - LIM",
            "name": "Ayacucho - Lima",
            "base_price": 40.42,
            "economic_price":7,
            "premiun_price":16, 
            "min_economic_seat": 100,
            "max_economic_seat": 115,
            "min_premium_seat": 10,
            "max_premium_seat": 15,
        },
        {
            "cod_ruta": "CUS - LIM",
            "name": "Cusco - Lima",
            "base_price": 124.32,
            "economic_price":7,
            "premiun_price":16, 
            "min_economic_seat": 105,
            "max_economic_seat": 120,
            "min_premium_seat": 14,
            "max_premium_seat": 20,
        },
        {
            "cod_ruta": "ARE - LIM",
            "name": "Arequipa - Lima",
            "base_price": 86.59,
            "economic_price":7,
            "premiun_price":16, 
            "min_economic_seat": 100,
            "max_economic_seat": 110,
            "min_premium_seat": 13,
            "max_premium_seat": 28,
        },
        {
            "cod_ruta": "TAR - LIM",
            "name": "Tarapoto - Lima",
            "base_price": 68.42,
            "economic_price":7,
            "premiun_price":16, 
            "min_economic_seat": 90,
            "max_economic_seat": 105,
            "min_premium_seat": 10,
            "max_premium_seat": 15,
        }
    ]

    # Creamos la lista de objetos Flights
    List_flights: List[Flight] = []

    for k,f in enumerate(flights):
        # Creamos el objeto Product
        
        obj_flight = Flight(str(f['cod_ruta']), 
                            str(f['name']), 
                            float(f['base_price']), 
                            float(f['economic_price']), 
                            float(f['premiun_price']),
                            int(f['min_economic_seat']),
                            int(f['max_economic_seat']),
                            int(f['min_premium_seat']),
                            int(f['max_premium_seat'])
                            )
        List_flights.append(obj_flight)

    return List_flights 


def main():
    """
    Función principal del módulo application
    """

    # Capacity = 168
    # Premium =  24
    # Economic = 144
    # propuesta comprobar la capacidad
    # Ver perdidas en lugar de ganancia  y ver en que horario ocurre mas perdidas
    # total = economicos*preciode asientos 
    List_flights: List[Flight] = create_list_flights()

    # ¿Cuál es el total de pasajes vendidos entre todos los vuelos?
    # Total de pasajes vendidos 
    total_passage:int = 0
    sales_total_eco: float = 0
    sales_total_pre:float = 0
    total_IGV: float = 0
    total_economic_seat: int = 0
    total_premium_seat: int = 0
    max_total_seat: int = 0
    min_total_seat: int = 0
    cod_rut_max: str = ""
    cod_rut_min: str = ""

    for k,f in enumerate(List_flights):
        # Total de pasajes vendidos 
        economic_seat = f.get_rand_seating_economic()
        premium_seat = f.get_rand_seating_premium()
        total_seat = economic_seat + premium_seat
        total_passage += total_seat

        # ¿Cuál es el total de ingresos por la venta de pasajes económicos?}

        passage_econimic = f.sales_price_economic_total
        total_passage_economic = round(economic_seat * passage_econimic, 2)          
        sales_total_eco += total_passage_economic

        # ¿Cuál es el total de ingresos por la venta de pasajes premium?

        passage_premium = f.sales_price_economic_total
        total_passage_premium = round(premium_seat * passage_premium, 2)
        sales_total_pre += total_passage_premium

        # ¿Cuál es el importe total de IGV cobrado?
        # supones que el culculo total del IGV cobrado es la sumatoria de la camtidad total de asientos vendidos por cada el IGV de cada clase vendida.

        total_IGV = economic_seat* f.IGV_economic + premium_seat*f.IGV_premium

        #¿Cuál es el valor promedio de un pasaje económico?
        total_economic_seat += economic_seat

        #¿Cuál es el valor promedio de un pasaje premium?
        total_premium_seat += premium_seat

        #¿Cuál fue el vuelo con la mayor cantidad de pasajeros?
        print(total_seat)
        if max_total_seat < total_seat:
            max_total_seat = total_seat
            cod_rut_max = f.cod_ruta

        #¿Cuál fue el vuelo con la menor cantidad de pasajeros?
        if k == 0: 
            min_total_seat = total_seat
        if min_total_seat > total_seat:
            min_total_seat = total_seat
            cod_rut_min = f.cod_ruta



    avg_passage_economic: float = sales_total_eco/total_economic_seat
    avg_passage_premium: float = sales_total_pre/total_premium_seat

    print('* '*20)
    print('Total de pasajes vendidos: {0:.2f}'.format(total_passage))
    print('Total de ventas de pasajes economicos: {0:.2f}'.format(sales_total_eco))
    print('Total de ventas de pasajes premium: {0:.2f}'.format(sales_total_pre))
    print('Total IGV cobrado: {0:.2f}'.format(total_IGV))
    print('Promedio de pasajes económicos: {0:.2f}'.format(avg_passage_economic))
    print('Promedio de pasajes premium: {0:.2f}'.format(avg_passage_premium))
    print('Vuelo con mayor cantidad de pasajeros: ',cod_rut_max,'con',max_total_seat)
    print('Vuelo con menor cantidad de pasajeros: ',cod_rut_min,'con ',min_total_seat)

if __name__ == "__main__":
    main()
    #create_list_flights()
