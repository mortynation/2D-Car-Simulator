# Car Simulator

__What it does?__

Simulates real life behaviour of a car but with few stipulations in terms of its functioning. User get to choose the type of car or can modify the car's features to their desired values which are automatically fed to functions developed to yield a car's dahsboard related information. 

__Features, Functions and Stipulations__

Before starting the discussion about features and functions, it should be understood that the car only travel in straight line, can't turn but can move back and forth and any effect due to wind resistance can be negated.

There are three types of cars we will be dealing with here - _FastCar_, _SlowCar_, and _FancyCar_. Each of them will travel on their own roads and will share the features and most of the basic functionalities of an average car.

An average will contain following features:
 1. `car_type` - Stores the car type
 2. `speed` - Stores the car's speed
 3. `acceleration` - Stores the car's acceleration (constant)
 4. `deceleration` - Stores the car's deceleration (constant)
 5. `distance` - Stores the distance travelled by the car
 6. `enigne_on` - Stores the enigne status(True - on, False - off)
 7. `headlights_on` - Stores the headlight status(True - on, False - off)
 8. `direction` - Stores the direction the car is moving in or the gear status
 9. `home` - Stores the home's distance or from where the engine is turned on
 10. `max_speed` - Stores the maximum speed allowed by the car(constant)
 11. `dist_from_home` - Stores the car's distance from home

 Following are the standard values for the features of an average car that are going to stay constant over the journey and their modifications for respective car types:
 
| Feature          | AverageCar | FastCar | SlowCar | FancyCar |
| ---------------- | :--------: | :-----: | :-----: | :------: |
| Max Speed        |  50 m/sec  |   3x    |  .75x   |    2x    |
| Acceleration     |  5 m/sec^2 |   2x    |  .75x   |    1x    |
| Brake Efficiency |  10 m/sec^2|   1x    |   2x    |    1x    |


An average car will contain following functions:
1. `turn_on` - Enables gas, drive and brake, and initialises current travelled distance as home.
2. `turn_off` - Disables gas, drive and brake, and can be turned off only when speed is 0.
3. `gas` - Increases speed of the car for given time, speed cannot exceed the specified value and doesn't affect distance.
4. `brake` - Decreases speed of the car for given time if it is greater than 0 and doesn't affect distance.
5. `drive` - Increases distance of the car for the given time, continues moving the car in the current direction and doesn't affect acceleration.
6. `toggle_headlights` - Toggles the headlight whenever called, eg: If the headlight is ON, calling the method would turn OFF the headlight.
7. `check_dashboard` - Retrieves and displays information like car type, engine status, headlights status, current speed, odomoeter value, distance from home and current gear status.

Also few helper functions were defined to help in retrieving the current status or values of the features.

In addition to these functions _FancyCar_ will have its own set of fuctions to facilitate on honk and gear change:
1. `gear_change` - Changes car's gear by changing its direction when speed is 0.
2. `horn` - Honks by saying 'beep beep'.

__Repo Contents__

This project contains 7 files including `README.md` which are namely `base_car.py`, `fast_car.py`, `slow_car.py`, `fancy_car`, `test.py` and `main.py`. Let's briefly go through the details about the need of presence of these files:

1. `base_car.py` - This file contains an average car's features and the functions which can make use of these features to generate dahsboard related information.
2. `fast_car.py` - Fast car essentially contains the features of an average car, so, the file contains methods to inherit those features and modifications in features maximum speed, acceleration and deceleration.
3. `slow_car.py` - Slow car essentially contains the features of an average car, so, the file contains methods to inherit those features and modifications in features maximum speed, acceleration and deceleration.
4. `fancy_car.py` - Fancy car essentially contains the features of an average car, so, the file contains methods to inherit those features, modifications in maximum speed, acceleration, deceleration features and drive function, and includes exclusive functions to facilitate gear change and honk.
5. `test.py` - This file contains implementation of test cases for testing the functions, which was done using pytest package.
6. `main.py` - This file contains methods of simulating few of the predefined actions.

__Testing the functionalities__

Predefined test cases were framed and implemented using pytest package. Type of car to be tested can be changed by changing the value of object `car` to the respective car type's class (`FastCar()`, `SlowCar()` or `FancyCar()`) that have been already imported. Functions can be called inside the test functions with desired input values to test various test cases and edge cases. 

__Prerequisites__

Latest version of Python is required to be installed and using an IDE like Visual Studio Code would make the execution and editing process more easy.

__Instructions to run the simulation__

1. Actions specific to a car type can be performed by calling the required functions at the bottom of the respective car type's python file.

Example: 
Class to be called has already been stored in an object.
```
type_car.turn_on()
type_car.toggle_headlights()
type_car.gas(time=4)
type_car.drive(time=3)
```

To see the output, the file can be directly executed through an IDE by triggering the `Run Python File` provision or through command line by first entering the directory where these files are located and typing python followed by the path to the python file.

Example: 
```
cd 'Path to Directory'
python3 fast_car.py
```

2. To test the car's functionalities go to the `tests.py` file and under the function `car_type` specify the required car type to be tested by assigning car's class(`FastCar()`, `SlowCar()` or `FancyCar()`) to the object `car`. To execute the tests enter the directory where these files are located and run the command `pytest tests.py`

Example:
```
cd 'Path to Directory'
pytest tests.py
```

3. To execute few of the predefined actions to understand each of the car type's functioning, execute the `main.py` directly from the command line or through an IDE.

Example:
```
cd 'Path to Directory'
python3 main.py
```
