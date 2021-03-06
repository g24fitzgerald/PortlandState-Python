"""Learn to Program: The Fundamentals | University of Toranto Computer Science
2018 Gina Fitzgerald"""

def report_status(scheduled_time, estimated_time):
    """(number, number) -> str

    Return the flight status {on time, early, delayed}
    for a flight that was scheduled to arrive at
    scheduled_time, but is expected at estimated_time.

    Pre-condition: 0.0 <= scheduled_time < 24
                   0.0 <= estimated_time < 24

    >>>report_status(14.3, 14.3)
    "on time"
    >>>report_status(12.5, 11.5)
    "early"
    >>>report_status(10.2, 11.5)
    "delayed"
    """
    if estimated_time < scheduled_time:
        return "early"
    elif estimated_time > scheduled_time:
        return "delayed"
    else:
        return "on time"
