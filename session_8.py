#----------------------- Task 8 -----------------------------
print("\n----------------------- Task 8 -----------------------------\n")

# Q_1 "Use Different Dunder methods"
class Btech:
    def __init__(self, fname, lname, ttmarks):
        self.fname = fname
        self.lname = lname
        self.ttmarks = ttmarks

    def __add__(self, newMarks):
        return Btech(self.fname, self.lname, self.ttmarks + newMarks)

    def __str__(self):
        return f"Hi, {self.fname} {self.lname}!"

    def __repr__(self):
        return f"Hey, {self.fname} {self.lname} this is of repr! :)"

    def __len__(self):
        return len(self.fname) + len(self.lname)

# Example
print("-- Init Method --")
ratn = Btech("Ratn", "Govindam", 78)
print(ratn) 
print("-- Add Method --")
print(f"Total marks: {ratn.ttmarks}")
ratn = ratn + 12
print(f"Updated total marks: {ratn.ttmarks}")

print("-- Length Method --")
print(f"Total length of name: {len(ratn)}")

print("-- Dictonary Attribute --")
ratn.__dict__['lname'] = "Pandey"
print(ratn.__dict__)

print("-- Repr method --")
print(repr(ratn))
