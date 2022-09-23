# grafana-simplejson-proxies

A collection of proxy backends for the Grafana SimpleJson plugin. See:
- https://grafana.com/grafana/plugins/grafana-simple-json-datasource/

## Common Functionality
These plugins are very simple. They convert from a non-supported format, where no
community plugin exists, to an API compatible with the SimpleJson plugin.

If you're exposing metrics and are using Prometheus, you should definitely consider
a Prometheus exporter over a proxy backend like the ones found here. This style
of backend is useful for things that wouldn't fit well in a Prometheus (or other)
TSDB.

### Caching
All of these plugins implement some very simple TTL caching to reduce load on the
backend. The default cache TTL is 1800 seconds (30 minutes) and is configurable.

## ical-simplejson-proxy
This proxy returns an iCal feed as annotations. I wanted to have events from a shared
maintenance calendar available on a status page in Grafana. There is a Google Calendar
datasource backend plugin, but I wanted something less tied in. iCal is pretty much
the defacto calendar sharing standard format.
