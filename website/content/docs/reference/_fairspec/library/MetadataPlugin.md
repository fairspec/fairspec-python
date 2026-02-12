---
editUrl: false
next: false
prev: false
title: "MetadataPlugin"
---

Defined in: metadata/build/plugin.d.ts:5

## Extended by

- [`DatasetPlugin`](/reference/_fairspec/library/datasetplugin/)

## Methods

### convertDatasetFrom()?

> `optional` **convertDatasetFrom**(`descriptor`, `options`): `undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}

Defined in: metadata/build/plugin.d.ts:12

#### Parameters

##### descriptor

[`Descriptor`](/reference/_fairspec/library/descriptor/)

##### options

###### format

`string`

#### Returns

`undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}

***

### convertDatasetTo()?

> `optional` **convertDatasetTo**(`dataset`, `options`): `undefined` \| `Record`\<`string`, `unknown`\>

Defined in: metadata/build/plugin.d.ts:9

#### Parameters

##### dataset

###### $schema?

`string`

###### alternateIdentifiers?

`object`[]

###### contributors?

`object`[]

###### creators?

`object`[]

###### dates?

`object`[]

###### descriptions?

`object`[]

###### doi?

`string`

###### formats?

`string`[]

###### fundingReferences?

`object`[]

###### geoLocations?

`object`[]

###### language?

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

###### resources?

`object`[]

###### rightsList?

`object`[]

###### sizes?

`string`[]

###### subjects?

`object`[]

###### suffix?

`string`

###### titles?

`object`[]

###### types?

\{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}

###### types.resourceType?

`string`

###### types.resourceTypeGeneral

`"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`

###### version?

`string`

##### options

###### format

`string`

#### Returns

`undefined` \| `Record`\<`string`, `unknown`\>

***

### convertTableSchemaFrom()?

> `optional` **convertTableSchemaFrom**(`descriptor`, `options`): `undefined` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: `string`; `value`: `number`; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

Defined in: metadata/build/plugin.d.ts:24

#### Parameters

##### descriptor

[`Descriptor`](/reference/_fairspec/library/descriptor/)

##### options

###### format

`string`

#### Returns

`undefined` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: `string`; `value`: `number`; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

***

### convertTableSchemaTo()?

> `optional` **convertTableSchemaTo**(`tableSchema`, `options`): `undefined` \| `Record`\<`string`, `unknown`\>

Defined in: metadata/build/plugin.d.ts:21

#### Parameters

##### tableSchema

###### $schema?

`string`

###### description?

`string`

###### foreignKeys?

`object`[]

###### missingValues?

(`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]

###### primaryKey?

`string`[]

###### properties?

`Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: `string`; `value`: `number`; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>

###### required?

`string`[]

###### title?

`string`

###### uniqueKeys?

`string`[][]

##### options

###### format

`string`

#### Returns

`undefined` \| `Record`\<`string`, `unknown`\>

***

### renderDataSchemaAs()?

> `optional` **renderDataSchemaAs**(`dataSchema`, `options`): `undefined` \| `string`

Defined in: metadata/build/plugin.d.ts:15

#### Parameters

##### dataSchema

[`DataSchema`](/reference/_fairspec/library/dataschema/)

##### options

###### format

`string`

#### Returns

`undefined` \| `string`

***

### renderDatasetAs()?

> `optional` **renderDatasetAs**(`dataset`, `options`): `undefined` \| `string`

Defined in: metadata/build/plugin.d.ts:6

#### Parameters

##### dataset

###### $schema?

`string`

###### alternateIdentifiers?

`object`[]

###### contributors?

`object`[]

###### creators?

`object`[]

###### dates?

`object`[]

###### descriptions?

`object`[]

###### doi?

`string`

###### formats?

`string`[]

###### fundingReferences?

`object`[]

###### geoLocations?

`object`[]

###### language?

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

###### resources?

`object`[]

###### rightsList?

`object`[]

###### sizes?

`string`[]

###### subjects?

`object`[]

###### suffix?

`string`

###### titles?

`object`[]

###### types?

\{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}

###### types.resourceType?

`string`

###### types.resourceTypeGeneral

`"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`

###### version?

`string`

##### options

###### format

`string`

#### Returns

`undefined` \| `string`

***

### renderTableSchemaAs()?

> `optional` **renderTableSchemaAs**(`tableSchema`, `options`): `undefined` \| `string`

Defined in: metadata/build/plugin.d.ts:18

#### Parameters

##### tableSchema

###### $schema?

`string`

###### description?

`string`

###### foreignKeys?

`object`[]

###### missingValues?

(`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]

###### primaryKey?

`string`[]

###### properties?

`Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: `string`; `value`: `number`; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>

###### required?

`string`[]

###### title?

`string`

###### uniqueKeys?

`string`[][]

##### options

###### format

`string`

#### Returns

`undefined` \| `string`
