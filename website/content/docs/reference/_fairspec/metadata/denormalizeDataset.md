---
editUrl: false
next: false
prev: false
title: "denormalizeDataset"
---

> **denormalizeDataset**(`dataset`, `options`): `object`

Defined in: [metadata/actions/dataset/denormalize.ts:5](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/metadata/actions/dataset/denormalize.ts#L5)

## Parameters

### dataset

#### $schema?

`string` = `...`

#### alternateIdentifiers?

`object`[] = `...`

#### contributors?

`object`[] = `...`

#### creators?

`object`[] = `...`

#### dates?

`object`[] = `...`

#### descriptions?

`object`[] = `...`

#### doi?

`string` = `...`

#### formats?

`string`[] = `...`

#### fundingReferences?

`object`[] = `...`

#### geoLocations?

`object`[] = `...`

#### language?

`string` = `...`

#### prefix?

`string` = `...`

#### publicationYear?

`string` = `...`

#### publisher?

\{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \} = `...`

#### publisher.lang?

`string` = `...`

#### publisher.name

`string` = `...`

#### publisher.publisherIdentifier?

`string` = `...`

#### publisher.publisherIdentifierScheme?

`string` = `...`

#### publisher.schemeUri?

`string` = `...`

#### relatedIdentifiers?

`object`[] = `...`

#### relatedItems?

`object`[] = `...`

#### resources?

`object`[] = `...`

#### rightsList?

`object`[] = `...`

#### sizes?

`string`[] = `...`

#### subjects?

`object`[] = `...`

#### suffix?

`string` = `...`

#### titles?

`object`[] = `...`

#### types?

\{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \} = `...`

#### types.resourceType?

`string` = `...`

#### types.resourceTypeGeneral

`"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"` = `...`

#### version?

`string` = `...`

### options

#### basepath?

`string`

## Returns

`object`

### $schema?

> `optional` **$schema**: `string`

### alternateIdentifiers?

> `optional` **alternateIdentifiers**: `object`[]

### contributors?

> `optional` **contributors**: `object`[]

### creators?

> `optional` **creators**: `object`[]

### dates?

> `optional` **dates**: `object`[]

### descriptions?

> `optional` **descriptions**: `object`[]

### doi?

> `optional` **doi**: `string`

### formats?

> `optional` **formats**: `string`[]

### fundingReferences?

> `optional` **fundingReferences**: `object`[]

### geoLocations?

> `optional` **geoLocations**: `object`[]

### language?

> `optional` **language**: `string`

### prefix?

> `optional` **prefix**: `string`

### publicationYear?

> `optional` **publicationYear**: `string`

### publisher?

> `optional` **publisher**: `object`

#### publisher.lang?

> `optional` **lang**: `string`

#### publisher.name

> **name**: `string`

#### publisher.publisherIdentifier?

> `optional` **publisherIdentifier**: `string`

#### publisher.publisherIdentifierScheme?

> `optional` **publisherIdentifierScheme**: `string`

#### publisher.schemeUri?

> `optional` **schemeUri**: `string`

### relatedIdentifiers?

> `optional` **relatedIdentifiers**: `object`[]

### relatedItems?

> `optional` **relatedItems**: `object`[]

### resources?

> `optional` **resources**: `object`[]

### rightsList?

> `optional` **rightsList**: `object`[]

### sizes?

> `optional` **sizes**: `string`[]

### subjects?

> `optional` **subjects**: `object`[]

### suffix?

> `optional` **suffix**: `string`

### titles?

> `optional` **titles**: `object`[]

### types?

> `optional` **types**: `object`

#### types.resourceType?

> `optional` **resourceType**: `string`

#### types.resourceTypeGeneral

> **resourceTypeGeneral**: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`

### version?

> `optional` **version**: `string`
