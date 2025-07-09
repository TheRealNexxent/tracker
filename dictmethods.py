dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
}
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())
dictionary.update({"name": "Divy", "Is Employed": True})
print(dictionary)
print(dictionary.get("abc"))

#Now, the difference between print(dictionary["abc"]) and print(dictionary.get("abc")) is that the first will throw an error if the key does not exist, while the second will return None.
# This is useful for checking if a key exists without raising an error.

