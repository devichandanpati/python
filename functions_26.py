def to_secs(hr,min,secs) :
    secs_hours = hr * 3600
    secs_min = min * 60
    secs_secs = secs * 1

    total_secs = secs_hours + secs_min + secs_secs
    return total_secs

hr = float(input("Number of hours"))
min = float(input("Number of min"))
secs = float(input("Number of secs"))

print(int(to_secs(hr,min,secs)))