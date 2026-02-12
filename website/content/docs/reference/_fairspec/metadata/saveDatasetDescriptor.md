---
editUrl: false
next: false
prev: false
title: "saveDatasetDescriptor"
---

> **saveDatasetDescriptor**(`dataset`, `options`): `Promise`\<`void`\>

Defined in: [metadata/actions/dataset/save.ts:11](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/metadata/actions/dataset/save.ts#L11)

Save a Dataset to a file path
Works in Node.js environments

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

#### overwrite?

`boolean`

#### path

`string`

## Returns

`Promise`\<`void`\>
