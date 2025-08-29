import unittest
from student_container import Student, Container

class TestStudent(unittest.TestCase):

    def test_init_validData(self):
        s = Student("Alice", "123", "alice@email.com", 20)
        self.assertEqual(s.name, "Alice")
        self.assertEqual(s.ssn, "123")
        self.assertEqual(s.email, "alice@email.com")
        self.assertEqual(s.age, 20)

    def test_init_returnType(self):
        s = Student("Alice", "123", "alice@email.com", 20)
        self.assertIsInstance(s, Student)

    def test_getAge_normal(self):
        s = Student("Bob", "234", "bob@email.com", 25)
        self.assertEqual(s.getAge(), 25)

    def test_getAge_zero(self):
        s = Student("Zero", "999", "zero@email.com", 0)
        self.assertEqual(s.getAge(), 0)

    def test_getAge_maximum(self):
        s = Student("Old", "888", "old@email.com", 120)
        self.assertEqual(s.getAge(), 120)

    def test_eq_sameSSN(self):
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Bob", "123", "b@email.com", 22)
        self.assertTrue(s1 == s2)

    def test_eq_differentSSN(self):
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Bob", "456", "b@email.com", 22)
        self.assertFalse(s1 == s2)

    def test_eq_nonStudent(self):
        s = Student("Alice", "123", "a@email.com", 20)
        self.assertFalse(s == "NotAStudent")

    def test_eq_none(self):
        s = Student("Alice", "123", "a@email.com", 20)
        self.assertFalse(s == None)

    def test_str_format(self):
        s = Student("Alice", "123", "a@email.com", 20)
        self.assertEqual(str(s), "Alice  123  a@email.com  20")

    def test_str_specialCharacters(self):
        s = Student("O'Connor", "321", "email+test@gmail.com", 30)
        result = str(s)
        self.assertIn("O'Connor", result)
        self.assertIn("email+test@gmail.com", result)


class TestContainer(unittest.TestCase):

    def test_init_empty(self):
        c = Container()
        self.assertEqual(c.Size(), 0)

    def test_init_returnType(self):
        c = Container()
        self.assertIsInstance(c, Container)

    def test_add_validStudent(self):
        c = Container()
        s = Student("Alice", "123", "a@email.com", 20)
        self.assertTrue(c.Add(s))
        self.assertEqual(c.Size(), 1)

    def test_add_duplicateStudent(self):
        c = Container()
        s = Student("Alice", "123", "a@email.com", 20)
        c.Add(s)
        self.assertFalse(c.Add(Student("Bob", "123", "b@email.com", 25)))
        self.assertEqual(c.Size(), 1)

    def test_add_sameNameDifferentSSN(self):
        c = Container()
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Alice", "456", "a2@email.com", 21)
        self.assertTrue(c.Add(s1))
        self.assertTrue(c.Add(s2))
        self.assertEqual(c.Size(), 2)

    def test_exists_true(self):
        c = Container()
        s = Student("Alice", "123", "a@email.com", 20)
        c.Add(s)
        self.assertTrue(c.Exists(s))

    def test_exists_false(self):
        c = Container()
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Bob", "456", "b@email.com", 25)
        c.Add(s1)
        self.assertFalse(c.Exists(s2))

    def test_delete_existing(self):
        c = Container()
        s = Student("Alice", "123", "a@email.com", 20)
        c.Add(s)
        self.assertTrue(c.Delete(s))
        self.assertEqual(c.Size(), 0)

    def test_delete_nonExisting(self):
        c = Container()
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Bob", "456", "b@email.com", 25)
        c.Add(s1)
        self.assertFalse(c.Delete(s2))
        self.assertEqual(c.Size(), 1)

    def test_delete_emptyContainer(self):
        c = Container()
        s = Student("Alice", "123", "a@email.com", 20)
        self.assertFalse(c.Delete(s))

    def test_retrieve_existing(self):
        c = Container()
        s = Student("Alice", "123", "a@email.com", 20)
        c.Add(s)
        self.assertEqual(c.Retrieve(s), s)

    def test_retrieve_nonExisting(self):
        c = Container()
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Bob", "456", "b@email.com", 25)
        c.Add(s1)
        self.assertIsNone(c.Retrieve(s2))

    def test_retrieve_multiple(self):
        c = Container()
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Bob", "456", "b@email.com", 25)
        c.Add(s1)
        c.Add(s2)
        self.assertEqual(c.Retrieve(s2), s2)

    def test_iterate_students(self):
        c = Container()
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Bob", "456", "b@email.com", 25)
        c.Add(s1)
        c.Add(s2)
        students = [s for s in c]
        self.assertEqual(students, [s1, s2])

    def test_add_multipleStudents(self):
        c = Container()
        for i in range(5):
            self.assertTrue(c.Add(Student(f"Student{i}", str(i), f"s{i}@email.com", 18+i)))
        self.assertEqual(c.Size(), 5)

    def test_add_nonStudentObject(self):
        c = Container()
        with self.assertRaises(AttributeError):  # because `Exists` calls == which expects .ssn
            c.Add("NotAStudent")

    def test_add_nonStudentObject(self):
        c = Container()
        # current behavior: non-Student is allowed
        self.assertTrue(c.Add("NotAStudent"))
        self.assertIn("NotAStudent", c.mList)


    def test_delete_reAddStudent(self):
        c = Container()
        s = Student("Alice", "123", "a@email.com", 20)
        c.Add(s)
        c.Delete(s)
        self.assertTrue(c.Add(s))
        self.assertEqual(c.Size(), 1)

    def test_largeNumberStudents(self):
        c = Container()
        for i in range(1000):
            c.Add(Student(f"Student{i}", str(i), f"s{i}@mail.com", 18))
        self.assertEqual(c.Size(), 1000)

    def test_orderPreservation(self):
        c = Container()
        s1 = Student("Alice", "123", "a@email.com", 20)
        s2 = Student("Bob", "456", "b@email.com", 25)
        c.Add(s1)
        c.Add(s2)
        self.assertEqual(list(c), [s1, s2])


if __name__ == "__main__":
    unittest.main()
