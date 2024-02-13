from rover import Rover, Coordonnees, CardinalVector


def test_rover_10_N():
    rover = Rover(Coordonnees(1, 0), "N")

    assert rover.position == Coordonnees(1, 0)
    assert rover.direction == "N"


def test_rover_avance():
    # Given
    rover = Rover(Coordonnees(1, 0), "N")
    # When
    rover.accept("f")
    # Then
    assert rover.position == Coordonnees(1, 1)
    assert rover.direction == "N"


def test_translate_2_4_direction_EST():
    assert Coordonnees(2, 4).translate(CardinalVector.EST) == Coordonnees(3, 4)


def test_translate_2_4_direction_NORD():
    assert Coordonnees(2, 4).translate(CardinalVector.NORD) == Coordonnees(2, 5)  # noqa


def test_rover_recule():
    # Given
    rover = Rover(Coordonnees(1, 0), "N")
    # When
    rover.accept("b")
    # Then
    assert rover.position == Coordonnees(1, -1)
    assert rover.direction == "N"
