# InsertRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Documents** | [**[]RAGDocument**](RAGDocument.md) |  | 
**VectorDbId** | **string** |  | 
**ChunkSizeInTokens** | **int32** |  | 

## Methods

### NewInsertRequest

`func NewInsertRequest(documents []RAGDocument, vectorDbId string, chunkSizeInTokens int32, ) *InsertRequest`

NewInsertRequest instantiates a new InsertRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInsertRequestWithDefaults

`func NewInsertRequestWithDefaults() *InsertRequest`

NewInsertRequestWithDefaults instantiates a new InsertRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDocuments

`func (o *InsertRequest) GetDocuments() []RAGDocument`

GetDocuments returns the Documents field if non-nil, zero value otherwise.

### GetDocumentsOk

`func (o *InsertRequest) GetDocumentsOk() (*[]RAGDocument, bool)`

GetDocumentsOk returns a tuple with the Documents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDocuments

`func (o *InsertRequest) SetDocuments(v []RAGDocument)`

SetDocuments sets Documents field to given value.


### GetVectorDbId

`func (o *InsertRequest) GetVectorDbId() string`

GetVectorDbId returns the VectorDbId field if non-nil, zero value otherwise.

### GetVectorDbIdOk

`func (o *InsertRequest) GetVectorDbIdOk() (*string, bool)`

GetVectorDbIdOk returns a tuple with the VectorDbId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVectorDbId

`func (o *InsertRequest) SetVectorDbId(v string)`

SetVectorDbId sets VectorDbId field to given value.


### GetChunkSizeInTokens

`func (o *InsertRequest) GetChunkSizeInTokens() int32`

GetChunkSizeInTokens returns the ChunkSizeInTokens field if non-nil, zero value otherwise.

### GetChunkSizeInTokensOk

`func (o *InsertRequest) GetChunkSizeInTokensOk() (*int32, bool)`

GetChunkSizeInTokensOk returns a tuple with the ChunkSizeInTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChunkSizeInTokens

`func (o *InsertRequest) SetChunkSizeInTokens(v int32)`

SetChunkSizeInTokens sets ChunkSizeInTokens field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


