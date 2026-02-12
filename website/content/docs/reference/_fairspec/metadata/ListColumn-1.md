---
editUrl: false
next: false
prev: false
title: "ListColumn"
---

> `const` **ListColumn**: `ZodObject`\<\{ `name`: `ZodString`; `property`: `ZodObject`\<\{ `const`: `ZodOptional`\<`ZodString`\>; `default`: `ZodOptional`\<`ZodArray`\<`ZodString`\>\>; `delimiter`: `ZodOptional`\<`ZodString`\>; `description`: `ZodOptional`\<`ZodString`\>; `enum`: `ZodOptional`\<`ZodArray`\<`ZodString`\>\>; `examples`: `ZodOptional`\<`ZodArray`\<`ZodString`\>\>; `format`: `ZodLiteral`\<`"list"`\>; `itemType`: `ZodOptional`\<`ZodEnum`\<\{ `boolean`: `"boolean"`; `date`: `"date"`; `date-time`: `"date-time"`; `integer`: `"integer"`; `number`: `"number"`; `string`: `"string"`; `time`: `"time"`; \}\>\>; `maxItems`: `ZodOptional`\<`ZodNumber`\>; `maxLength`: `ZodOptional`\<`ZodNumber`\>; `minItems`: `ZodOptional`\<`ZodNumber`\>; `minLength`: `ZodOptional`\<`ZodNumber`\>; `missingValues`: `ZodOptional`\<`ZodArray`\<`ZodUnion`\<readonly \[`ZodString`, `ZodObject`\<\{ `label`: `ZodString`; `value`: `ZodString`; \}, `$strip`\>\]\>\>\>; `pattern`: `ZodOptional`\<`ZodString`\>; `rdfType`: `ZodOptional`\<`ZodString`\>; `title`: `ZodOptional`\<`ZodString`\>; `type`: `ZodLiteral`\<`"string"`\>; \}, `$strip`\>; `required`: `ZodOptional`\<`ZodBoolean`\>; `type`: `ZodLiteral`\<`"list"`\>; \}, `$strip`\>

Defined in: [metadata/models/column/list.ts:44](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/metadata/models/column/list.ts#L44)
