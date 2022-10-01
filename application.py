from typing import List, Dict
from model.flights import Flight

"""
Implementación del proyecto de Aerolinea: 
Estimar las ventas por pasajes de cada vuelo comercial
"""


def create_list_flights() -> List[Flight]:
    """
     Función que crea y devuelve una lista de objetos Flight
    """
    data_flights: List[Dict[str, str | int | float]] = [
        {
            "cod_ruta": "LIM - AYA",
            "name": "Lima - Ayacucho",
            "plane": "A001",
            "base_price": 55.19,
            "economic_price": 8,
            "premiun_price": 16,
            "min_economic_seat": 120,
            "max_economic_seat": 130,
            "min_premium_seat": 10,
            "max_premium_seat": 20,
        },
        {
            "cod_ruta": "LIM - CUS",
            "name": "Lima - Cusco",
            "plane": "A002",
            "base_price": 136.51,
            "economic_price": 8,
            "premiun_price": 16,
            "min_economic_seat": 130,
            "max_economic_seat": 144,
            "min_premium_seat": 15,
            "max_premium_seat": 24,
        },
        {
            "cod_ruta": "LIM - ARE",
            "name": "Lima - Arequipa",
            "plane": "A003",
            "base_price": 90.59,
            "economic_price": 8,
            "premiun_price": 16,
            "min_economic_seat": 115,
            "max_economic_seat": 138,
            "min_premium_seat": 16,
            "max_premium_seat": 22,
        },
        {
            "cod_ruta": "LIM - TAR",
            "name": "Lima - Tarapoto",
            "plane": "A004",
            "base_price": 71.89,
            "economic_price": 8,
            "premiun_price": 16,
            "min_economic_seat": 100,
            "max_economic_seat": 120,
            "min_premium_seat": 12,
            "max_premium_seat": 18,
        },
        {
            "cod_ruta": "AYA - LIM",
            "name": "Ayacucho - Lima",
            "plane": "A001",
            "base_price": 40.42,
            "economic_price": 7,
            "premiun_price": 16,
            "min_economic_seat": 100,
            "max_economic_seat": 115,
            "min_premium_seat": 10,
            "max_premium_seat": 15,
        },
        {
            "cod_ruta": "CUS - LIM",
            "name": "Cusco - Lima",
            "plane": "A002",
            "base_price": 124.32,
            "economic_price": 7,
            "premiun_price": 16,
            "min_economic_seat": 105,
            "max_economic_seat": 120,
            "min_premium_seat": 14,
            "max_premium_seat": 20,
        },
        {
            "cod_ruta": "ARE - LIM",
            "name": "Arequipa - Lima",
            "plane": "A003",
            "base_price": 86.59,
            "economic_price": 7,
            "premiun_price": 16,
            "min_economic_seat": 100,
            "max_economic_seat": 110,
            "min_premium_seat": 13,
            "max_premium_seat": 28,
        },
        {
            "cod_ruta": "TAR - LIM",
            "name": "Tarapoto - Lima",
            "plane": "A004",
            "base_price": 68.42,
            "economic_price": 7,
            "premiun_price": 16,
            "min_economic_seat": 90,
            "max_economic_seat": 105,
            "min_premium_seat": 10,
            "max_premium_seat": 15,
        }
    ]

    # Creamos la lista de objetos Flight
    flights: List[Flight] = []

    for k, f in enumerate(data_flights):
        # Creamos el objeto Flight
        obj_flight = Flight(str(f['cod_ruta']),
                            str(f['name']),
                            str(f['plane']),
                            float(f['base_price']),
                            float(f['economic_price']),
                            float(f['premiun_price']),
                            int(f['min_economic_seat']),
                            int(f['max_economic_seat']),
                            int(f['min_premium_seat']),
                            int(f['max_premium_seat'])
                            )
        flights.append(obj_flight)

    return flights

def main():
    """
    Función principal del módulo application
    """
    # Crear la lista de vuelos
    List_flights: List[Flight] = create_list_flights()

    # Inicializar variables
    total_passage: int = 0
    sales_total_eco: float = 0
    sales_total_pre: float = 0
    total_IGV: float = 0
    total_economic_seat: int = 0
    total_premium_seat: int = 0
    list_f:List[Dict[str, Flight | int | float]] = []
    dict_plane:Dict[str,int] = dict()

    # Recorrer la lista de vuelos
    for k, f in enumerate(List_flights):

        # Numero de asientos economicos 
        economic_seat: int = f.get_rand_seating_economic()
        # Numero de asientos premium 
        premium_seat: int = f.get_rand_seating_premium()
        # Numero total de asientos en  un vuelo 
        total_seat: int = economic_seat + premium_seat
        # Suma total de asientos entre todos los vuelos 
        total_passage += total_seat

        # Ingreso por la venta de pasajes económica en un vuelo 
        total_passage_economic: float = round(economic_seat * f.sales_price_economic_total, 2)
        # Suma total de ingresos por la venta de pasajes económicos
        sales_total_eco += total_passage_economic

        # Ingreso por la venta de pasajes premiun en un vuelo 
        total_passage_premium: float = round(premium_seat * f.sales_price_economic_total, 2)
        # Suma total de ingresos por la venta de pasajes premiun 
        sales_total_pre += total_passage_premium

        # Suma total de IGV cobrado entre todos los vuelos
        total_IGV += economic_seat * f.IGV_economic + premium_seat * f.IGV_premium

        # Numero total de asientos economicos vendidos entre todos los vuelos
        total_economic_seat += economic_seat
        # Numero total de asientos premiun vendidos entre todos los vuelos
        total_premium_seat += premium_seat

        # Total de ingresos por la venta de asientos
        sales_total: float = total_passage_economic + total_passage_premium

        # Lista de diccionario de vuelos 
        list_f.append({
            'objetc': f,
            'total_seat': total_seat,
            'sales_total': round(sales_total, 2)
        })

        # Diccionario de aviones con la cantidad de asientos vendidos 
        if not f.plane in dict_plane:
            dict_plane[f.plane] = total_seat
        else:
            dict_plane[f.plane] += total_seat

    # Vuelo con mayor cantidad de asientos vendidos entre todos los vuelos
    max_seats: Dict[str, Flight | int | float] = max(list_f, key=lambda x:x['total_seat'])
    # Vuelo con menor cantidad de asientos vendidos entre todos los vuelos
    mim_seats: Dict[str, Flight | int | float] = min(list_f, key=lambda x:x['total_seat'])

    # Lista ordena por el ingreso total de asientos
    sort_list_f = sorted(list_f, key=lambda x: x['sales_total'], reverse=True)

    # Valor promedio de pasaje economicos
    avg_passage_economic: float = sales_total_eco/total_economic_seat
    # Valor promedio de pasaje premiun
    avg_passage_premium: float = sales_total_pre/total_premium_seat

    # avión con mayor cantidad de pasajeros
    max_plane = max(
        dict_plane, key=dict_plane.get)

    print('* '*20)
    # 1.-¿Cuál es el total de pasajes vendidos entre todos los vuelos?
    print('Total de pasajes vendidos: {0:.2f}'.format(total_passage))

    # 2.-¿Cuál es el total de ingresos por la venta de pasajes económicos?
    print('Total de ventas de pasajes economicos: {0:.2f}'.format(
        sales_total_eco))

    # 3.-¿Cuál es el total de ingresos por la venta de pasajes premium?
    print('Total de ventas de pasajes premium: {0:.2f}'.format(
        sales_total_pre))

    # 4.-¿Cuál es el importe total de IGV cobrado?
    print('Total IGV cobrado: {0:.2f}'.format(total_IGV))

    # 5.-¿Cuál es el valor promedio de un pasaje económico?
    print('Promedio de pasajes económicos: {0:.2f}'.format(
        avg_passage_economic))
    
    #  6.-¿Cuál es el valor promedio de un pasaje premium?
    print('Promedio de pasajes premium: {0:.2f}'.format(avg_passage_premium))
   
    # 7.-¿Cuál fue el vuelo con la mayor cantidad de pasajeros?
    print('Vuelo con mayor cantidad de pasajeros: ',
          max_seats['objetc'].cod_ruta, 'con', max_seats['total_seat'])

    # 8.-¿Cuál fue el vuelo con la menor cantidad de pasajeros?
    print('Vuelo con menor cantidad de pasajeros: ',
          mim_seats['objetc'].cod_ruta, 'con ', mim_seats['total_seat'])

    # 9.-¿Cuáles son los tres primeros vuelos que obtuvieron los mayores ingresos por la venta de asientos?
    for f in sort_list_f[:3]:
        print('Para el vuelo', f['objetc'].cod_ruta,
              'ingreso', f['sales_total'])

    # 10.-¿Cuál fue el avión que transportó la mayor cantidad de pasajeros?

    print('El avion con la mayor cantidad fue :', max_plane,'con',dict_plane[max_plane],'pasajeros')

if __name__ == "__main__":
    main()
    # requirements
    # programar mejoras
    # corregir maximo duplicado

