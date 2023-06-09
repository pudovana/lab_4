class test_Converter(unittest.TestCase):
    def test_values(self):
        self.assertEqual(calc(100000, 5, 12))
        self.assertEqual(calc(-100000, -1, -2), "Одно или все значения меньше нуля")

    def test_types(self):
        self.assertEqual(calc(100000, 1, "пять"), 'ValueError: не является числом')
        self.assertEqual(calc(100000, 1, [1, 2, 3]), 'TypeError: недопустимое значение')
        self.assertEqual(calc(100000, 1, (1, 2, 3)), 'TypeError: недопустимое значение')
if __name__ == '__main__':
    app.run(debug=True)
