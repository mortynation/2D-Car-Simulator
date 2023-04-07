from base_car import AverageCar
avg_car = AverageCar()

class FancyCar(AverageCar):
    def __init__(self) -> None:
        super().__init__()
        self.car_type: str = 'Fancy'
        self.max_speed: float = 2 * avg_car.get_max_speed()

    def gear_change(self, gear: str) -> None:
        '''
        Changes car's gear by changing its direction when 
        speed is 0
        '''
        if self.speed == 0:
            if gear == 'drive':
                self.direction = gear
            if gear == 'reverse':
                self.direction = gear

    def drive(self, time: int) -> None:
        '''
        Increases distance of the car for the given time, doesn't
        affect acceleration, distance will be additive irrespective of
        direction and distance from home will change accordingly
        '''
        if self.engine_on == True :
            if self.direction == 'reverse':
                self.dist_from_home -= self.speed * time
                self.distance += self.speed * time
            else:
                self.distance += self.speed * time
                self.dist_from_home = self.distance - self.home

    def horn(self) -> str:
        '''
        Honks by saying 'beep beep'
        '''
        print('beep beep')
        return('beep beep')
    
fancy_car = FancyCar()


