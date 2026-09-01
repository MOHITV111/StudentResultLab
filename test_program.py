from app import calculate_result


def test_calculate_result_A():
    total, grade = calculate_result(90, 90, 90)
    assert total == 270
    assert grade == "A"


def test_calculate_result_B():
    total, grade = calculate_result(80, 80, 80)
    assert total == 240
    assert grade == "B"


def test_calculate_result_C():
    total, grade = calculate_result(60, 60, 60)
    assert total == 180
    assert grade == "C"


def test_calculate_result_F():
    total, grade = calculate_result(50, 50, 50)
    assert total == 150
    assert grade == "F"