"""
    If you are using django.contrib.auth, you will have a table called auth_user.

    It will have fields as username, first_name, last_name and more.

    Say you want to fetch all users with id NOT < 5.

    You need a NOT operation.

    Django provides two options.

        1. exclude(<condition>)
        2. filter(~Q(<condition>))

    Our SQL query for the above condition will look something like:

        SELECT id, username, first_name, last_name, email FROM auth_user WHERE NOT id < 5;
"""
from django.db.models import Q
queryset = User.objects.filter(~Q(id__lt=5))

"""
    :return
    <QuerySet [<User: Ritesh>, <User: Billy>, <User: Radha>, <User: sohan>, <User: Raghu>, <User: rishab>]>
"""