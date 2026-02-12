---
editUrl: false
next: false
prev: false
title: "CellError"
---

> `const` **CellError**: `ZodDiscriminatedUnion`\<\[`ZodObject`\<\{ `cell`: `ZodString`; `columnName`: `ZodString`; `columnType`: `ZodEnum`\<\{ `array`: `"array"`; `base64`: `"base64"`; `boolean`: `"boolean"`; `categorical`: `"categorical"`; `date`: `"date"`; `date-time`: `"date-time"`; `decimal`: `"decimal"`; `duration`: `"duration"`; `email`: `"email"`; `geojson`: `"geojson"`; `hex`: `"hex"`; `integer`: `"integer"`; `list`: `"list"`; `number`: `"number"`; `object`: `"object"`; `string`: `"string"`; `time`: `"time"`; `topojson`: `"topojson"`; `unknown`: `"unknown"`; `url`: `"url"`; `wkb`: `"wkb"`; `wkt`: `"wkt"`; \}\>; `rowNumber`: `ZodNumber`; `type`: `ZodLiteral`\<`"cell/type"`\>; \}, `$strip`\>, `ZodObject`\<\{ `cell`: `ZodString`; `columnName`: `ZodString`; `rowNumber`: `ZodNumber`; `type`: `ZodLiteral`\<`"cell/required"`\>; \}, `$strip`\>, `ZodObject`\<\{ `cell`: `ZodString`; `columnName`: `ZodString`; `minimum`: `ZodString`; `rowNumber`: `ZodNumber`; `type`: `ZodLiteral`\<`"cell/minimum"`\>; \}, `$strip`\>\], `"type"`\>

Defined in: [metadata/models/error/cell.ts:91](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/metadata/models/error/cell.ts#L91)
