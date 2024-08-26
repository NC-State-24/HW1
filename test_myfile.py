from myfile import sum_list, count

def test_sum_list():
    test=[i for i in range(1,10)]
    assert sum_list(test) == 45  # This should pass

def test_count():
    test=[i for i in range(1,10)]
    assert count(test) == 9  # This should fail (it should be 9)