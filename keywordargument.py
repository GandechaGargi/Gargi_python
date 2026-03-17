def student_info(name, age, city):
    print("Name : ", name)
    print("Age : ", age)
    print("City : ", city)

student_info(age=18, city="Rajkot", name="Ravi")


def display(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

display(1, c=3, b=2)


# Create function of simple Interest
def simple_interest(p: float, r: int, t: float):
    si = (p * r * t) / 100
    print("simple Interest : ", si)

simple_interest(p=10000, t=2, r=1.5)
simple_interest(t=1.5, p=15000, r=2)