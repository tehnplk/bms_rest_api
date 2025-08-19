from datetime import datetime, timezone, timedelta


dt1 = (
    datetime.now(timezone.utc)
    .isoformat(timespec="milliseconds")
    .replace("+00:00", "Z")
)
dt2 = (
    datetime.now(timezone(timedelta(hours=7)))
    .isoformat(timespec="milliseconds")
    .replace("+07:00", "Z")
)
dt3 = (
    datetime.now(timezone(timedelta(hours=7)))
    .isoformat(timespec="milliseconds")
    .replace("+07:00", "Z")
)
print('dt1',dt1)
print('dt2',dt2)
print('dt3',dt3)