[iran-ground-truth.json](iran-ground-truth.json) holds the spring-equinox
(Nowruz / Tahvil-e Sal) moments officially announced by the University of Tehran
(`calendar.ut.ac.ir`), given in Iran Standard Time (UTC+3:30) and rounded to
whole seconds. Each row is:

    [year, month, day, hour, minute, second, source-url]

[persian-calendar/equinox](https://github.com/persian-calendar/equinox) now
targets sub-second accuracy against JPL DE440 (error < 1 s for 1800–2200), and
we validate it against this ground truth as a second, independent signal.

Recent years match almost exactly: the announced value is essentially the DE440
instant rounded to the second, so the difference is normally ±1–2 s. Older
years drift more however.

## Summary

| Range     | Typical Δ vs DE440 |
|-----------|--------------------|
| 2003–2026 | ≈ ±0.1–2.1 s       |
| 2002      | −6.3 s             |
| 2001      | −2.3 s             |
| 1990s     | +6…13 s            |
| 1980s     | +8…20 s            |
| 1981      | +40.4 s            |

## Per-year difference

`Δ` is announced − DE440, in seconds; DE440's time is shown in IRST as well.

| Year | Announced (IRST) | DE440 (IRST) | Δ (s) |
|-----:|------------------|--------------|------:|
| 2026 | Mar 20, 18:15:59 | Mar 20, 18:15:57 |  +1.6 |
| 2025 | Mar 20, 12:31:30 | Mar 20, 12:31:29 |  +1.1 |
| 2024 | Mar 20, 06:36:26 | Mar 20, 06:36:24 |  +1.8 |
| 2023 | Mar 21, 00:54:28 | Mar 21, 00:54:26 |  +1.5 |
| 2022 | Mar 20, 19:03:26 | Mar 20, 19:03:25 |  +1.1 |
| 2021 | Mar 20, 13:07:28 | Mar 20, 13:07:29 |  −0.5 |
| 2020 | Mar 20, 07:19:37 | Mar 20, 07:19:37 |  −0.1 |
| 2019 | Mar 21, 01:28:27 | Mar 21, 01:28:26 |  +1.2 |
| 2018 | Mar 20, 19:45:28 | Mar 20, 19:45:27 |  +0.7 |
| 2017 | Mar 20, 13:58:40 | Mar 20, 13:58:38 |  +2.1 |
| 2016 | Mar 20, 08:00:12 | Mar 20, 08:00:11 |  +0.8 |
| 2015 | Mar 21, 02:15:11 | Mar 21, 02:15:09 |  +1.7 |
| 2014 | Mar 20, 20:27:07 | Mar 20, 20:27:06 |  +1.4 |
| 2013 | Mar 20, 14:31:56 | Mar 20, 14:31:55 |  +1.3 |
| 2012 | Mar 20, 08:44:27 | Mar 20, 08:44:26 |  +1.3 |
| 2011 | Mar 21, 02:50:45 | Mar 21, 02:50:43 |  +1.6 |
| 2010 | Mar 20, 21:02:13 | Mar 20, 21:02:12 |  +1.0 |
| 2009 | Mar 20, 15:13:39 | Mar 20, 15:13:37 |  +1.5 |
| 2008 | Mar 20, 09:18:19 | Mar 20, 09:18:17 |  +1.6 |
| 2007 | Mar 21, 03:37:26 | Mar 21, 03:37:25 |  +1.1 |
| 2006 | Mar 20, 21:55:35 | Mar 20, 21:55:34 |  +1.3 |
| 2005 | Mar 20, 16:03:24 | Mar 20, 16:03:25 |  −1.1 |
| 2004 | Mar 20, 10:18:37 | Mar 20, 10:18:38 |  −1.1 |
| 2003 | Mar 21, 04:29:45 | Mar 21, 04:29:46 |  −0.7 |
| 2002 | Mar 20, 22:46:02 | Mar 20, 22:46:08 |  −6.3 |
| 2001 | Mar 20, 17:00:40 | Mar 20, 17:00:42 |  −2.3 |
| 2000 | Mar 20, 11:05:14 | Mar 20, 11:05:14 |  −0.4 |
| 1999 | Mar 21, 05:15:48 | Mar 21, 05:15:48 |  −0.4 |
| 1998 | Mar 20, 23:24:31 | Mar 20, 23:24:32 |  −0.5 |
| 1997 | Mar 20, 17:24:46 | Mar 20, 17:24:39 |  +6.6 |
| 1996 | Mar 20, 11:33:10 | Mar 20, 11:33:04 |  +6.2 |
| 1995 | Mar 21, 05:44:35 | Mar 21, 05:44:25 | +10.2 |
| 1994 | Mar 20, 23:58:13 | Mar 20, 23:58:00 | +12.9 |
| 1993 | Mar 20, 18:10:50 | Mar 20, 18:10:38 | +12.3 |
| 1992 | Mar 20, 12:18:11 | Mar 20, 12:18:03 |  +8.3 |
| 1991 | Mar 21, 06:32:04 | Mar 21, 06:31:55 |  +9.0 |
| 1990 | Mar 21, 00:49:26 | Mar 21, 00:49:15 | +10.7 |
| 1989 | Mar 20, 18:58:29 | Mar 20, 18:58:15 | +14.1 |
| 1988 | Mar 20, 13:08:56 | Mar 20, 13:08:36 | +20.4 |
| 1987 | Mar 21, 07:22:08 | Mar 21, 07:21:58 | +10.5 |
| 1986 | Mar 21, 01:32:56 | Mar 21, 01:32:41 | +15.0 |
| 1985 | Mar 20, 19:43:56 | Mar 20, 19:43:44 | +12.1 |
| 1984 | Mar 20, 13:54:31 | Mar 20, 13:54:19 | +11.8 |
| 1983 | Mar 21, 08:08:53 | Mar 21, 08:08:44 |  +8.8 |
| 1982 | Mar 21, 02:25:59 | Mar 21, 02:25:50 |  +8.9 |
| 1981 | Mar 20, 20:33:31 | Mar 20, 20:32:51 | +40.4 |
