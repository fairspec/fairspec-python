---
editUrl: false
next: false
prev: false
title: "inspectJson"
---

> **inspectJson**(`value`, `options`): `Promise`\<`object`[]\>

Defined in: [metadata/actions/json/inspect.ts:9](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/metadata/actions/json/inspect.ts#L9)

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
