---
editUrl: false
next: false
prev: false
title: "loadDescriptor"
---

> **loadDescriptor**(`path`, `options?`): `Promise`\<`Record`\<`string`, `any`\>\>

Defined in: metadata/build/actions/descriptor/load.d.ts:6

Load a descriptor (JSON Object) from a file or URL
Uses dynamic imports to work in both Node.js and browser environments
Supports HTTP, HTTPS protocols

## Parameters

### path

`string`

### options?

#### onlyRemote?

`boolean`

## Returns

`Promise`\<`Record`\<`string`, `any`\>\>
