"""
    Django allows using SQL subqueries.

    Let’s start with something simple,

    We have a UserParent model which has OnetoOne relation with auth user.

    We will find all the UserParent which have a UserParent.

"""

# >>> from django.db.models import Subquery
# >>> users = User.objects.all()
# >>> UserParent.objects.filter(user_id__in=Subquery(users.values('id')))
# <QuerySet [<UserParent: UserParent object (2)>, <UserParent: UserParent object (5)>, <UserParent: UserParent object (8)>]>

"""
    Now for something more complex. 
    
    For each Category, we want to find the most benevolent Hero.
    
"""

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


class Hero(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    benevolence_factor = models.PositiveSmallIntegerField(
        help_text="How benevolent this hero is?",
        default=50
    )

"""
    You can find the most benevolent Hero like this
    
    hero_qs = Hero.objects.filter(category=OuterRef("pk")).order_by("-benevolence_factor")
    We are ordering the Hero object by benevolence_factor in DESC order, and using category=OuterRef("pk") to declare that we will be using it in a subquery.
"""

"""
    Category.objects.all().annotate(most_benevolent_hero=Subquery(hero_qs.values('name')[:1]))
    Then we annotate with most_benevolent_hero=Subquery(hero_qs.values('name')[:1]), to get use the subquery with a Category queryset.
    The hero_qs.values('name')[:1] part picks up the first name from subquery.
"""
#

