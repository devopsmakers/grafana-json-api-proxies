# ical-proxy

Exposes an iCal feed as JSON for querying with the JSON API plugin.

Examples:
  - input: ./fixtures/calendar.ics
  - output: ./fixtures/calendar.json

Url to query: <hostname:port>/annotations - does not do any filtering or querying (exposes all events). The JSON result can be queried as a metric to display in tables, or as annotations.

You can get extra information from the JSON using the JSONata features of the JSON API plugin. Examples:

- `duration`: `$.(timeEnd-time)`
- `timeSinceEvent`: `$.(timeEnd-$millis())`

You can use values in transforms to filter data out of tables.

## Configuration

### HTTP Headers
#### Required
- `X-ICAL-URL` - The URL of the iCal feed.
#### Optional
- `X-TAGS` - A comma delimited list of tags for the annotations. Example: `maintenance,IT,planned`

### Environment Variables
#### Optional
- `CACHE_TTL` - Default: 1800 - The number of seconds that results should be cached for.
