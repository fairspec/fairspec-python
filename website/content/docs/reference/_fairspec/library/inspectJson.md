---
editUrl: false
next: false
prev: false
title: "inspectJson"
---

> **inspectJson**(`value`, `options`): `Promise`\<`object`[]\>

Defined in: metadata/build/actions/json/inspect.d.ts:6

Validate a value against a JSON Schema
It uses Ajv for JSON Schema validation under the hood

## Parameters

### value

`unknown`

### options

#### jsonSchema

`string` \| `Record`\<`string`, `unknown`\>

#### rootJsonPointer?

`string`

## Returns

`Promise`\<`object`[]\>
