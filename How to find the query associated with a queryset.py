"""
    Sometime you want to know how a Django ORM makes our queries execute or what is the corresponding SQL of the code you are writing.

    This is very straightforward.

    You can get str of any queryset.query to get the sql.

"""

queryset = Event.objects.all()
str(queryset.query)
"""
    :return 
    SELECT "events_event"."id", "events_event"."epic_id",
    "events_event"."details", "events_event"."years_ago"
    FROM "events_event"
"""

queryset = Event.objects.filter(years_ago__gt=5)
str(queryset.query)

"""
    :return
    SELECT "events_event"."id", "events_event"."epic_id", "events_event"."details",
    "events_event"."years_ago" FROM "events_event"
    WHERE "events_event"."years_ago" > 5
"""