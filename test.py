import images
import unittest


class Test(unittest.TestCase):

    def mass_generate_images(self):
        for i in range(25):
            img = images.get_image(1024, 768, style_code=i, noisy=False, iter=200)
            with open(f"output/{i}.png", "wb") as f:
                f.write(img.getbuffer())

    def raise_value_error(self):
        self.assertRaises(ValueError, images.get_image, size_x=10, size_y=10, iter=0)
        self.assertRaises(ValueError, images.get_image, size_x=10, size_y=-1, iter=10)
        self.assertRaises(ValueError, images.get_image, size_x=-2, size_y=10, iter=10)


if __name__ == '__main__':
    unittest.main()