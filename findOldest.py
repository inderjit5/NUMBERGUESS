#take input of age from 3 people
#determine the oldest and youngest
inderjit = int(input("age of first person"))
ritesh = int(input("age of second person"))
abhishek = int(input("age of third person"))

if inderjit>ritesh and inderjit>abhishek:
    print("oldest is ", inderjit)
elif ritesh>inderjit and ritesh>abhishek:
    print("oldest is", ritesh)
elif abhishek>inderjit and abhishek>ritesh:
    print("oldest is", abhishek)
else: 
    print("inderjit,ritesh,abhishek having same age") 
