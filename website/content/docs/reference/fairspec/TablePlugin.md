---
editUrl: false
next: false
prev: false
title: "TablePlugin"
---

Defined in: table/build/plugin.d.ts:14

## Extends

- [`DatasetPlugin`](/reference/fairspec/datasetplugin/)

## Methods

### convertDatasetFrom()?

> `optional` **convertDatasetFrom**(`descriptor`, `options`): `undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}

Defined in: metadata/build/plugin.d.ts:12

#### Parameters

##### descriptor

[`Descriptor`](/reference/fairspec/descriptor/)

##### options

###### format

`string`

#### Returns

`undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`convertDatasetFrom`](/reference/fairspec/datasetplugin/#convertdatasetfrom)

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

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`convertDatasetTo`](/reference/fairspec/datasetplugin/#convertdatasetto)

***

### convertTableSchemaFrom()?

> `optional` **convertTableSchemaFrom**(`descriptor`, `options`): `undefined` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: `string`; `value`: `number`; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

Defined in: metadata/build/plugin.d.ts:24

#### Parameters

##### descriptor

[`Descriptor`](/reference/fairspec/descriptor/)

##### options

###### format

`string`

#### Returns

`undefined` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: `string`; `value`: `number`; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: ... \| ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: `string`; `value`: `string`; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`convertTableSchemaFrom`](/reference/fairspec/datasetplugin/#converttableschemafrom)

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

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`convertTableSchemaTo`](/reference/fairspec/datasetplugin/#converttableschemato)

***

### inferFormat()?

> `optional` **inferFormat**(`resource`, `options?`): `Promise`\<`undefined` \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `delimiter?`: `string`; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `lineTerminator?`: `string`; `name`: `"csv"`; `nullSequence?`: `string`; `quoteChar?`: `string`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `lineTerminator?`: `string`; `name`: `"tsv"`; `nullSequence?`: `string`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `jsonPointer?`: `string`; `name`: `"json"`; `rowType?`: `"object"` \| `"array"`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"jsonl"`; `rowType?`: `"object"` \| `"array"`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"xlsx"`; `sheetName?`: `string`; `sheetNumber?`: `number`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"ods"`; `sheetName?`: `string`; `sheetNumber?`: `number`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"sqlite"`; `tableName?`: `string`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"parquet"`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"arrow"`; `title?`: `string`; \} \| \{ `description?`: `string`; `name?`: `undefined`; `title?`: `string`; \}\>

Defined in: dataset/build/plugin.d.ts:14

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

`string` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

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

[`InferFormatOptions`](/reference/fairspec/inferformatoptions/)

#### Returns

`Promise`\<`undefined` \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `delimiter?`: `string`; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `lineTerminator?`: `string`; `name`: `"csv"`; `nullSequence?`: `string`; `quoteChar?`: `string`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `lineTerminator?`: `string`; `name`: `"tsv"`; `nullSequence?`: `string`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `jsonPointer?`: `string`; `name`: `"json"`; `rowType?`: `"object"` \| `"array"`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"jsonl"`; `rowType?`: `"object"` \| `"array"`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"xlsx"`; `sheetName?`: `string`; `sheetNumber?`: `number`; `title?`: `string`; \} \| \{ `columnNames?`: `string`[]; `commentPrefix?`: `string`; `commentRows?`: `number`[]; `description?`: `string`; `headerJoin?`: `string`; `headerRows?`: `false` \| `number`[]; `name`: `"ods"`; `sheetName?`: `string`; `sheetNumber?`: `number`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"sqlite"`; `tableName?`: `string`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"parquet"`; `title?`: `string`; \} \| \{ `description?`: `string`; `name`: `"arrow"`; `title?`: `string`; \} \| \{ `description?`: `string`; `name?`: `undefined`; `title?`: `string`; \}\>

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`inferFormat`](/reference/fairspec/datasetplugin/#inferformat)

***

### inferTableSchema()?

> `optional` **inferTableSchema**(`resource`, `options?`): `Promise`\<`undefined` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}\>

Defined in: table/build/plugin.d.ts:22

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

`string` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

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

[`InferTableSchemaOptions`](/reference/fairspec/infertableschemaoptions/)

#### Returns

`Promise`\<`undefined` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}\>

***

### loadDataset()?

> `optional` **loadDataset**(`source`): `Promise`\<`undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}\>

Defined in: dataset/build/plugin.d.ts:10

#### Parameters

##### source

`string`

#### Returns

`Promise`\<`undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}\>

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`loadDataset`](/reference/fairspec/datasetplugin/#loaddataset)

***

### loadTable()?

> `optional` **loadTable**(`resource`, `options?`): `Promise`\<`undefined` \| [`Table`](/reference/fairspec/table/)\>

Defined in: table/build/plugin.d.ts:20

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

`string` \| \{ `$schema?`: `string`; `description?`: `string`; `foreignKeys?`: `object`[]; `missingValues?`: (`string` \| `number` \| \{ `label`: `string`; `value`: `string` \| `number`; \})[]; `primaryKey?`: `string`[]; `properties?`: `Record`\<`string`, \{ `const?`: `boolean`; `default?`: `boolean`[]; `description?`: `string`; `enum?`: `boolean`[]; `examples?`: `boolean`[]; `falseValues?`: `string`[]; `format?`: `undefined`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `trueValues?`: `string`[]; `type`: `"boolean"`; \} \| \{ `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withText?`: `boolean`; \} \| \{ `categories?`: (`number` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `number`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"categorical"`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"integer"`; `withOrder?`: `boolean`; `withText?`: `boolean`; \} \| \{ `const?`: `number`; `decimalChar?`: `string`; `default?`: `number`[]; `description?`: `string`; `enum?`: `number`[]; `examples?`: `number`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format?`: `undefined`; `groupChar?`: `string`; `maximum?`: `number`; `minimum?`: `number`; `missingValues?`: (`string` \| `number` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `rdfType?`: `string`; `title?`: `string`; `type`: `"number"`; `withText?`: `boolean`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `delimiter?`: `string`; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"list"`; `itemType?`: `"string"` \| `"number"` \| `"boolean"` \| `"date"` \| `"integer"` \| `"date-time"` \| `"time"`; `maxItems?`: `number`; `maxLength?`: `number`; `minItems?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"base64"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"hex"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"email"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"url"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date-time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"date"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"time"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `temporalFormat?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"duration"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkt"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"wkb"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format?`: `undefined`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; \} \| \{ `categories?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `const?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `format`: `"categorical"`; `maxLength?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withOrder?`: `boolean`; \} \| \{ `const?`: `string`; `decimalChar?`: `string`; `default?`: `string`[]; `description?`: `string`; `enum?`: `string`[]; `examples?`: `string`[]; `exclusiveMaximum?`: `number`; `exclusiveMinimum?`: `number`; `format`: `"decimal"`; `groupChar?`: `string`; `maximum?`: `number`; `maxLength?`: `number`; `minimum?`: `number`; `minLength?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `multipleOf?`: `number`; `pattern?`: `string`; `rdfType?`: `string`; `title?`: `string`; `type`: `"string"`; `withText?`: `boolean`; \} \| \{ `additionalItems?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `unknown`[]; `contains?`: `unknown`; `default?`: `unknown`[][]; `description?`: `string`; `else?`: `unknown`; `enum?`: `unknown`[]; `examples?`: `unknown`[][]; `format?`: `undefined`; `if?`: `unknown`; `items?`: `unknown`; `maxContains?`: `number`; `maxItems?`: `number`; `minContains?`: `number`; `minItems?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `prefixItems?`: `unknown`; `rdfType?`: `string`; `then?`: `unknown`; `title?`: `string`; `type`: `"array"`; `uniqueItems?`: `boolean`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"geojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format`: `"topojson"`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `additionalProperties?`: `unknown`; `allOf?`: `unknown`; `anyOf?`: `unknown`; `const?`: `Record`\<`string`, `unknown`\>; `default?`: `Record`\<`string`, `unknown`\>[]; `dependencies?`: `unknown`; `dependentRequired?`: `unknown`; `dependentSchemas?`: `unknown`; `description?`: `string`; `else?`: `unknown`; `enum?`: `Record`\<`string`, `unknown`\>[]; `examples?`: `Record`\<`string`, `unknown`\>[]; `format?`: `undefined`; `if?`: `unknown`; `maxProperties?`: `number`; `minProperties?`: `number`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `not?`: `unknown`; `oneOf?`: `unknown`; `patternProperties?`: `unknown`; `properties?`: `unknown`; `propertyNames?`: `unknown`; `rdfType?`: `string`; `required?`: `unknown`; `then?`: `unknown`; `title?`: `string`; `type`: `"object"`; \} \| \{ `const?`: `unknown`[]; `default?`: `unknown`[]; `description?`: `string`; `enum?`: `unknown`[][]; `examples?`: `unknown`[][]; `format?`: `undefined`; `missingValues?`: (`string` \| \{ `label`: ...; `value`: ...; \})[]; `rdfType?`: `string`; `title?`: `string`; `type?`: `"null"`; \}\>; `required?`: `string`[]; `title?`: `string`; `uniqueKeys?`: `string`[][]; \}

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

[`LoadTableOptions`](/reference/fairspec/loadtableoptions/)

#### Returns

`Promise`\<`undefined` \| [`Table`](/reference/fairspec/table/)\>

***

### renderDataSchemaAs()?

> `optional` **renderDataSchemaAs**(`dataSchema`, `options`): `undefined` \| `string`

Defined in: metadata/build/plugin.d.ts:15

#### Parameters

##### dataSchema

[`DataSchema`](/reference/fairspec/dataschema/)

##### options

###### format

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`renderDataSchemaAs`](/reference/fairspec/datasetplugin/#renderdataschemaas)

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

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`renderDatasetAs`](/reference/fairspec/datasetplugin/#renderdatasetas)

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

#### Inherited from

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`renderTableSchemaAs`](/reference/fairspec/datasetplugin/#rendertableschemaas)

***

### saveDataset()?

> `optional` **saveDataset**(`dataset`, `options`): `Promise`\<`undefined` \| \{ `path?`: `string`; \}\>

Defined in: table/build/plugin.d.ts:15

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

[`SaveDatasetOptions`](/reference/fairspec/savedatasetoptions/) & `object`

#### Returns

`Promise`\<`undefined` \| \{ `path?`: `string`; \}\>

#### Overrides

[`DatasetPlugin`](/reference/fairspec/datasetplugin/).[`saveDataset`](/reference/fairspec/datasetplugin/#savedataset)

***

### saveTable()?

> `optional` **saveTable**(`table`, `options`): `Promise`\<`undefined` \| `string`\>

Defined in: table/build/plugin.d.ts:21

#### Parameters

##### table

[`Table`](/reference/fairspec/table/)

##### options

[`SaveTableOptions`](/reference/fairspec/savetableoptions/)

#### Returns

`Promise`\<`undefined` \| `string`\>
