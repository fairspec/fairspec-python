---
editUrl: false
next: false
prev: false
title: "ZenodoPlugin"
---

Defined in: [dataset/plugins/zenodo/plugin.ts:5](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/dataset/plugins/zenodo/plugin.ts#L5)

## Implements

- [`DatasetPlugin`](/reference/_fairspec/dataset/datasetplugin/)

## Constructors

### Constructor

> **new ZenodoPlugin**(): `ZenodoPlugin`

#### Returns

`ZenodoPlugin`

## Methods

### loadDataset()

> **loadDataset**(`source`): `Promise`\<`undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}\>

Defined in: [dataset/plugins/zenodo/plugin.ts:6](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/dataset/plugins/zenodo/plugin.ts#L6)

#### Parameters

##### source

`string`

#### Returns

`Promise`\<`undefined` \| \{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}\>

#### Implementation of

[`DatasetPlugin`](/reference/_fairspec/dataset/datasetplugin/).[`loadDataset`](/reference/_fairspec/dataset/datasetplugin/#loaddataset)
