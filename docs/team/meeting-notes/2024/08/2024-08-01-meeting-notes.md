# 2024-08-01 maintainer meeting

**Attendees**: Anish, Brent, Pavish, Sean

## Validation of metadata values

**Sean**:

I noticed a problem and I'm wondering if it's worth addressing.

The API accepts arbitrary strings like "foo" for metadata stored in Django `CharField` fields set to have specific `choices` values.

For example on columns we have a `bool_input` field to set whether to show a checkbox or a dropdown:

```py
class ColumnMetaData(BaseModel):
    # ...
    bool_input = models.CharField(
        choices=[("dropdown", "dropdown"), ("checkbox", "checkbox")],
        null=True
    )
    # ...
```

But this API request works:

```json
{
  "jsonrpc": "2.0",
  "method": "columns.metadata.set",
  "id": 0,
  "params": {
    "database_id": 1,
    "table_oid": 66125,
    "column_meta_data_list": [
      {
        "attnum": 6,
        "bool_input": "NOPE!"
      }
    ]
  }
}
```

I would expect that sort of request to fail based on validation either at the service layer or the DB layer.

Weird, right?

Is this a problem? Is it worth addressing for beta?

### Discussion
- We should fix this eventually, but it seems low priority.
    - We'll need to fix this on a field by field basis, even using Django's `full_clean` method. Anish tried this.
- Let's not worry about validation for now, treat this as a documentation issue rather than a validation issue.
- Might be better in the long run for the backend to validate less, and use more unstructured JSON blobs.
    - Sean has thoughts on this, but putting in the parking lot for now.


## Records vs. explorations filtering

Filtering options are different in `records.list` vs. `explorations.run`, will this cause an issue for the frontend?

- No, because explorations use transformations, don't filter directly.
- We don't expect the paradigm to be the same.
- Can be addressed later if needed, especially if/when explorations functionality is moved to the database layer.
