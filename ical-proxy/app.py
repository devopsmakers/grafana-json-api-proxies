import os
import requests
import time
import icalendar

from datetime import datetime
from flask import Flask, request, abort
from flask_cors import CORS
from requests_file import FileAdapter
from cachetools import TTLCache, cached

CACHE_TTL = os.environ.get("CACHE_TTL", 1800)

CACHE = TTLCache(maxsize=1000, ttl=CACHE_TTL)

app = Flask(__name__)

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

methods = ["GET", "HEAD", "POST", "OPTIONS"]


@app.route("/", methods=methods)
def index():
    return "OK"


@app.route("/search", methods=methods)
def search():
    return []


@app.route("/query", methods=methods)
def query():
    return []


@app.route("/annotations", methods=methods)
def annotations():
    if request.method in ["GET", "POST"]:
        tags = ""

        ical_url = request.headers.get(
            "X-ICAL-URL",
            f"file://{os.path.dirname(os.path.realpath(__file__))}/fixtures/something.ics",
        )

        if "X-TAGS" in request.headers:
            tags = request.headers.get("X-TAGS")

        return _ical_annotations(ical_url, tags)
    return []


@app.route("/tag-keys", methods=methods)
def tag_keys():
    return []


@app.route("/tag-values", methods=methods)
def tag_values():
    return []


def _ical_annotations_cache_key(url: str, tags: str, *args):
    return f"{url}/{tags}"


@cached(CACHE, _ical_annotations_cache_key)
def _ical_annotations(url: str, tags: str):
    ical_data = _fetch_ical_data(url)
    ical_as_annotations = _convert_ical_to_annotations(ical_data, tags)

    return ical_as_annotations


def _fetch_ical_data(url: str):
    s = requests.Session()
    s.mount("file://", FileAdapter())

    ical_resp = s.get(url)
    if ical_resp.status_code != 200:
        abort(ical_resp.status_code)

    ical_data = ical_resp.text
    if not ical_data.startswith("BEGIN:VCALENDAR"):
        abort(400)

    return ical_data


def _convert_ical_to_annotations(ical_data, tags):
    ical_annotations = []
    ical_calendar = icalendar.Calendar.from_ical(ical_data)

    for component in ical_calendar.walk():
        if component.name == "VEVENT":
            try:
                ical_annotation = {
                    "time": int(
                        time.mktime(component.get("dtstart").dt.timetuple()) * 1000
                    ),
                    "title": component.get("summary"),
                    "tags": tags,
                    "text": component.get("description", ""),
                    "uid": component.get("uid"),
                }

                try:
                    ical_annotation["timeEnd"] = int(
                        time.mktime(component.get("dtend").dt.timetuple()) * 1000
                    )
                except AttributeError:
                    pass

                ical_annotations.append(ical_annotation)

            except AttributeError:
                print(
                    f'level=ERROR msg="decoding event failed" event_summary="{component.get("summary")}" event_dtstart="{component.get("dtstart")}" event_dtstamp="{component.get("dtstamp")}" event_dtend="{component.get("dtend")}"'
                )
    return ical_annotations


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
