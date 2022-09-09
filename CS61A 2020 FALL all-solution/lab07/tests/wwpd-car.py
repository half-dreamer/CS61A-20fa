test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.model
          d44fbfeedd5748e8ed04de29de968251
          # locked
          >>> deneros_car.gas = 10
          >>> deneros_car.drive()
          08adfbe4efff8d65757aa6e3130e95d6
          # locked
          >>> deneros_car.drive()
          ed7e31d39fdaefb22a23971c5b0eb43d
          # locked
          >>> deneros_car.fill_gas()
          73199fd3939cadd5e1e581b76e26a9e9
          # locked
          >>> deneros_car.gas
          e1b5abca0ce46c01fbc9ffe5da884d06
          # locked
          >>> Car.gas
          cf3b881608904e51c384abfbd72a7cc8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = Car('Tesla', 'Model S')
          >>> deneros_car.wheels = 2
          >>> deneros_car.wheels
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> Car.num_wheels
          f2991d685f624ad59b79213e20800653
          # locked
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          ed7e31d39fdaefb22a23971c5b0eb43d
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          ed7e31d39fdaefb22a23971c5b0eb43d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = MonsterTruck('Monster', 'Batmobile')
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          beba7598767b3ddfeb4b0163408184fa
          8a7be733d5923219ef98f4d3a98c169c
          # locked
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          8a7be733d5923219ef98f4d3a98c169c
          # locked
          >>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          beba7598767b3ddfeb4b0163408184fa
          8a7be733d5923219ef98f4d3a98c169c
          # locked
          >>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
