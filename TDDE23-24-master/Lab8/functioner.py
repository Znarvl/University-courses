def start_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return strip_tag(ts)[0]

def end_time(ts):
    "span->time"
    ensure(ts, is_time_span)
    return strip_tag(ts)[0]


def overlap(ts1, ts2):
    # Violates abstraction layers (etc).
    ensure(ts1, is_time_span)
    ensure(ts2, is_time_span)
    min1 = latest_time(start_time(ts1), start_time(ts2))
    min2 = earliest_time(end_time(ts1), end_time(ts2))

    return new_time_span(min1,min2)

def new_duration(hour, minute):
    "hour x minute -> duration"
    #if mintute exceeds 60
    overflow_hour = get_integer(minute) // 60
    #if mintue exceeds 60min, find true value
    minute = new_minute(get_integer(minute) % 60)
    hour = new_hour(get_integer(hour) + overflow_hour)
    return attach_tag("duration", (hour, minute))

def length_of_span(ts):
    "span -> duration"
    mins = get_integer(get_minute(end_time(ts)))+ \
    get_integer(get_hour(end_time(ts)))*60 -\
     get_integer(get_minute(start_time(ts)))\
     - get_integer(get_hour(start_time(ts)))*60
    return new_duration(0, mins)



def new_time_spans():
    "spans -> new"
    return attach_tag('time_spans', [])

def is_time_spans(object):
    "Python-object -> Bool"
    return get_tag(object) == 'time_spans'

def is_empty_time_spans(object):
    ensure(object,is_time_spans)
    return not strip_tag(object)

def insert_span(time_span,time_spans):
    "time_spans x time_spans -> time_spans"

    ensure(time_span,is_time_span)
    ensure(time_spans,is_time_spans)

    def update(ts):
        if not ts or precedes(start_time(time_span),start_time(ts[0])):
            return [time_span] + ts
        elif is_same_time(start_time(time_span),start_time(ts[0])):
            return [time_span] + ts[1:]
        else:
            return [ts[0]] + update(ts[1:])

    return attach_tag("time_spans",update(strip_tag(time_spans)))


def free_spans(cal_day, start_free_time, end_free_time):
        "calendar_day x time x time -> time_spans"

        free_time_spans = new_time_spans()
        current_time_spans = new_time_spans()

        if(is_empty_calendar_day(cal_day)):
            span = new_time_span(start_free_time,end_free_time)
            free_time_spans = insert_span(span,free_time_spans)
            return free_time_spans


        def add_current_time(appointments,current_time_spans):

            if not appointments:
                return current_time_spans

            span = get_span(appointments[0])
            if precedes(start_free_time,end_time(span)) and precedes(start_time(span),end_free_time):
                current_time_spans = insert_span(span,current_time_spans)

            return add_current_time(appointments[1:],current_time_spans)

        current_time_spans = add_current_time(strip_tag(cal_day),current_time_spans)

        return find_free_span(current_time_spans, free_time_spans,start_free_time,end_free_time)

def find_free_span(current_time_spans,free_time_spans,start,end):
    def free(current_time_spans,new_start_time,free_time_spans):

        if not current_time_spans:
            if precedes(new_start_time,end):
                span = new_time_span(new_start_time,end)
                free_time_spans = insert_span(span,free_time_spans)
            return free_time_spans

        span = current_time_spans[0]
        current_start = start_time(span)
        current_end = end_time(span)

        if precedes(current_start, start) or is_same_time(current_start,start):
            return free(current_time_spans[1:], current_end,free_time_spans)
        elif precedes(new_start_time, current_end):

            if(not(is_same_time(new_start_time,current_start))):

                span = new_time_span(new_start_time,current_start)
                free_time_spans = insert_span(span,free_time_spans)

            return free(current_time_spans[1:], current_end,free_time_spans)

    return free(strip_tag(current_time_spans),start,free_time_spans)

def remove_appointment(cal_day, start_time):
    "appointment x calendar_day -> calendar_day"

    start_time = convert_time(start_time)

    def without_appointment(al):

        if not al:
            return []

        span = get_span(al[0])
        current_time = strip_tag(span)[0]

        if(current_time == start_time):
            return without_appointment(al[1:])

        return [al[0]] + without_appointment(al[1:])

    ensure(cal_day, is_calendar_day)
    return attach_tag('calendar_day', without_appointment(strip_tag(cal_day)))


def remove(cal_name, date, month, time):
    "string x day x month x time -> none"
    day = new_day(date)
    mon = new_month(month)
    year = fetch_calendar(cal_name)
    new_year = new_calendar_year()
    cal_day = calendar_day(day, calendar_month(mon, year))
    calc_name = insert_calendar_month(
                            mon,
                            insert_calendar_day(
                                day,
                                remove_appointment(cal_day, time),
                                calendar_month(mon, year)),
                            year)

    insert_calendar(cal_name, calc_name)
    print("Appointment has been removed")


def show_free(cal_name, date, month, start, end):
    "String x day x month x time x time"
    day = new_day(date)
    mon = new_month(month)
    year = fetch_calendar(cal_name)

    cal_day = calendar_day(day, calendar_month(mon, year))
    start_time = convert_time(start)
    end_time = convert_time(end)
    return show_time_spans(free_spans(cal_day,start_time,end_time))
