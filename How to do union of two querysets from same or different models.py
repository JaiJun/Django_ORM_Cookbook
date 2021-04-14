"""
    The UNION operator is used to combine the result-set of two or more querysets.

    The querysets can be from the same or from different models.

    When they querysets are from different models, the fields and their datatypes should match.

    Let’s continue with our auth_user model and generate 2 querysets to perform union operation
"""

# >>> q1 = User.objects.filter(id__gte=5)
# >>> q1
# <QuerySet [<User: Ritesh>, <User: Billy>, <User: Radha>, <User: sohan>, <User: Raghu>, <User: rishab>]>
# >>> q2 = User.objects.filter(id__lte=9)
# >>> q2
# <QuerySet [<User: yash>, <User: John>, <User: Ricky>, <User: sharukh>, <User: Ritesh>, <User: Billy>, <User: Radha>, <User: sohan>, <User: Raghu>]>
# >>> q1.union(q2)
# <QuerySet [<User: yash>, <User: John>, <User: Ricky>, <User: sharukh>, <User: Ritesh>, <User: Billy>, <User: Radha>, <User: sohan>, <User: Raghu>, <User: rishab>]>
# >>> q2.union(q1)
# <QuerySet [<User: yash>, <User: John>, <User: Ricky>, <User: sharukh>, <User: Ritesh>, <User: Billy>, <User: Radha>, <User: sohan>, <User: Raghu>, <User: rishab>]>

"""
    The union operation can be performed only with the querysets having same fields and the datatypes. 
    
    Hence our last union operation encountered error. 
    
    You can do a union on two models as long as they have same fields or same subset of fields.
    
    Since "Hero" and "Villain" both have the name and gender, we can use "values_list" to limit the selected fields then do a union.
"""

# Hero.objects.all().values_list("name", "gender").union(Villain.objects.all().values_list("name", "gender"))

"""
    This would give you all "Hero" and "Villain" objects with their name and gender.
"""