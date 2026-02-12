---
editUrl: false
next: false
prev: false
title: "validateTable"
---

> **validateTable**(`resource`, `options?`): `Promise`\<\{ `errors`: (\{ `jsonPointer`: `string`; `message`: `string`; `type`: `"metadata"`; \} \| \{ `resourceName`: `string`; `type`: `"resource/missing"`; \} \| \{ `expectedResourceType`: `"data"` \| `"table"`; `type`: `"resource/type"`; \} \| \{ `columnName`: `string`; `type`: `"column/missing"`; \} \| \{ `actualColumnType`: `"string"` \| `"number"` \| `"boolean"` \| `"object"` \| `"date"` \| `"array"` \| `"url"` \| `"integer"` \| `"categorical"` \| `"list"` \| `"date-time"` \| `"time"` \| `"base64"` \| `"hex"` \| `"email"` \| `"duration"` \| `"wkt"` \| `"wkb"` \| `"decimal"` \| `"geojson"` \| `"topojson"` \| `"unknown"`; `columnName`: `string`; `expectedColumnType`: `"string"` \| `"number"` \| `"boolean"` \| `"object"` \| `"date"` \| `"array"` \| `"url"` \| `"integer"` \| `"categorical"` \| `"list"` \| `"date-time"` \| `"time"` \| `"base64"` \| `"hex"` \| `"email"` \| `"duration"` \| `"wkt"` \| `"wkb"` \| `"decimal"` \| `"geojson"` \| `"topojson"` \| `"unknown"`; `type`: `"column/type"`; \} \| \{ `columnNames`: `string`[]; `rowNumber`: `number`; `type`: `"row/primaryKey"`; \} \| \{ `columnNames`: `string`[]; `rowNumber`: `number`; `type`: `"row/uniqueKey"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `columnType`: `"string"` \| `"number"` \| `"boolean"` \| `"object"` \| `"date"` \| `"array"` \| `"url"` \| `"integer"` \| `"categorical"` \| `"list"` \| `"date-time"` \| `"time"` \| `"base64"` \| `"hex"` \| `"email"` \| `"duration"` \| `"wkt"` \| `"wkb"` \| `"decimal"` \| `"geojson"` \| `"topojson"` \| `"unknown"`; `rowNumber`: `number`; `type`: `"cell/type"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `rowNumber`: `number`; `type`: `"cell/required"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `minimum`: `string`; `rowNumber`: `number`; `type`: `"cell/minimum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `maximum`: `string`; `rowNumber`: `number`; `type`: `"cell/maximum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `minimum`: `string`; `rowNumber`: `number`; `type`: `"cell/exclusiveMinimum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `maximum`: `string`; `rowNumber`: `number`; `type`: `"cell/exclusiveMaximum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `multipleOf`: `number`; `rowNumber`: `number`; `type`: `"cell/multipleOf"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `minLength`: `number`; `rowNumber`: `number`; `type`: `"cell/minLength"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `maxLength`: `number`; `rowNumber`: `number`; `type`: `"cell/maxLength"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `minItems`: `number`; `rowNumber`: `number`; `type`: `"cell/minItems"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `maxItems`: `number`; `rowNumber`: `number`; `type`: `"cell/maxItems"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `pattern`: `string`; `rowNumber`: `number`; `type`: `"cell/pattern"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `rowNumber`: `number`; `type`: `"cell/unique"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `const`: `string`; `rowNumber`: `number`; `type`: `"cell/const"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `enum`: `string`[]; `rowNumber`: `number`; `type`: `"cell/enum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `jsonPointer`: `string`; `message`: `string`; `rowNumber`: `number`; `type`: `"cell/json"`; \} \| \{ `cells`: `string`[]; `foreignKey`: \{ `columns`: `string`[]; `reference`: \{ `columns`: `string`[]; `resource?`: `string`; \}; \}; `type`: `"foreignKey"`; \} \| \{ `jsonPointer`: `string`; `message`: `string`; `type`: `"data"`; \} \| \{ `actualEncoding?`: `string`; `type`: `"file/textual"`; \} \| \{ `actualHash`: `string`; `expectedHash`: `string`; `hashType`: `string`; `type`: `"file/integrity"`; \} \| (\{ type: "metadata"; message: string; jsonPointer: string; \} \| \{ type: "resource/missing"; resourceName: string; \} \| \{ type: "resource/type"; expectedResourceType: "data" \| "table"; \} \| ... 23 more ... \| \{ ...; \}) & \{ ...; \})[]; `valid`: `boolean`; \}\>

Defined in: library/build/actions/table/validate.d.ts:7

## Parameters

### resource

#### alternateIdentifiers?

`object`[]

#### contributors?

`object`[]

#### creators?

`object`[]

#### data?

`unknown`

#### dataSchema?

`string` \| `Record`\<`string`, `unknown`\>

#### dates?

`object`[]

#### descriptions?

`object`[]

#### doi?

`string`

#### format?

\{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `delimiter?`: `string`; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `lineTerminator?`: `string`; `name`: `"csv"`; `nullSequence?`: `string`; `quoteChar?`: `string`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `lineTerminator?`: `string`; `name`: `"tsv"`; `nullSequence?`: `string`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `jsonPointer?`: `string`; `name`: `"json"`; `rowType?`: `"object"` \| `"array"`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"jsonl"`; `rowType?`: `"object"` \| `"array"`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"xlsx"`; `sheetName?`: `string`; `sheetNumber?`: `number`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"ods"`; `sheetName?`: `string`; `sheetNumber?`: `number`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"sqlite"`; `tableName?`: `string`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"parquet"`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"arrow"`; `title?`: `string`; \} \| \{ `description?`: `string`; `name?`: `undefined`; `title?`: `string`; \}

#### formats?

`string`[]

#### fundingReferences?

`object`[]

#### geoLocations?

`object`[]

#### integrity?

\{ `hash`: `string`; `type`: `"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`; \}

#### integrity.hash

`string`

#### integrity.type

`"md5"` \| `"sha1"` \| `"sha256"` \| `"sha512"`

#### language?

`string`

#### name?

`string`

#### prefix?

`string`

#### publicationYear?

`string`

#### publisher?

\{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}

#### publisher.lang?

`string`

#### publisher.name

`string`

#### publisher.publisherIdentifier?

`string`

#### publisher.publisherIdentifierScheme?

`string`

#### publisher.schemeUri?

`string`

#### relatedIdentifiers?

`object`[]

#### relatedItems?

`object`[]

#### rightsList?

`object`[]

#### sizes?

`string`[]

#### subjects?

`object`[]

#### suffix?

`string`

#### tableSchema?

`string` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

#### textual?

`boolean`

#### titles?

`object`[]

#### types?

\{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}

#### types.resourceType?

`string`

#### types.resourceTypeGeneral

`"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`

#### unstable_customMetadata?

`Record`\<`string`, `unknown`\>

#### version?

`string`

### options?

`ValidateTableOptions`

## Returns

`Promise`\<\{ `errors`: (\{ `jsonPointer`: `string`; `message`: `string`; `type`: `"metadata"`; \} \| \{ `resourceName`: `string`; `type`: `"resource/missing"`; \} \| \{ `expectedResourceType`: `"data"` \| `"table"`; `type`: `"resource/type"`; \} \| \{ `columnName`: `string`; `type`: `"column/missing"`; \} \| \{ `actualColumnType`: `"string"` \| `"number"` \| `"boolean"` \| `"object"` \| `"date"` \| `"array"` \| `"url"` \| `"integer"` \| `"categorical"` \| `"list"` \| `"date-time"` \| `"time"` \| `"base64"` \| `"hex"` \| `"email"` \| `"duration"` \| `"wkt"` \| `"wkb"` \| `"decimal"` \| `"geojson"` \| `"topojson"` \| `"unknown"`; `columnName`: `string`; `expectedColumnType`: `"string"` \| `"number"` \| `"boolean"` \| `"object"` \| `"date"` \| `"array"` \| `"url"` \| `"integer"` \| `"categorical"` \| `"list"` \| `"date-time"` \| `"time"` \| `"base64"` \| `"hex"` \| `"email"` \| `"duration"` \| `"wkt"` \| `"wkb"` \| `"decimal"` \| `"geojson"` \| `"topojson"` \| `"unknown"`; `type`: `"column/type"`; \} \| \{ `columnNames`: `string`[]; `rowNumber`: `number`; `type`: `"row/primaryKey"`; \} \| \{ `columnNames`: `string`[]; `rowNumber`: `number`; `type`: `"row/uniqueKey"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `columnType`: `"string"` \| `"number"` \| `"boolean"` \| `"object"` \| `"date"` \| `"array"` \| `"url"` \| `"integer"` \| `"categorical"` \| `"list"` \| `"date-time"` \| `"time"` \| `"base64"` \| `"hex"` \| `"email"` \| `"duration"` \| `"wkt"` \| `"wkb"` \| `"decimal"` \| `"geojson"` \| `"topojson"` \| `"unknown"`; `rowNumber`: `number`; `type`: `"cell/type"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `rowNumber`: `number`; `type`: `"cell/required"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `minimum`: `string`; `rowNumber`: `number`; `type`: `"cell/minimum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `maximum`: `string`; `rowNumber`: `number`; `type`: `"cell/maximum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `minimum`: `string`; `rowNumber`: `number`; `type`: `"cell/exclusiveMinimum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `maximum`: `string`; `rowNumber`: `number`; `type`: `"cell/exclusiveMaximum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `multipleOf`: `number`; `rowNumber`: `number`; `type`: `"cell/multipleOf"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `minLength`: `number`; `rowNumber`: `number`; `type`: `"cell/minLength"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `maxLength`: `number`; `rowNumber`: `number`; `type`: `"cell/maxLength"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `minItems`: `number`; `rowNumber`: `number`; `type`: `"cell/minItems"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `maxItems`: `number`; `rowNumber`: `number`; `type`: `"cell/maxItems"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `pattern`: `string`; `rowNumber`: `number`; `type`: `"cell/pattern"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `rowNumber`: `number`; `type`: `"cell/unique"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `const`: `string`; `rowNumber`: `number`; `type`: `"cell/const"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `enum`: `string`[]; `rowNumber`: `number`; `type`: `"cell/enum"`; \} \| \{ `cell`: `string`; `columnName`: `string`; `jsonPointer`: `string`; `message`: `string`; `rowNumber`: `number`; `type`: `"cell/json"`; \} \| \{ `cells`: `string`[]; `foreignKey`: \{ `columns`: `string`[]; `reference`: \{ `columns`: `string`[]; `resource?`: `string`; \}; \}; `type`: `"foreignKey"`; \} \| \{ `jsonPointer`: `string`; `message`: `string`; `type`: `"data"`; \} \| \{ `actualEncoding?`: `string`; `type`: `"file/textual"`; \} \| \{ `actualHash`: `string`; `expectedHash`: `string`; `hashType`: `string`; `type`: `"file/integrity"`; \} \| (\{ type: "metadata"; message: string; jsonPointer: string; \} \| \{ type: "resource/missing"; resourceName: string; \} \| \{ type: "resource/type"; expectedResourceType: "data" \| "table"; \} \| ... 23 more ... \| \{ ...; \}) & \{ ...; \})[]; `valid`: `boolean`; \}\>
