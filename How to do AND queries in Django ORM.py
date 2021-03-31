"""
    If you are using django.contrib.auth, you will have a table called auth_user.
    It will have fields as username, first_name, last_name and more.
    You would frequently need to want to perform AND operation, to find querysets which match multiple criteria.
    Say you want to find users with firstname starting with ‘R’ AND last_name starting with ‘D’.

    Django provides three options.

    1. filter(<condition_1>, <condition_2>)
    2. queryset_1 & queryset_2
    3. filter(Q(<condition_1>) & Q(<condition_2>))

    Our SQL query for the above condition will look something like:
        SELECT username, first_name, last_name, email FROM auth_user WHERE first_name LIKE 'R%' AND last_name LIKE 'D%';

"""
from django.db.models import Q
# No.1
# The default way to combine multiple conditions in filter is AND, so you can just do.
queryset_1 = User.objects.filter(first_name__startswith='R', last_name__startswith='D')

"""
    :return
    queryset_1
        <QuerySet [<User: Ricky>, <User: Ritesh>, <User: rishab>]>
"""

# No.2
# Alternatively, you can explicitly use the & operator on querysets.
queryset_2 = User.objects.filter(first_name__startswith='R') & User.objects.filter(last_name__startswith='D')

"""
    :return
    str(queryset_2.query)
        'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE ("auth_user"."first_name"::text LIKE R% AND "auth_user"."last_name"::text LIKE D%)'
"""

# No.3
# Alternatively, you can explicitly use the & operator on querysets.
queryset_3 = User.objects.filter(Q(first_name__startswith='R') & Q(last_name__startswith='D'))
