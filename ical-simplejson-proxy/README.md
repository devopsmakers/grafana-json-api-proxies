# ical-simplejson-proxy

## Configuration

### Environment Variables
#### Required
- `ICAL_URL` - The URL to the iCal feed or file. Examples: `file://path/to/file.ics`,
  `https://my.calendar.org/feeds/calendar.ics`
#### Optional
- `CACHE_TTL` - Default: 1800 - The number of seconds that results should be cached for.
