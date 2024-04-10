# JSON-RPC client plans

## Examples of how the API would be called

### Non-batched

```ts
/** @type {ApiRequest<Spacecraft>>} */
const request = api.spacecrafts.get({ id: 42 });

/** @type {CancellablePromise<Spacecraft>} */
const promise = request.run();

/** @type {Spacecraft} */
const spacecraft = await promise; // Might throw!
```

### Batched

```ts
/** @type {[ApiResult<Spacecraft>, ApiResult<Voyage>]} */
const [spacecraftResult, voyageResult] = await batchSend(
  api.spacecrafts.get({ id: 42 }),
  api.voyages.get({ id: 100 }),
);

/** @type {Spacecraft} */
const spacecraft = spacecraftResult.unwrap(); // Might throw!

/** @type {Voyage} */
const voyage = voyageResult.unwrap(); // Might throw!
```

## Lower-level types

_(Some of these would actually be **classes**, but the type defs written below give you a rough idea of how they would work.)_

### ApiResult

```ts
interface ApiOk<T> {
  status: 'ok';
  value: T;
}

interface ApiError {
  status: 'error';
  code: number;
  message: string;
  data?: unknown;
}

type ApiResult<T> = ApiOk<T> | ApiError;
```

### ApiRequest

```ts
class ApiRequest<T> {
  /**
   * The simplest, most common way to run an API request.
   *
   * @throws `ApiError` when awaited if any errors are encountered.
   */
  run(): CancellablePromise<T> {
    throw Error('Not yet implemented');
  }

  /**
   * Provides more fine-grained control instead of `run` by returning
   * ApiResult which can be type-narrowed manually.
   *
   * Will not reject or throw errors.
   */
  send(): CancellablePromise<ApiResult<T>> {
    throw Error('Not yet implemented');
  }
}
```

## Error handling

### Error handling with try/catch

```ts
try {
  const spacecraft = await api.spacecrafts.get({ id: 42 }).run();
  toast.success(spacecraft.name);
} catch (e) {
  toast.error(getErrorMessage(e));
}
```

### Error handling with `match`

```ts
match(await api.spacecrafts.get({ id: 42 }).send(), 'status', {
  ok: ({ value: spacecraft }) => toast.success(spacecraft.name),
  error: ({ message }) => toast.error(message),
});
```

(I already implemented this `match` function in #3037 [here](https://github.com/mathesar-foundation/mathesar/blob/4f2a253cc8c83a1bd231ae2158b31fbb4c1c4097/mathesar_ui/src/utils/patternMatching.ts#L29).)
