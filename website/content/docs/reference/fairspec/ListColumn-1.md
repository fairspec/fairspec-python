---
editUrl: false
next: false
prev: false
title: "ListColumn"
---

> `const` **ListColumn**: `z.ZodObject`\<\{ `name`: `z.ZodString`; `property`: `z.ZodObject`\<\{ `const`: `z.ZodOptional`\<`z.ZodString`\>; `default`: `z.ZodOptional`\<`z.ZodArray`\<`z.ZodString`\>\>; `delimiter`: `z.ZodOptional`\<`z.ZodString`\>; `description`: `z.ZodOptional`\<`z.ZodString`\>; `enum`: `z.ZodOptional`\<`z.ZodArray`\<`z.ZodString`\>\>; `examples`: `z.ZodOptional`\<`z.ZodArray`\<`z.ZodString`\>\>; `format`: `z.ZodLiteral`\<`"list"`\>; `itemType`: `z.ZodOptional`\<`z.ZodEnum`\<\{ `boolean`: `"boolean"`; `date`: `"date"`; `date-time`: `"date-time"`; `integer`: `"integer"`; `number`: `"number"`; `string`: `"string"`; `time`: `"time"`; \}\>\>; `maxItems`: `z.ZodOptional`\<`z.ZodNumber`\>; `maxLength`: `z.ZodOptional`\<`z.ZodNumber`\>; `minItems`: `z.ZodOptional`\<`z.ZodNumber`\>; `minLength`: `z.ZodOptional`\<`z.ZodNumber`\>; `missingValues`: `z.ZodOptional`\<`z.ZodArray`\<`z.ZodUnion`\<readonly \[`z.ZodString`, `z.ZodObject`\<\{ `label`: ...; `value`: ...; \}, `z.core.$strip`\>\]\>\>\>; `pattern`: `z.ZodOptional`\<`z.ZodString`\>; `rdfType`: `z.ZodOptional`\<`z.ZodString`\>; `title`: `z.ZodOptional`\<`z.ZodString`\>; `type`: `z.ZodLiteral`\<`"string"`\>; \}, `z.core.$strip`\>; `required`: `z.ZodOptional`\<`z.ZodBoolean`\>; `type`: `z.ZodLiteral`\<`"list"`\>; \}, `z.core.$strip`\>

Defined in: metadata/build/models/column/list.d.ts:32
