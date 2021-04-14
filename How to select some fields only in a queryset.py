"""
    The auth_user model has a number of fields in it.

     But sometimes, you do not need to use all the fields.

     In such situations, we can query only desired fields.

     Django provides two ways to do this

    1. values and values_list methods on queryset.
    2. only_method

"""

"""
    Say, we want to get first_name and last_name of all the users whose name starts with R. 
    
    You do not want the fetch the other fields to reduce the work the DB has to do.
"""

# >>> queryset = User.objects.filter(first_name__startswith='R').values('first_name', 'last_name')
# >>> queryset
# <QuerySet [{'first_name': 'Ricky', 'last_name': 'Dayal'},
            # {'first_name': 'Ritesh', 'last_name': 'Deshmukh'},
            # {'first_name': 'Radha', 'last_name': 'George'},
            # {'first_name': 'Raghu', 'last_name': 'Khan'},
            # {'first_name': 'Rishabh', 'last_name': 'Deol'}]

"""
    The output will be list of dictionaries.
    
    Alternatively, you can do
"""

# >>> queryset = User.objects.filter(first_name__startswith='R').only("first_name", "last_name")


"""
    The only difference between only and values is only also fetches the id.
"""