import re
from datetime import date
from rest_framework import serializers


def validate_decimals(value):
    if not re.match('[0-9]*(\.[0-9]{2})?$', value):
        raise serializers.ValidationError(
            '%(value)s is not an integer or a float  number')
    else:
        return float(value)


def date_validation(d):
    regex = "(?:0[1-9]|[12][0-9]|3[01])[-](?:0[1-9]|1[012])[-](?:19\d{2}|20[01][0-9]|20[2][0-2])"
    if re.match(regex, d):
        d1, m1, y1 = d.split('-')
        return date(int(y1), int(m1), int(d1))
    else:
        raise ValueError("It's not date.")




