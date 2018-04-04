# regexp creator : epoch dates
# given a list of directories, find those which are within a time frame
# for example, last five entries
# (presumably find / mtime or other OS methods can't be used )

import datetime
import time

def create_regex(querydays):
    """output a regular expression that will include now to X days back."""
    regex = []
    unsync = 0
    # epoch now
    now = int(time.time())
    epochlen = len(str(now))
    scan = list(str(now))
    target_date = now - int(datetime.timedelta(days=querydays).total_seconds())
    print(now, target_date)
    for x, y in enumerate(list(str(target_date))):
        if y != scan[x] and unsync == 0:
            # now quite right
            print( int(y) + 1, '-', int(scan[x]) -1, '\d{', epochlen - x - 1, '}')
            unsync = x
        elif y != scan[x]:
            print( int(y) + 1, '-', int(scan[x]) -1, '\d{', epochlen - x - 1, '}')
    return str(now)[:unsync]

# thinking https://stackoverflow.com/questions/29977086/regex-how-can-i-match-all-numbers-greater-than-954
# chain like 152220688[7-9]|15222068[9]|1522206[9]|152220[7-9]|15222[1-9]|1522[3-4]
# 152245
# 152244
# 152145
# 152030
# (1,1)(5,5)(2,2)(2,0)(4,3)(5,0) zip?
# 152[1d{2}|
print(create_regex(2))a
