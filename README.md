Aggregate knowledge around equinox calcuation so we can be more confident about
a final implementation.

[iran-ground-truth.json](/iran-ground-truth.json), Spring equinox times
provided in Iran's time by calendar.ut.ac.ir, we like to have an implementation
matching to it.

Implementations:
* https://github.com/xyproto/calendar/blob/master/equinox.go
  which it self is a port of http://jgiesen.de/astro/astroJS/seasons/seasons.js
  used on http://jgiesen.de/astro/astroJS/seasons/
  Our current https://github.com/persian-calendar/equinox is based on it
* https://stellafane.org/misc/equinox.html this apparently matches better with
  Iran provided ones? ([Dart](https://github.com/shawnlauzon/meeus) & [Go](https://github.com/soniakeys/meeus) implementation from the same [book](https://www.amazon.com/Astronomical-Algorithms-Jean-Meeus/dp/0943396611))
* (feel free to add more)
