print('hoi')
print('hi')
c=4

class B:
    def running(self):
        print("it is running")

r = B()
r.running()

a = 6
s = B()
print(c)

print(a)

a -= 7
g = B()
g.running()

print(a)
a = 5
print(a)
s.running()


f = open("start.txt", "r")
print(f.read())