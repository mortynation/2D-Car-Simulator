from fast_car import FastCar
from slow_car import SlowCar
from fancy_car import FancyCar

fast_car = FastCar()
slow_car = SlowCar()
fancy_car = FancyCar()

def main():
    '''
    Contains actions from __Problem Statement__
    '''
    # 1. All three cars start their engines
    fast_car.turn_on()
    slow_car.turn_on()
    fancy_car.turn_on()

    # 2. `FastCar` and `FancyCar` turn on their lights
    fast_car.toggle_headlights()
    fancy_car.toggle_headlights()

    # 3. All three cars gas for 11 seconds
    fast_car.gas(time=11.0)
    slow_car.gas(time=11.0)
    fancy_car.gear_change('drive')
    fancy_car.gas(time=11.0)

    # 4. All three cars drive for 30 seconds
    fast_car.drive(time=30.0)
    slow_car.drive(time=30.0)
    fancy_car.drive(time=30.0)

    # 5. `FancyCar` brakes for 5 seconds, slowing down in order to 
    # enjoy the scenery around it, then continues driving for 3 seconds
    fancy_car.brake(time=5.0)
    fancy_car.drive(time=3.0)

    # 6. `SlowCar` brakes for 6 seconds, curious 
    # what `FancyCar` is looking at
    slow_car.brake(time=6.0)

    # 7. `FancyCar` realizes they left their lucky keychain behind and immediately brakes to a full stop, changes to reverse, gases for 20 seconds, 
    # then drives for an additional 30 seconds
    fancy_car.brake(time=1.0)
    fancy_car.gear_change('reverse')
    fancy_car.gas(time=10.0)

    # 8. `SlowCar` feels lonely (now that both cars have left it behind), 
    # comes to a full stop, then turns off its engine
    slow_car.turn_off()

    # 9. After realizing headlights aren't that useful while going 
    # in reverse, `FancyCar` turns off its lights
    fancy_car.toggle_headlights()

    # 10. `FastCar`, all the while, continues driving for another 30 seconds, gasses 20 seconds, 
    # and drives an addition 60 seconds
    fast_car.drive(time=30.0)
    fast_car.gas(time=20.0)
    fast_car.drive(time=60.0)

    # 11. All three cars check their dashboards
    print('\n')
    fast_car.check_dashboard()
    print('\n')
    slow_car.check_dashboard()
    print('\n')
    fancy_car.check_dashboard()
    print('\n')

    # 12. `FancyCar` honks its horn twice, 
    # celebrating that it found its lost keychain
    fancy_car.horn()
    fancy_car.horn()

    # 13. `SlowCar`, starts to get cold in the infinite nothingness. 
    # It turns on its engine again, turns on its lights, gases for 4 seconds, and 
    # then drives for 2000 seconds into the inifinite beyond
    slow_car.turn_on()
    slow_car.toggle_headlights()
    slow_car.gas(time=4.0)
    slow_car.drive(time=2000.0)

    # 14. `SlowCar` checks its dashboard
    print('\n')
    slow_car.check_dashboard()

if __name__ == '__main__':
    main()