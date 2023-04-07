class AverageCar:
    def __init__(self) -> None:
        '''
        Initializing features of an average car
        '''
        self.car_type: str = 'Average'
        self.speed: float = 0
        self.acceleration: float = 5.0
        self.deceleration: float = 10.0
        self.distance: float = 0
        self.engine_on: bool = False
        self.headlights_on: bool = False
        self.direction: str = 'park'
        self.home: float = 0
        self.max_speed: float = 50.0
        self.dist_from_home: float = 0
    
    def get_car_type(self) -> str:
        return self.car_type
    
    def get_max_speed(self) -> float:
        return self.max_speed

    def get_acceleration(self) -> float:
        return self.acceleration
    
    def get_deceleration(self) -> float:
        return self.deceleration

    def turn_on(self) -> None:
        '''
        Enables gas, drive and brake, and initialises current 
        travelled distance as home
        '''
        if self.speed == 0:
            self.engine_on = True
            self.home = self.distance

    def turn_off(self) -> None:
        '''
        Disables gas, drive and brake, and can be turned off 
        only when speed is 0
        '''
        if self.speed == 0:
            self.engine_on = False
            self.direction = 'park'

    def get_current_engine_status(self) -> bool:
        return self.engine_on

    def gas(self, time: float) -> None:
        '''
        Increases speed of the car for given time,
        speed cannot exceed the specified value and doesn't
        affect distance
        '''
        if self.engine_on == True:
            self.speed += self.acceleration * time
            self.speed = min(self.speed, self.max_speed)

    def get_current_speed(self) -> float:
        return self.speed

    def brake(self, time: float) -> None:
        '''
        Decreases speed of the car for given time if it is
        greater than 0 and doesn't affect distance
        '''
        if self.engine_on == True:
            self.speed -= time * self.deceleration
            self.speed = max(self.speed, 0) 

    def drive(self, time: float) -> None:
        '''
        Increases distance of the car for the given time,
        continues moving the car in the current direction and
        doesn't affect acceleration
        '''
        if self.engine_on == True:
            self.distance += self.speed * time
            self.dist_from_home = self.distance - self.home
            self.direction = 'drive'

    def get_current_distance(self) -> float:
        return self.distance
    
    def get_current_distance_from_home(self) -> float:
        return self.dist_from_home

    def get_current_direction(self) -> str:
        return self.direction
    
    def toggle_headlights(self) -> None:
        '''
        Toggles the headlight whenever called
        eg: If the headlight is ON, calling the method would turn OFF the headlight
        '''
        self.headlights_on = not self.headlights_on

    def get_current_headlight_status(self) -> bool:
        return self.headlights_on
    
    def check_dashboard(self) -> None:
        '''
        Displays information present in the odometer at the 
        particular instance
        '''
        print('Car Type: ', self.get_car_type())
        print('Engine On: ', self.get_current_engine_status())
        print('Headlights On: ', self.get_current_headlight_status())
        print('Current speed: ', self.get_current_speed(), 'm/s')
        print('Odometer value: ', self.get_current_distance(), 'm')
        print('Distance from Home: ', abs(self.get_current_distance_from_home()), 'm')
        print('Current gear: ', self.get_current_direction())

average_car = AverageCar()



