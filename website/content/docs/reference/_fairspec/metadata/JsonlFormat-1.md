---
editUrl: false
next: false
prev: false
title: "JsonlFormat"
---

> `const` **JsonlFormat**: `ZodObject`\<\{ `columnNames`: `ZodOptional`\<`ZodArray`\<`ZodString`\>\>; `commentPrefix`: `ZodOptional`\<`ZodString`\>; `commentRows`: `ZodOptional`\<`ZodArray`\<`ZodNumber`\>\>; `description`: `ZodOptional`\<`ZodString`\>; `headerJoin`: `ZodOptional`\<`ZodString`\>; `headerRows`: `ZodOptional`\<`ZodUnion`\<readonly \[`ZodLiteral`\<`false`\>, `ZodArray`\<`ZodNumber`\>\]\>\>; `name`: `ZodLiteral`\<`"jsonl"`\>; `rowType`: `ZodOptional`\<`ZodEnum`\<\{ `array`: `"array"`; `object`: `"object"`; \}\>\>; `title`: `ZodOptional`\<`ZodString`\>; \}, `$strip`\>

Defined in: [metadata/models/format/jsonl.ts:12](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/metadata/models/format/jsonl.ts#L12)
