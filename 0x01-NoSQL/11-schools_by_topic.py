#!/usr/bin/env python3
""" module doc"""


def schools_by_topic(mongo_collection, topic):
    """ returns a specif topic to be searched """

    return mongo_collection.find({"topics":topic})
