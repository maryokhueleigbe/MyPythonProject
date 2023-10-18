myfruit = ("banana", "apples", "guava", "cherry");
a = list(myfruit)
a.append("cucumber");
myfruit = tuple(a)
print(myfruit);
b = list(myfruit)
b.insert(1, "pineapple");
myfruit = tuple(b);
print(myfruit);
c = list(myfruit);
c[1] = "mango";
myfruit = tuple(c);
print(myfruit);