---
editUrl: false
next: false
prev: false
title: "JsonPlugin"
---

Defined in: [table/plugins/json/plugin.ts:12](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/table/plugins/json/plugin.ts#L12)

## Implements

- [`TablePlugin`](/reference/_fairspec/table/tableplugin/)

## Constructors

### Constructor

> **new JsonPlugin**(): `JsonPlugin`

#### Returns

`JsonPlugin`

## Methods

### loadTable()

> **loadTable**(`resource`, `options?`): `Promise`\<`undefined` \| `LazyDataFrame`\<`any`\>\>

Defined in: [table/plugins/json/plugin.ts:13](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/table/plugins/json/plugin.ts#L13)

#### Parameters

##### resource

###### alternateIdentifiers?

`object`[]

###### contributors?

`object`[]

###### creators?

`object`[]

###### data?

`unknown`

###### dataSchema?

`string` \| `Record`\<`string`, `unknown`\>

###### dates?

`object`[]

###### descriptions?

`object`[]

###### doi?

`string`

###### format?

\{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `delimiter?`: `string`; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `lineTerminator?`: `string`; `name`: `"csv"`; `nullSequence?`: `string`; `quoteChar?`: `string`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `lineTerminator?`: `string`; `name`: `"tsv"`; `nullSequence?`: `string`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `jsonPointer?`: `string`; `name`: `"json"`; `rowType?`: `"object"` \| `"array"`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"jsonl"`; `rowType?`: `"object"` \| `"array"`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"xlsx"`; `sheetName?`: `string`; `sheetNumber?`: `number`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"ods"`; `sheetName?`: `string`; `sheetNumber?`: `number`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"sqlite"`; `tableName?`: `string`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"parquet"`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"arrow"`; `title?`: `string`; \} \| \{ `description?`: `string`; `name?`: `undefined`; `title?`: `string`; \}

###### formats?

`string`[]

###### fundingReferences?

`object`[]

###### geoLocations?

`object`[]

###### integrity?

\{ `hash`: `string`; `type`: `"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`; \}

###### integrity.hash

`string`

###### integrity.type

`"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`

###### language?

`string`

###### name?

`string`

###### prefix?

`string`

###### publicationYear?

`string`

###### publisher?

\{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}

###### publisher.lang?

`string`

###### publisher.name

`string`

###### publisher.publisherIdentifier?

`string`

###### publisher.publisherIdentifierScheme?

`string`

###### publisher.schemeUri?

`string`

###### relatedIdentifiers?

`object`[]

###### relatedItems?

`object`[]

###### rightsList?

`object`[]

###### sizes?

`string`[]

###### subjects?

`object`[]

###### suffix?

`string`

###### tableSchema?

`string` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"integer"` \| `"date"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

###### textual?

`boolean`

###### titles?

`object`[]

###### types?

\{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}

###### types.resourceType?

`string`

###### types.resourceTypeGeneral

`"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`

###### unstable_customMetadata?

`Record`\<`string`, `unknown`\>

###### version?

`string`

##### options?

[`LoadTableOptions`](/reference/_fairspec/table/loadtableoptions/)

#### Returns

`Promise`\<`undefined` \| `LazyDataFrame`\<`any`\>\>

#### Implementation of

[`TablePlugin`](/reference/_fairspec/table/tableplugin/).[`loadTable`](/reference/_fairspec/table/tableplugin/#loadtable)

***

### saveTable()

> **saveTable**(`table`, `options`): `Promise`\<`undefined` \| `string`\>

Defined in: [table/plugins/json/plugin.ts:20](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/table/plugins/json/plugin.ts#L20)

#### Parameters

##### table

[`Table`](/reference/_fairspec/table/table/)

##### options

[`SaveTableOptions`](/reference/_fairspec/table/savetableoptions/)

#### Returns

`Promise`\<`undefined` \| `string`\>

#### Implementation of

[`TablePlugin`](/reference/_fairspec/table/tableplugin/).[`saveTable`](/reference/_fairspec/table/tableplugin/#savetable)
