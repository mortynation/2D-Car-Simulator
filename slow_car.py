from base_car import AverageCar
avg_car = AverageCar()

class SlowCar(AverageCar):
    def __init__(self) -> None:
        super().__init__()
        self.car_type: str = 'Slow'
        self.acceleration: float = 0.75 * avg_car.get_acceleration()
        self.deceleration: float = 2 * avg_car.get_deceleration()
        self.max_speed: float = 0.75 * avg_car.get_max_speed()

slow_car = SlowCar()

