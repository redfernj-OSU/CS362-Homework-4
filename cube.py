def volume(x, y, z):

    if isinstance(x, int) is False or isinstance(y, int) is False or isinstance(z, int) is False:
        raise TypeError('You must input a number.')

    if x < 0 or y < 0 or z < 0:
        raise ValueError('Your input must be positive.')

    return x * y * z
