---
editUrl: false
next: false
prev: false
title: "ZipPlugin"
---

Defined in: [dataset/plugins/zip/plugin.ts:7](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/dataset/plugins/zip/plugin.ts#L7)

## Implements

- [`DatasetPlugin`](/reference/_fairspec/dataset/datasetplugin/)

## Constructors

### Constructor

> **new ZipPlugin**(): `ZipPlugin`

#### Returns

`ZipPlugin`

## Methods

### loadDataset()

> **loadDataset**(`source`): `Promise`\<`undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}\>

Defined in: [dataset/plugins/zip/plugin.ts:8](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/dataset/plugins/zip/plugin.ts#L8)

#### Parameters

##### source

`string`

#### Returns

`Promise`\<`undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}\>

#### Implementation of

[`DatasetPlugin`](/reference/_fairspec/dataset/datasetplugin/).[`loadDataset`](/reference/_fairspec/dataset/datasetplugin/#loaddataset)

***

### saveDataset()

> **saveDataset**(`dataset`, `options`): `Promise`\<`undefined` \| \{ `path`: `undefined`; \}\>

Defined in: [dataset/plugins/zip/plugin.ts:16](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/dataset/plugins/zip/plugin.ts#L16)

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

###### target

`string`

###### withRemote?

`boolean`

#### Returns

`Promise`\<`undefined` \| \{ `path`: `undefined`; \}\>

#### Implementation of

[`DatasetPlugin`](/reference/_fairspec/dataset/datasetplugin/).[`saveDataset`](/reference/_fairspec/dataset/datasetplugin/#savedataset)
