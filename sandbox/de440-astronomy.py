from skyfield import almanac
from skyfield.api import load, wgs84
import pytz
import astronomy # https://github.com/cosinekitty/astronomy
from datetime import datetime, timedelta

eph = load('de440.bsp')
ts = load.timescale()

tehran_tz = pytz.timezone('Asia/Tehran')

print("Spring Equinox (March Equinox) in Tehran Timezone (IRST/IRDT)")
print("Year       Date       Time       DST Status")
print("-------------------------------------------")

for year in range(2025, 2001, -1):
    t0 = ts.utc(year, 3, 19)
    t1 = ts.utc(year, 4, 22)
    
    t, y = almanac.find_discrete(t0, t1, almanac.seasons(eph))
    
    for ti, yi in zip(t, y):
        if yi == 0:
            utc_time = ti.utc_datetime()
            tehran_time = utc_time.astimezone(tehran_tz)
            
            is_dst = tehran_time.dst() != timedelta(0)
            dst_status = "IRDT" if is_dst else "IRST"
            
            print(f"    de440: {year}  {tehran_time.strftime('%Y-%m-%d  %H:%M:%S')}  {dst_status}")
            
            dt = astronomy.Seasons(year).mar_equinox.Utc()
            dt_utc = pytz.utc.localize(dt)
            dt_in_timezone = dt_utc.astimezone(pytz.timezone('Asia/Tehran'))
            print(f"astronomy: {year}  {dt_in_timezone.strftime('%Y-%m-%d  %H:%M:%S')}  {dst_status}")
            
            break
