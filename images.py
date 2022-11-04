import numpy as np
from matplotlib import pyplot as plt
import io


def get_image(size_x: int = 500, size_y: int = 500, style_code: int = None, noisy: bool = False, iter: int = 200):
    """
    Get random cubic art image as BytesIO
    :param size_x: integer
        Length of the image in pixels, default is 500
    :param size_y: integer
        Height of the image in pixels, default is 500
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

    cmap_styles = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu',
                   'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'BuGn', 'YlGn', 'binary', 'gray', 'bone', 'pink', 'summer',
                   'hot', 'afmhot', 'gist_heat', 'copper']

    if any([size_x < 1, size_y < 1, iter < 1]):
        raise ValueError("The parameters 'size_x', 'size_y', and 'iter' must be positive and greater than equal to 1")

    image_size = (size_y, size_x)
    if noisy:
        img_array = np.random.triangular(0, 2, 3, image_size)
    else:
        img_array = np.full(image_size, 10)

    try:
        cmap = cmap_styles[style_code]
    except (IndexError, TypeError):
        cmap = cmap_styles[np.random.randint(0, len(cmap_styles))]

    for i in range(iter):
        # Random generated coordinates of a rectangle:
        p1_start = np.random.randint(0, size_y)
        p1_end = np.random.randint(p1_start, size_y)
        p2_start = np.random.randint(0, size_x)
        p2_end = np.random.randint(p2_start, size_x)

        img_array[p1_start:p1_end, p2_start:p2_end] = img_array[p1_start:p1_end, p2_start:p2_end] + 1

    output = io.BytesIO()
    plt.imsave(output, img_array, cmap=cmap)

    return output
