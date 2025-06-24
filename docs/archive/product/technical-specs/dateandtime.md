# Human Readable Dates and Times

## Goals

1. Users should be able to interact with dates, times, datetimes, and time durations in Mathesar in the most human-friendly way possible
2. The UI should be extremely forgiving w.r.t. date/time input, and also display dates and times in a human-friendly way.
3. The API should be extremely forgiving w.r.t. date/time input, but should return dates, times, and time durations in a more programmatic, i.e., consistent way than the UI.
4. The UI and API should be consistent in the following way:  If the input string is accepted by both UI and API, they should always result in the _same date/time_ being stored, regardless of the input method.
5. The dates/time input strings accepted by the API should be a subset of those accepted by the UI. That is, there should be no dates/times/time durations that are accepted by the API, but which are invalidated by the UI.

## Overall input flow

For the moment, the UI should simply send the input string along to the API to be handled by the data layer, which should use the underlying database to parse input strings into date/time types to avoid inconsistency. 

If we want to extend the set of understandable date/time input strings in the future, then the UI could parse the more exotic input strings into the appropriate canonical form described below and send that as the input to be stored to the API. The canonical form isn't _required_, but it's recommended since it guarantees the known value ending up stored in the database. Care should be taken to ensure that _if the UI parses the string_, then it's either 

- a string which wouldn't be handled by the database parsing, or
- the parsing results in an identical value being stored as the one that would have resulted from sending the raw string to the API. 

If the UI is not able to parse the input, it should still send the raw input string to the API and let the data layer try to parse the string. This helps satisfy goal number 5. If the data layer is able to parse the string, then store it. Otherwise, raise a validation error.

Another way to input data is through bulk import. In that case, we're completely reliant on the database parsing. This is the reason goal (4) is important.

The PostgreSQL documentation regarding Date and Time types is [here](https://www.postgresql.org/docs/13/datatype-datetime.html). Note especially the input and output of the various types.

#### Regarding relative times

There are some relative dates / times which make sense, e.g. "tomorrow", to store in a date column. These will _not_ be stored in a "relative" way, though. They'll be stored as a static date or time (one day later than the current day in the example). As for durations, there's some weird overlap between intervals "2 days ago" and a specific time "2 days ago". We'll choose whether to store the duration or a static time based on the column type or other context.

## Overall output flow

For showing dates / times, they'll always be returned from the API in the appropriate canonical form described below. It's then up to the UI layer to format them for a pleasant display to the user.

## RFC 3339 (based on ISO 8601)

The canonical representation of a date, time, datetime, or duration in Mathesar will be as per the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#appendix-A) spec, with very minor modifications to match our use case.

## Canonical Representation of Durations

A duration describes the amount of time between two datetime values (or dates or times). Two durations can be added or subtracted to create another duration. A duration can be added to a date, time, or datetime to get a different date, time, or datetime. As per the RFC, the canonical representation of a duration is:

```python
f'P{years}Y{months}M{days}DT{hours}H{minutes}M{seconds}S'
```
Here, `seconds` can be an integer or float, and the other variables are all integers. For the canonical representation, we are filling in each unit with zeroes, which is optional in the RFC spec. To be completely proper, we aggregate units of time into larger ones where possible:

- seconds aggregate into minutes,
- minutes aggregate into hours, and
- months aggregate into years.

Because some units of time (months and days) are inconsistent w.r.t. the number of smaller units they contain, we avoid aggregating some units:

- hours do not aggregate into days, and
- days do not aggregate into months.

#### Examples of Canonical Durations

- `'1 year 1 month, 1 day 1 hour 1 minute 1.1 seconds'` maps to `P1Y1M1DT1H1M1.1S`
- `'0 years 13 months 31 days 23 hours 60 minutes 61.1 seconds'` maps to `P1Y1M31DT24H1M1.1S`
- `'1 year -1 month 3 days 14 hours -10 minutes 30.4 seconds'` maps to `P0Y11M3DT13H50M30.4S`
- `'1 year -1 month 3 days 14 hours -10 minutes 30.4 seconds ago'` maps to `P0Y-11M-3DT-13H-50M-30.4S`

Notes:

- Commas and pluralization don't matter. 
- We use `T` to separate the date and time portions.
- Take care of where the units do and do not aggregate into larger units in the second example.
- Take care of how units are disaggregated in the third and fourth examples (e.g., 1 year - 1 month is 11 months). Negatives can get complicated.
- In the final example, we see that `'ago'` negates the whole duration, but negative signs `'-'` affect only the single following unit.

## Canonical Representation of Dates and Times

These will similarly follow RFC 3339.

### Dates

```python
f'{year}-{month}-{day} {era}'
```
Here, `year` will have a minimum of 4 digits, using preceding zeroes for years like 0042 b.c. Years with more than 4 digits have the correct number of digits. `month` is a 2-digit integer, as is `day` (with preceding zeroes as needed). `era` will always be included, and will be either `BC` or `AD` as appropriate.

#### Examples of canonical dates

- `2022-02-15 AD`
- `0022-02-15 BC`
- `10101-01-01 AD`

### Times

```python
f'{hour}:{minute}:{second}{offset}'
```
Here, `hour` and `minute` are both 2-digit integers between `00` and `59`. `second` is an integer or float which is at least `00` and which is strictly less than `60`. Each of these is padded to the tens place with zeroes if needed. The `offset` has a `+` or `-` prefix, and then the form `{hour}:{minute}` to describe the amount of the offset. In the special case where `offset` is zero, i.e., for UTC, we use `Z`.

For columns which don't have time zones, we'll (of course) omit the `offset` entirely.

#### Examples of canonical times

- `12:30:15Z`
- `12:30:15-08:00`
- `12:30:15+05:30`
- `12:30:15.5432`

### Date/Time combinations

For these, we use a combination of the pieces above to construct
```python
f'{year}-{month}-{day}T{hour}:{minute}{second}{offset} {era}'
```
For columns which don't have time zones, we'll (of course) omit the `offset` entirely.

#### Examples of canonical date/time combinations

- `2022-02-15T12:30:15Z AD`
- `0022-02-15T12:30:15 BC`
- `2222-02-15T12:30:15.12345-08:00 AD`

Note the `T` separator between the date and time portions.

## Appendix: Mathesar vs. other tools

This appendix should collect (over time) more and more examples of differences between date/time/datetime parsing in Mathesar and other tools.

### Google Sheets

| Data type | User input |  PostgreSQL | Google Sheets |
| -- | -- | -- | -- |
| date | `7/8` | error | `2022-07-08` |
| date | `12/30/69` | `2069-12-30` | `1969-12-30` |
| time | `6 pm` | error | `18:00:00` |
