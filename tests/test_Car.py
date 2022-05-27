from Car import Car


def test_car_brake():
    car = Car(0)
    car.brake()
    assert car.speed == 0


def test_accelerate():
    car = Car(50)
    car.accelerate()
    assert car.speed == 55
