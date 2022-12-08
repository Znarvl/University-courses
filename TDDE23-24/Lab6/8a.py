"""
Bara funktioner från labb 8a
Docstrings känns överflödiga för det har beskrivits innan
men annars ge oss komplettering
"""
def start_time(ts):

    ensure(ts, is_time_span)
    return strip_tag(ts)[0]

def end_time(ts):

    ensure(ts, is_time_span)
    return strip_tag(ts)[1]

def overlap(ts1, ts2):
    # Violates abstraction layers (etc).
    ensure(ts1, is_time_span)
    ensure(ts2, is_time_span)
    min1 = latest_time(start_time(ts1), start_time(ts2))
    min2 = earliest_time(end_time(ts1), end_time(ts2))
    return new_time_span(min1, min2)

def new_duration(hour, minute):

    ensure(minute, is_minute)
    ensure(hour, is_hour)
    return attach_tag('duration', (new_hour(get_integer(hour) + \
            get_integer(minute) // 60), new_minute(get_integer(minute) % 60)))


def length_of_span(ts):

    mins = get_integer(get_minute(end_time(ts))) + \
            get_integer(get_hour(end_time(ts))) * 60 - \
            get_integer(get_minute(start_time(ts))) - \
            get_integer(get_hour(start_time(ts))) * 60
    return new_duration(0, mins)
