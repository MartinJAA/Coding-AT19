import _pickle as pickle
import ast

my_dict2 = "{'gluglu': 'yoilNuzw7vqyuqfe', 'gloglo': 'pXrdkl7jegt', 'glegle': 'paLrjkfh6'}"
my_dict = {"reddit": "bMibgis2vu", "google": "mDahag2mxjasrw", "facebook": "fNqqkb2ermcexftn"}
# print(my_dict2.split())
# with open('password.txt', 'w') as file:
#      a = file.write(pickle.dumps(my_dict))
#      print(a)

# reading the data from the file
with open('password.txt') as f:
    data = f.read()

print("Data type before reconstruction : ", type(data))

# reconstructing the data as a dictionary
d = ast.literal_eval(data)

print("Data type after reconstruction : ", type(d))
print(d)
b = d.get("google")
print(b)

