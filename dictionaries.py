# my_name={
#     "name":"manjri",
#     "age":20,
#     "course":"btech cse"
#     }
# print(my_name.keys())
# keys=list(my_name.keys())
# print(keys)



students=[
    {"name":"Manjri","marks":80},
    {"name":"kriya","marks":90},
    {"name":"madhu","marks":85},

]
for s in students:
    if s["marks"]>=60:
        print(s["name"])