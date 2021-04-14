"""
    Django ORM makes it easy to filter based on fixed values.

    To get all User objects with first_name starting with 'R', you can do User.objects.filter(first_name__startswith='R').

    What if you want to compare the first_name and last name?

    You can use the F object.

    Create some users first.
"""

# In [27]: User.objects.create_user(email="shabda@example.com", username="shabda", first_name="Shabda", last_name="Raaj")
# Out[27]: <User: shabda>
#
# In [28]: User.objects.create_user(email="guido@example.com", username="Guido", first_name="Guido", last_name="Guido")
# Out[28]: <User: Guido>

"""
    Now you can find the users where first_name==last_name
"""

# In [29]: User.objects.filter(last_name=F("first_name"))
# Out[29]: <QuerySet [<User: Guido>]>

"""
    "F" also works with calculated field using annotate.
     
     What if we wanted users whose first and last names have same letter?
     
     You can set the first letter from a string using Substr("first_name", 1, 1), so we do.
"""

# In [41]: User.objects.create_user(email="guido@example.com", username="Tim", first_name="Tim", last_name="Teters")
# Out[41]: <User: Tim>
# In [46]: User.objects.annotate(first=Substr("first_name", 1, 1), last=Substr("last_name", 1, 1)).filter(first=F("last"))
# Out[46]: <QuerySet [<User: Guido>, <User: Tim>]>

"""
    "F" can also be used with __gt, __lt and other expressions.
"""