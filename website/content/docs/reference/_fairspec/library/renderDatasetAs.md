---
editUrl: false
next: false
prev: false
title: "renderDatasetAs"
---

> **renderDatasetAs**(`dataset`, `options`): `Promise`\<`string`\>

Defined in: [library/actions/dataset/render.ts:4](https://github.com/fairspec/fairspec-typescript/blob/803775fa64a99d4fa42ce85a2ad241f930b9f96a/library/actions/dataset/render.ts#L4)

## Parameters

### dataset

#### $schema?

`string`

#### alternateIdentifiers?

`object`[]

#### contributors?

`object`[]

#### creators?

`object`[]

#### dates?

`object`[]

#### descriptions?

`object`[]

#### doi?

`string`

#### formats?

`string`[]

#### fundingReferences?

`object`[]

#### geoLocations?

`object`[]

#### language?

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

#### resources?

`object`[]

#### rightsList?

`object`[]

#### sizes?

`string`[]

#### subjects?

`object`[]

#### suffix?

`string`

#### titles?

`object`[]

#### types?

\{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}

#### types.resourceType?

`string`

#### types.resourceTypeGeneral

`"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`

#### version?

`string`

### options

#### format

`string`

## Returns

`Promise`\<`string`\>
