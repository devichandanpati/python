def to_secs(hr,min,secs) :
    secs_hours = hr * 3600
    secs_min = min * 60
    secs_secs = secs * 1

    total_secs = secs_hours + secs_min + secs_secs
    return total_secs

hr = int(input("Number of hours"))
min = int(input("Number of min"))
secs = int(input("Number of secs"))

print(to_secs(hr,min,secs))
