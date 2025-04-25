# RAGDocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DocumentId** | **string** | The unique identifier for the document. | 
**Content** | [**RAGDocumentContent**](RAGDocumentContent.md) |  | 
**MimeType** | Pointer to **string** | The MIME type of the document. | [optional] 
**Metadata** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | Additional metadata for the document. | 

## Methods

### NewRAGDocument

`func NewRAGDocument(documentId string, content RAGDocumentContent, metadata map[string]AppendRowsRequestRowsInnerValue, ) *RAGDocument`

NewRAGDocument instantiates a new RAGDocument object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRAGDocumentWithDefaults

`func NewRAGDocumentWithDefaults() *RAGDocument`

NewRAGDocumentWithDefaults instantiates a new RAGDocument object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDocumentId

`func (o *RAGDocument) GetDocumentId() string`

GetDocumentId returns the DocumentId field if non-nil, zero value otherwise.

### GetDocumentIdOk

`func (o *RAGDocument) GetDocumentIdOk() (*string, bool)`

GetDocumentIdOk returns a tuple with the DocumentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDocumentId

`func (o *RAGDocument) SetDocumentId(v string)`

SetDocumentId sets DocumentId field to given value.


### GetContent

`func (o *RAGDocument) GetContent() RAGDocumentContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *RAGDocument) GetContentOk() (*RAGDocumentContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *RAGDocument) SetContent(v RAGDocumentContent)`

SetContent sets Content field to given value.


### GetMimeType

`func (o *RAGDocument) GetMimeType() string`

GetMimeType returns the MimeType field if non-nil, zero value otherwise.

### GetMimeTypeOk

`func (o *RAGDocument) GetMimeTypeOk() (*string, bool)`

GetMimeTypeOk returns a tuple with the MimeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeType

`func (o *RAGDocument) SetMimeType(v string)`

SetMimeType sets MimeType field to given value.

### HasMimeType

`func (o *RAGDocument) HasMimeType() bool`

HasMimeType returns a boolean if a field has been set.

### GetMetadata

`func (o *RAGDocument) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *RAGDocument) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *RAGDocument) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


