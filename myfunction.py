def maryisi():
    print("I'm a beautiful girl");
maryisi();
def citygirl(mycity):
    print("This is my city " + mycity);
citygirl("Houston");
citygirl("Dallas");
citygirl("Florida");
def myname(firstname, lastname):
    print("This is my firstname: " + firstname + " This is my lastname: " + lastname);
myname("Mary", "Isi");
myname("Collins", "Obi");
myname("Adams", "John");
def myfruits(berry):
    for x in berry:
        print(x);
fruits = ["strawberry", "raspberry", "blackberry", "blueberry"];
myfruits(fruits)
def marynumber(numbers):
    while numbers <= 8:
        print(numbers);
        numbers += 1
marynumber(1)