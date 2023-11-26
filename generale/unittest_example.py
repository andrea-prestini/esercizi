import unittest


class Food:
    def __init__(self) -> None:
        self.consumed = False

    def consume(self):
        self.consumed = True


class Fruit(Food):
    def __init__(self) -> None:
        super().__init__()
        self.been_cut = False

    def cut(self):
        print("Cut the fruit")
        self.been_cut = True


class Consumer:
    def __init__(self) -> None:
        self.apple = Fruit()
        self.banana = Fruit()

    def consume_food(self):
        food = self.pick_food()
        food.cut()
        print("consuming the food")
        food.consume()

    def pick_food(self):
        return self.apple


class TestConsumer(unittest.TestCase):
    def test_consume_apple(self):
        c = Consumer()
        c.consume_food()
        self.assertTrue(c.apple.consumed, "Expected apple to be consumed")

    def test_consume_cut_the_food(self):
        c = Consumer()
        c.consume_food()
        self.assertTrue(c.apple.been_cut, "Expected apple to be cut")

    def test_pick_food(self):
        c = Consumer()
        food = c.pick_food()
        self.assertEqual(c.apple, food, "Expected apple has been cut")


unittest.main()
