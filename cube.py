import pytest


def volume(x, y, z):
    return x * y * z

def test_answer():
    assert volume(5, 5, 5) == 125


# def main():
#     x = input("x: ")
#     y = input("y: ")
#     z = input("z: ")

#     print("volume: ", volume(int(x), int(y), int(z)))


# if __name__ == '__main__':
#     main()