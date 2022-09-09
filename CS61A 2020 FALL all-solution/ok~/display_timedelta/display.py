from datetime import timedelta


def display_timedelta(delta):
    if delta < timedelta(0):
        raise ValueError("cannot display negative time delta {}".format(delta))
    result = []
    seconds = int(delta.total_seconds())
    days, seconds = seconds // (3600 * 24), seconds % (3600 * 24)

    if days > 0:
        result.append("{} day{}".format(days, plural(days)))
    hours, seconds = seconds // 3600, seconds % 3600

    if hours > 0:
        result.append("{} hour{}".format(hours, plural(hours)))
    minutes, seconds = seconds // 60, seconds % 60

    if minutes > 0:
        result.append("{} minute{}".format(minutes, plural(minutes)))

    if seconds > 0:
        result.append("{} second{}".format(seconds, plural(seconds)))

    if len(result) >= 3:
        return ", ".join(result[:-1]) + ", and " + result[-1]

    if len(result) == 2:
        return " and ".join(result)

    if len(result) == 1:
        return result[0]

    return "right now"


def plural(number):
    if number == 1:
        return ""
    return "s"
