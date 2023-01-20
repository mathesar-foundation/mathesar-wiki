# 2023-01-20 Meeting about how to handle partial user input of dates

## Meeting details

- Attending: Sean, Pavish, Dom, Brent, Mukesh, Anish
- Facilitator: Sean

## Problem

- We have this ticket that we [can't agree](https://matrix.to/#/!vAyoAQoixqNrvBuIcH:matrix.mathesar.org/$LNuRmMfzsZ_8eV2Q-Z4tZ5kwfYUt_KsPVWQiRzSxYbU?via=matrix.mathesar.org&via=matrix.org) how to fix:

    **[InvalidDatetimeFormat error when attempting to filter on a partially-entered date](https://github.com/centerofci/mathesar/issues/1890)**


## Solution

Primarily:

- [Parse user entry of dates on the front end](https://github.com/centerofci/mathesar/issues/2327)

Secondarily (to mitigate against similar issues):

- [Fix API error response when filtering on an invalid date](https://github.com/centerofci/mathesar/issues/2326)
- [Keep records in store while fetching](https://github.com/centerofci/mathesar/issues/1893)


## Approaches we decided against

- ❌ Improve the API error response so that the front end can more gracefully handle this error scenario. Then modify the front end to avoid wiping out the records data when it receives an error.

    - When the ticket was originally opened, this approach was not considered viable due to performance problems with the API. Now those performance concerns seem to have vanished with the recent reflection improvements. But...

    - This will require a bit of work on the front end due to [1893](https://github.com/centerofci/mathesar/issues/1893).
    
    - Plus it doesn't give the user good feedback. If there are multiple filter conditions, we won't be able to show them which one is invalid.

- ❌ Validate partially-entered dates with Postgres on the backend before running the query, then remove problematic filter conditions before running the query

    - Users might enter an invalid value, expecting to see filtered data and become confused 

    - Running multiple DB queries in sequence, is not great for performance.

- ❌ Add a submit button to the filtering UI

    - This might work okay for the filtering dropdown, but it would not work very well for the Record Selector.

    - Can we submit on blur in the Record Selector? No because we _want_ "search as you type" for text columns, and using an inconsistent submission UX across different column types would be confusing.

- ❌ Force user to enter dates via the date-picker widget

    - This is bad UX. Lots of clicks to enter very distant dates. Bad a11y too. Relevant [HN post](https://news.ycombinator.com/item?id=34145216)

## Out of scope

This came up too, but we cut off conversation since it's an independent issue

- [Entering 'now' on a datetime column without timezone support shows different time from what user expects](https://github.com/centerofci/mathesar/issues/1694)


