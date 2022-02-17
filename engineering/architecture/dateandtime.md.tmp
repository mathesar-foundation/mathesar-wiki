---
title: Human Readable Dates and Times
description: Spec for handling dates and times in a human friendly way.
published: true
date: 2022-02-14T12:35:23.307Z
tags: 
editor: markdown
dateCreated: 2022-02-15T14:58:57.900Z
---

## Goals

1. Users should be able to interact with dates, times, datetimes, and time durations in Mathesar in the most human-friendly way possible
2. The UI should be extremely forgiving w.r.t. date/time input, and also display dates and times in a human-friendly way.
3. The API should be extremely forgiving w.r.t. date/time input, but should return dates, times, and time durations in a more programmatic, i.e., consistent way than the UI.
4. The UI and API should be consistent in the following way:  If the input string is understood by both UI and API, they should always result in the _same date/time_ being stored, regardless of the input method.
5. The dates/times understood by the API should be a subset of those understood by the UI. That is, there should be no dates/times/time durations that are understood by the API, but which can't be entered through the UI.

## Overall input flow

If the UI is able to parse a date, time, duration, etc., it should reformat it into the appropriate canonical form described below and send that as the input to be stored to the API. If it's not able to parse the input, it should send the raw input string to the API and let the service layer / database try to parse the string. This helps satisfy goal number 5. If the service layer is able to parse the string, then store it. Otherwise, raise a validation error.

Another way to input data is through bulk import. In that case, we're completely reliant on the database parsing. This is the reason goal (4) is important.

#### Regarding relative times

There are some relative dates / times which make sense, e.g. "tomorrow", to store in a date column. These will _not_ be stored in a "relative" way, though. They'll be stored as a static date or time (one day later than the current day in the example). As for durations, there's some weird overlap between intervals "2 days ago" and a specific time "2 days ago". We'll choose whether to store the duration or a static time based on the column type.

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

Note where the units do and do not aggregate into larger units in the second example.

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
Here, `hour` and `minute` are both 2-digit integers between `00` and `59`. `second` is an integer or float which is at least `00` and which is strictly less than `60`. Each of these is padded to the tens place with zeroes if needed. The `offset` has a `+` or `-` prefix, and then the form `{hour}:{minute}` to describe the amount of the offset. If the minute value is `00`, we can omit `:{minute}`. In the special case where `offset` is zero, i.e., for UTC, we use `Z`.

For columns which don't have time zones, we'll (of course) omit the `offset` entirely.

#### Examples of canonical times

- `12:30:15Z`
- `12:30:15-08`
- `12:30:15+05:30`
- `12.30:15.5432`

### Date/Time combinations

For these, we use a combination of the pieces above to construct
```python
f'{year}-{month}-{day}T{hour}:{minute}{second}{offset} {era}'
```
For columns which don't have time zones, we'll (of course) omit the `offset` entirely.

#### Examples of canonical date/time combinations

- `2022-02-15T12:30:15Z AD`
- `0022-02-15T12:30:15 BC`
- `2222-02-15T12:30:15.12345-08 AD`
