myfood = {
    "fruits": "apples",
    "veggies": "spinach",
    "protein": "fish"
}
print(myfood["veggies"]);
a = myfood.get("protein");
print(a);
myfood["veggies"] = "carrot";
print(myfood);
print(myfood["veggies"]);
myfood["beverage"] = "milo";
print(myfood);
myfood.update({"butter": "blueband"})
print(myfood);
myfood.pop("veggies");
print(myfood);