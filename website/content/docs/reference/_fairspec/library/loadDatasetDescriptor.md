---
editUrl: false
next: false
prev: false
title: "loadDatasetDescriptor"
---

> **loadDatasetDescriptor**(`path`): `Promise`\<\{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}\>

Defined in: metadata/build/actions/dataset/load.d.ts:5

Load a Dataset descriptor (JSON Object) from a file or URL
Ensures the descriptor is valid against its profile

## Parameters

### path

`string`

## Returns

`Promise`\<\{ `$schema?`: `string`; `alternateIdentifiers?`: `object`[]; `contributors?`: `object`[]; `creators?`: `object`[]; `dates?`: `object`[]; `descriptions?`: `object`[]; `doi?`: `string`; `formats?`: `string`[]; `fundingReferences?`: `object`[]; `geoLocations?`: `object`[]; `language?`: `string`; `prefix?`: `string`; `publicationYear?`: `string`; `publisher?`: \{ `lang?`: `string`; `name`: `string`; `publisherIdentifier?`: `string`; `publisherIdentifierScheme?`: `string`; `schemeUri?`: `string`; \}; `relatedIdentifiers?`: `object`[]; `relatedItems?`: `object`[]; `resources?`: `object`[]; `rightsList?`: `object`[]; `sizes?`: `string`[]; `subjects?`: `object`[]; `suffix?`: `string`; `titles?`: `object`[]; `types?`: \{ `resourceType?`: `string`; `resourceTypeGeneral`: `"Other"` \| `"Audiovisual"` \| `"Award"` \| `"Book"` \| `"BookChapter"` \| `"Collection"` \| `"ComputationalNotebook"` \| `"ConferencePaper"` \| `"ConferenceProceeding"` \| `"DataPaper"` \| `"Dataset"` \| `"Dissertation"` \| `"Event"` \| `"Image"` \| `"Instrument"` \| `"InteractiveResource"` \| `"Journal"` \| `"JournalArticle"` \| `"Model"` \| `"OutputManagementPlan"` \| `"PeerReview"` \| `"PhysicalObject"` \| `"Preprint"` \| `"Project"` \| `"Report"` \| `"Service"` \| `"Software"` \| `"Sound"` \| `"Standard"` \| `"StudyRegistration"` \| `"Text"` \| `"Workflow"`; \}; `version?`: `string`; \}\>
