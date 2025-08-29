# This file was written by me for CS-2420 when were learning different data structures. 
# This is the basic version that just uses a list

class Student:

    def __init__(self, name, ssn, email, age):
        self.name = name
        self.ssn = ssn
        self.email = email
        self.age = age
        return

    def getAge(self):
        return self.age

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.ssn == other.ssn
        return False
    
    def __str__(self):
        string = self.name 
        string += "  " + str(self.ssn)
        string += "  " + str(self.email) 
        string += "  " + str(self.age)
        return string

class Container:
    
    def __init__(self):
        self.mList = []
        return 
    
    def Add(self,item): # returns false on duplicate
        if self.Exists(item):
            return False
        else:
            self.mList.append(item)
            return True
    
    def Exists(self,other):
        for item in self.mList:
            if item == other:
                return True
        return False
        
    def Size(self):
        return len(self.mList)
    
    def Delete(self, student): # returns false if not there
        for i, item in enumerate(self.mList):
            if student == item:
                self.mList.pop(i)
                return True
        return False
    
    def Retrieve(self,item):
        for student in self.mList:
            if student == item:
                return student
        return None
    
    def __iter__(self):
        return iter(self.mList)
    



# def add(c):
#     print("\n----------- Insert ------------")
#     t1 = time.time()
#     fin = open("namesFiles/FakeNames.txt", "r")
#     for line in fin:
#         words = line.split()
#         name = words[0] + " " + words[1]
#         s = Student(name, words[2], words[3], words[4])
#         ok = c.Add(s)
#         if not ok:
#             print("Duplicate Found:", s)
        
#     t2 = time.time()
#     print("Total add time was", round(t2-t1), "seconds.")
#     fin.close()



# def traverse(c):
#     print("\n----------- Traverse ------------")
#     t1 = time.time()
#     totalAge = 0
#     for student in c:
#         age = int(student.getAge())
#         totalAge += age
#     print("The average age of all students is", round(totalAge / c.Size(),4))
#     t2 = time.time()
#     print("Total traverse time was", round(t2-t1,3), "seconds.\n")

# def delete(c):
#     print("\n----------- Delete ------------")
#     fin = open("namesFiles/DeleteNames.txt", "r")
#     t1 = time.time()
#     count = 0
#     for line in fin:
#         fake_student = Student("",line.strip(),"","")
#         ok = c.Delete(fake_student)
#         if not ok:
#             print("could not delete:", fake_student)
#         else:
#             count += 1

#     t2 = time.time()
#     print("Total delete time was", round(t2-t1), "seconds.\nTotal deletions:", count)
#     fin.close()

# def retrieve(c):
#     print("\n----------- Retrieve ------------")
#     fin = open("namesFiles/RetrieveNames.txt", "r")
#     t1 = time.time()
#     totalAge = 0
#     count = 0
#     for line in fin:
#         ssn = line.strip()
#         fake_student = Student("", ssn,"","")
#         s2 = c.Retrieve(fake_student)
#         if s2 is not None:
#             totalAge += int(s2.getAge())
#             count += 1
#         else:
#             print("could not retrieve", fake_student)
        
#     t2 = time.time()
#     avg = totalAge / count
#     print("Average age of retrieved students is", round(avg,4))
#     print("Total retrieve time was", round(t2-t1), "seconds.\n")
#     fin.close()



    
# def main():
#     overallStart = time.time()
#     print("")
#     c = Container()
#     add(c)
#     traverse(c)
#     delete(c)
#     retrieve(c)
#     overallEnd = time.time()
#     print("\n----------- Overall ------------")
#     print("Overall time was", round(overallEnd-overallStart), "seconds.\n")
#     return


# main()


# shortFake = [
#     "GREGORY DON 574-28-3634 DON.GREGORY@FakeSchool.edu 44",
#     "ENGLAND CORY 136-95-9728 CORY.ENGLAND@FakeSchool.edu 51",
#     "KNIGHT WOODROW 334-15-4911 WOODROW.KNIGHT@FakeSchool.edu 46",
#     "SILVA DAVID 482-25-3505 DAVID.SILVA@FakeSchool.edu 38",
#     "RUSSELL DANIELLE 247-09-6149 DANIELLE.RUSSELL@FakeSchool.edu 55",
#     "BUSH JUSTIN 451-30-3555 JUSTIN.BUSH@FakeSchool.edu 36",
#     "MILLS GILBERTO 122-15-1924 GILBERTO.MILLS@FakeSchool.edu 29",
#     "MCDONALD WILLIAM 102-06-4090 WILLIAM.MCDONALD@FakeSchool.edu 45",
#     "HOWARD LOIS 102-06-4090 LOIS.HOWARD@FakeSchool.edu 55",
#     "ACEVEDO WILLIE 463-89-5218 WILLIE.ACEVEDO@FakeSchool.edu 38"
# ]
# shortDelete = [
#     "574-28-3634",
#     "136-95-9728",
#     "334-15-4911",
#     "482-25-3505",
#     "247-09-6149",
#     "451-30-3555",
#     "122-15-1924",
#     "102-06-4090",
#     "102-06-4090",
#     "463-89-5218"
# ]
# shortRetrieve = [
#     "574-28-3634",
#     "136-95-9728",
#     "334-15-4911",
#     "482-25-3505",
#     "247-09-6149",
#     "451-30-3555",
#     "122-15-1924",
#     "102-06-4090",
#     "102-06-4090",
#     "463-89-5218"
# ]