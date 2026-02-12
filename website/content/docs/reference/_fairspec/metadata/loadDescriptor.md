---
editUrl: false
next: false
prev: false
title: "loadDescriptor"
---

> **loadDescriptor**(`path`, `options?`): `Promise`\<`Record`\<`string`, `any`\>\>

Defined in: [metadata/actions/descriptor/load.ts:10](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/metadata/actions/descriptor/load.ts#L10)

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
