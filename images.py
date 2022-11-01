import numpy as np
from matplotlib import pyplot as plt
import io


CMAP_STYLES = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
               'GnBu', 'PuBu', 'YlGnBu', 'BuGn', 'YlGn', 'binary', 'gray', 'bone', 'pink', 'summer', 'hot', 'afmhot',
               'gist_heat', 'copper']


def get_image(size_x: int, size_y: int, style_code: int = None, noisy: bool = False, iter: int = 200):
    """
    Get random cubic art image as BytesIO
    :param size_x: integer
        X size of the image
    :param size_y: integer
        Y size of the image
    :param style_code: integer
        Color style code to apply (valid codes: [0-24]).
        If the given value out of range or not provided, then a random style code will be used.
    :param noisy: boolean
        Produce a clean or noisy output, the default is False.
    :param iter: integer
        Number of iterations (the number of rectangles on result image), the default value is 200.

    :return: BytesIO
        Generated PNG image as BytesIO
    """

    if any([size_x < 1, size_y < 1, iter < 1]):
        raise ValueError("The parameters 'size_x', 'size_y', and 'iter' must be positive and greater than equal to 1")

    image_size = (size_y, size_x)
    if noisy:
        img_array = np.random.triangular(0, 2, 3, image_size)
    else:
        img_array = np.full(image_size, 10)

    try:
        cmap = CMAP_STYLES[style_code]
    except (IndexError, TypeError):
        cmap = CMAP_STYLES[np.random.randint(0, len(CMAP_STYLES))]

    for i in range(iter):
        r01 = np.random.randint(0, size_y)
        r02 = np.random.randint(r01, size_y)
        r11 = np.random.randint(0, size_x)
        r12 = np.random.randint(r11, size_x)

        img_array[r01:r02, r11:r12] = img_array[r01:r02, r11:r12] + 1

    output = io.BytesIO()
    plt.imsave(output, img_array, cmap=cmap)

    return output
