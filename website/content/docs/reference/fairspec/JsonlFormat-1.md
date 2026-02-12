---
editUrl: false
next: false
prev: false
title: "JsonlFormat"
---

> `const` **JsonlFormat**: `z.ZodObject`\<\{ `columnNames`: `z.ZodOptional`\<`z.ZodArray`\<`z.ZodString`\>\>; `commentPrefix`: `z.ZodOptional`\<`z.ZodString`\>; `commentRows`: `z.ZodOptional`\<`z.ZodArray`\<`z.ZodNumber`\>\>; `description`: `z.ZodOptional`\<`z.ZodString`\>; `headerJoin`: `z.ZodOptional`\<`z.ZodString`\>; `headerRows`: `z.ZodOptional`\<`z.ZodUnion`\<readonly \[`z.ZodLiteral`\<`false`\>, `z.ZodArray`\<`z.ZodNumber`\>\]\>\>; `name`: `z.ZodLiteral`\<`"jsonl"`\>; `rowType`: `z.ZodOptional`\<`z.ZodEnum`\<\{ `array`: `"array"`; `object`: `"object"`; \}\>\>; `title`: `z.ZodOptional`\<`z.ZodString`\>; \}, `z.core.$strip`\>

Defined in: metadata/build/models/format/jsonl.d.ts:2
