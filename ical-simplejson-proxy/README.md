# ical-simplejson-proxy

## Configuration

### HTTP Headers
#### Required
- `X-ICAL-URL` - The URL of the iCal feed.
#### Optional
- `X-TAGS` - A comma delimited list of tags for the annotations. Example: `maintenance,IT,planned`

### Environment Variables
#### Optional
- `CACHE_TTL` - Default: 1800 - The number of seconds that results should be cached for.