from base_car import AverageCar
avg_car = AverageCar()

class FastCar(AverageCar):
    def __init__(self) -> None:
        super().__init__()
        self.car_type: str = 'Fast'
        self.acceleration: float = 2 * avg_car.get_acceleration()
        self.deceleration: float = avg_car.get_deceleration()
        self.max_speed: float = 3 * avg_car.get_max_speed()

fast_car = FastCar()


