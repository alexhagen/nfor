import nfor

def test_two_var():
    sum_product = 0
    for variables in nfor.nfor([[1, 2, 3], [2, 3, 4]]):
        x, y = variables
        sum_product += x * y
    assert sum_product == (1*2 + 1*3 + 1*4 + 2*2 + 2*3 + 2*4 + 3*2 + 3*3 + 3*4)

if __name__ == "__main__":
    test_two_var()