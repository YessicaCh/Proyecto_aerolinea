import random
IGV_PERCENT: int = 18


class Flight(object):

    def __init__(self, cod_ruta: str, name: str, plane: str, base_price: float,
                 economic_price: float, premium_price: float,
                 min_economic_seat: int, max_economic_seat: int,
                 min_premium_seat: int, max_premium_seat: int):

        self.cod_ruta: str = cod_ruta
        self.name: str = name
        self.plane: str = plane
        self.base_price: float = base_price

        self.economic_price: float = economic_price
        self.premium_price: float = premium_price

        self.min_economic_seat: int = min_economic_seat
        self.max_economic_seat: int = max_economic_seat

        self.min_premium_seat: int = min_premium_seat
        self.max_premium_seat: int = max_premium_seat

        # calculo costo de pasaje economico y premiun
        self.sales_price_economic: float = round(
            self.base_price + self.economic_price, 2)
        self.sales_price_premium: float = round(
            self.base_price + self.premium_price, 2)

        self.IGV_economic: float = round(
            self.sales_price_economic*IGV_PERCENT/100, 2)
        self.IGV_premium: float = round(
            self.sales_price_economic*IGV_PERCENT/100, 2)

        # calculo de precio final economico y premiun
        self.sales_price_economic_total: float = round(
            self.sales_price_economic + self.IGV_economic, 2)
        self.sales_price_premium_total: float = round(
            self.sales_price_premium + self.IGV_premium, 2)

    def get_rand_seating_economic(self) -> int:
        """
        Devuelve un número de asientos de manera aleatoria basada en el rango
        de asientos mínimas y máximas del vuelo.
        """
        return random.randint(self.min_economic_seat, self.max_economic_seat)

    def get_rand_seating_premium(self) -> int:
        """
        Devuelve un número de asientos de manera aleatoria basada en el rango
        de asientos mínimas y máximas del vuelo.
        """
        return random.randint(self.min_premium_seat, self.max_premium_seat)
