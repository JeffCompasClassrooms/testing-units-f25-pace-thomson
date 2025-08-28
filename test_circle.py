import unittest
from circle import *

class test_circle(unittest.TestCase):
    def test_init_validRadius(self):
        circ = Circle(5)
        self.assertIsInstance(circ, Circle)
        self.assertEqual(circ.mRadius, 5)

    def test_init_invalidRadius(self):
        circ = Circle(-5)
        self.assertIsInstance(circ, Circle)
        self.assertNotEqual(circ.mRadius, -5)
    
    def test_getRadius(self): 
        circ = Circle(5)
        self.assertEqual(circ.getRadius(), 5)
        self.assertEqual(circ.getRadius(), circ.mRadius)
    
    def test_setRadius_validRadius(self): 
        circ = Circle(0)
        rad = circ.setRadius(5)
        self.assertEqual(circ.mRadius, 5)
        self.assertTrue(rad)

    def test_setRadius_invalidRadius(self): 
        circ = Circle(0)
        rad = circ.setRadius(-10)
        self.assertEqual(circ.mRadius, 0)
        self.assertFalse(rad)

    def test_getArea_not2(self): 
        circ = Circle(4)
        area = circ.getArea()
        self.assertEqual(area, 50.26548245743669)

    def test_getArea_with2(self): 
        circ = Circle(2)
        area = circ.getArea()
        self.assertEqual(area, 12.566370614359172)

    def test_getCircumference(self): 
        circ = Circle(3)
        circumference = circ.getCircumference()
        self.assertEqual(circumference, 2. * math.pi * 3)



if __name__ == "__main__":
    import unittest
    unittest.main()



