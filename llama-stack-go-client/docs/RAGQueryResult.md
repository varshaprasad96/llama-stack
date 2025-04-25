# RAGQueryResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | Pointer to [**InterleavedContent**](InterleavedContent.md) |  | [optional] 
**Metadata** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewRAGQueryResult

`func NewRAGQueryResult(metadata map[string]AppendRowsRequestRowsInnerValue, ) *RAGQueryResult`

NewRAGQueryResult instantiates a new RAGQueryResult object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRAGQueryResultWithDefaults

`func NewRAGQueryResultWithDefaults() *RAGQueryResult`

NewRAGQueryResultWithDefaults instantiates a new RAGQueryResult object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *RAGQueryResult) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *RAGQueryResult) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *RAGQueryResult) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.

### HasContent

`func (o *RAGQueryResult) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetMetadata

`func (o *RAGQueryResult) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *RAGQueryResult) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *RAGQueryResult) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


