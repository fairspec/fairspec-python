---
editUrl: false
next: false
prev: false
title: "describeFile"
---

> **describeFile**(`path`, `options?`): `Promise`\<\{ `bytes`: `number`; `integrity`: `undefined` \| \{ `hash`: `string`; `type`: `"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`; \}; `textual`: `boolean`; \}\>

Defined in: [dataset/actions/file/describe.ts:5](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/dataset/actions/file/describe.ts#L5)

## Parameters

### path

`string`

### options?

#### hashType?

`"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`

## Returns

`Promise`\<\{ `bytes`: `number`; `integrity`: `undefined` \| \{ `hash`: `string`; `type`: `"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`; \}; `textual`: `boolean`; \}\>
