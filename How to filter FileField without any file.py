"""
    A "FileField" or "ImageField" stores the path of the file or image.

    At the DB level they are same as a CharField.

    So to find FileField without any file we can query as under.
"""

# no_files_objects = MyModel.objects.filter(Q(file='')|Q(file=None))