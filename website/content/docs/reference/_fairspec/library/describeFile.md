---
editUrl: false
next: false
prev: false
title: "describeFile"
---

> **describeFile**(`path`, `options?`): `Promise`\<\{ `bytes`: `number`; `integrity`: `undefined` \| \{ `hash`: `string`; `type`: `"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`; \}; `textual`: `boolean`; \}\>

Defined in: dataset/build/actions/file/describe.d.ts:2

## Parameters

### path

`string`

### options?

#### hashType?

`"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`

## Returns

`Promise`\<\{ `bytes`: `number`; `integrity`: `undefined` \| \{ `hash`: `string`; `type`: `"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`; \}; `textual`: `boolean`; \}\>
