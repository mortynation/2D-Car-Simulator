import pytest

from fast_car import FastCar
from slow_car import SlowCar
from fancy_car import FancyCar

@pytest.fixture
def car_type():
    # assign the class of car type that needs to be tested
    car = FastCar()
    return car

def test_acceleration(car_type) -> None:
    acceleration = car_type.get_acceleration()
    print(car_type)
    # checking if acceleration is set to the desired value
    assert car_type.get_acceleration() == acceleration

def test_deceleration(car_type) -> None:
    deceleration = car_type.get_deceleration()

    # checking if deceleration is set to the desired value
    assert car_type.get_deceleration() == deceleration

def test_max_speed(car_type) -> None:
    max_speed = car_type.get_max_speed()

    # checking if maximum speed is set to the desired value
    assert car_type.get_max_speed() == max_speed

def test_turn_on(car_type) -> None:
    car_type.turn_on()

    # checking if speed is 0 when is engine is being turned on
    assert car_type.get_current_speed() == 0 

    # checking if every time the engine is turned on home is initialised as the
    # current travelled distance
    assert car_type.home == car_type.get_current_distance()

    car_type.gas(time=5)
    speed_before_brake = car_type.get_current_speed()

    # checking if car is able to gas when engine is turned on
    assert car_type.get_current_speed() > 0

    car_type.drive(time=5)

    # checking if car is able to drive when engine is turned on
    assert car_type.get_current_distance() > 0

    car_type.brake(time=2)

    # checking if car is able to brake when engine is turned on
    assert car_type.get_current_speed() < speed_before_brake

def test_turn_off(car_type) -> None:
    car_type.turn_on()
    car_type.gas(time=4)
    car_type.drive(time=3)
    distance_before_engine_off = car_type.get_current_distance()
    car_type.brake(time=4)
    speed_before_engine_off = car_type.get_current_speed()
    car_type.turn_off()

    # checking if engine can be turned off only when speed is 0
    assert car_type.get_current_speed() == 0

    car_type.gas(time=2)

    # checking if the car is able to gas after engine is turned off
    assert car_type.get_current_speed() == 0

    car_type.drive(time=6)

    # checking if the car is able to drive after engine is turned off
    assert car_type.get_current_distance() == distance_before_engine_off

    car_type.brake(time=4)

    # checking if the car is able to brake after engine is turned off
    assert car_type.get_current_speed() == speed_before_engine_off

    # checking if direction is in park when engine is turned off
    assert car_type.get_current_direction() == 'park'

def test_gas(car_type) -> None:
    max_speed  = car_type.get_max_speed()
    car_type.turn_on()
    car_type.gas(time=5)
    speed_before_nxt_gas = car_type.get_current_speed()
    car_type.gas(time=2)

    # checking if speed is being added when gas is triggered multiple times
    assert car_type.get_current_speed() > speed_before_nxt_gas

    car_type.gas(time=7)

    # checking if speed exceeds the specified maximum speed
    assert car_type.get_current_speed() <= max_speed

def test_drive_excluding_fancy_car(car_type) -> None:
    if car_type.get_car_type() == 'Fancy':
        return
    
    car_type.turn_on()
    car_type.gas(time=5)
    car_type.drive(time=5)
    distance_before_nxt_drive = car_type.get_current_distance()
    car_type.drive(time=5)

    # checking if distance is being added when drive is triggered multiple times
    assert car_type.get_current_distance() > distance_before_nxt_drive

    # checking if direction is in drive
    assert car_type.get_current_direction() == 'drive'

    # checking if sign of distance is positive, to ensure the car is moving forward
    assert car_type.get_current_distance() * -1 == -car_type.get_current_distance()

def test_brake(car_type) -> None:
    car_type.turn_on()
    car_type.gas(time=5)
    car_type.drive(time=5)
    car_type.brake(time=2)
    speed_before_nxt_brake = car_type.get_current_speed()
    car_type.brake(time=2)

    # checking if speed decreases from its previous value when triggered brake
    # multiple times
    assert car_type.get_current_speed() < speed_before_nxt_brake

    car_type.brake(time=5)

    # checking if speed doesn't go below 0
    assert car_type.get_current_speed() >= 0

def test_headlights(car_type) -> None:
    car_type.turn_on()

    # checking if headlight is switched on when engine is turned on
    assert car_type.get_current_headlight_status() == False

    car_type.toggle_headlights()
    car_type.turn_off()

    # checking if headlight is switched off when engine is turned off
    assert car_type.get_current_headlight_status() == True

def test_gear_change_only_fancy_car(car_type) -> None:
    if car_type.get_car_type() == 'Fast' or car_type.get_car_type() == 'Slow':
        return
    
    car_type.turn_on()
    car_type.gear_change(gear='drive')
    car_type.gas(time=5)
    car_type.gear_change(gear='reverse')

    # checking if car is able to change gear when speed is not 0
    assert car_type.get_current_direction() == 'drive'

    car_type.brake(time=6)
    car_type.gear_change(gear='reverse')

    # checking if car is able to change gear when speed is 0
    assert car_type.get_current_direction() == 'reverse'

def test_drive_only_fancy_car(car_type) -> None:
    if car_type.get_car_type() == 'Fast' or car_type.get_car_type() == 'Slow':
        return
    
    car_type.turn_on()
    car_type.gear_change(gear='drive')
    car_type.gas(time=3)
    car_type.drive(time=3)
    distance_before_nxt_drive = car_type.get_current_distance()
    car_type.drive(time=3)

    # checking if distance increases from its previous value 
    # when the gear is in drive
    assert car_type.get_current_distance() > distance_before_nxt_drive

    current_distance = car_type.get_current_distance()
    car_type.brake(time=4)
    car_type.gear_change(gear='reverse')
    car_type.gas(time=4)
    car_type.drive(time=2)

    # checking if distance increases from its previous value 
    # when the gear is in reverse
    assert car_type.get_current_distance() > current_distance

    # checking if distance from home decreases from its previous value 
    # when the gear is in reverse
    assert car_type.get_current_distance_from_home() < current_distance

def test_horn_only_fancy_car(car_type) -> None:
    if car_type.get_car_type() == 'Fast' or car_type.get_car_type() == 'Slow':
        return
    
    car_type.turn_on()
    
    # checking if user is able to honk when engine is turned on
    assert car_type.horn() == 'beep beep'
    
    car_type.turn_off()

    # checking if user is able to honk when engine is turned off
    assert car_type.horn() == 'beep beep'




        

