# we can concatenate variable multiple ways, the most common being;
'''
x = "variable"
print("string" + x)
or
print("string {}".format(x))
or
print(f"string {x}")
'''

# using these 3 ways, we can now work on our madlibs;

adj = input("Adjective: ")
adj2 = input("Another Adjective: ")
typbrd = input("Type of Bird: ")
roomhuse = input("Room of a House: ")
vrbpt = input("Verb (Past Tense): ")
vrb = input("Verb: ")
name = input("Name: ")
noun = input("Noun: ")
lqud = input("Liquid: ")
vrbing = input("Verb (ing): ")
bdyprtplrl = input("Body Part (Plural): ")
nounplrl = input("Noun (Plural): ")
vrbing2 = input("Verb (ing): ")
noun2 = input("Noun: ")

madlib = f"It was a {adj}, cold Novemebr day. I woke up to the {adj2} smell of {typbrd} roasting in the {roomhuse} downstairs. \
I {vrbpt} down the stairs to see if i could help {vrb} the dinner. My mom said, 'see if {name} needs a fresh {noun}'. So i carried \
a tray of glasses full of {lqud} into the {vrbing} room. When i got there, i couldnt believe my {bdyprtplrl}! There were \
{nounplrl} {vrbing2} on the {noun2}!"

print(madlib)