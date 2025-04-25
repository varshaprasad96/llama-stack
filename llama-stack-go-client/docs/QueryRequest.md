# QueryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | [**InterleavedContent**](InterleavedContent.md) |  | 
**VectorDbIds** | **[]string** |  | 
**QueryConfig** | Pointer to [**RAGQueryConfig**](RAGQueryConfig.md) |  | [optional] 

## Methods

### NewQueryRequest

`func NewQueryRequest(content InterleavedContent, vectorDbIds []string, ) *QueryRequest`

NewQueryRequest instantiates a new QueryRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryRequestWithDefaults

`func NewQueryRequestWithDefaults() *QueryRequest`

NewQueryRequestWithDefaults instantiates a new QueryRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *QueryRequest) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *QueryRequest) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *QueryRequest) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.


### GetVectorDbIds

`func (o *QueryRequest) GetVectorDbIds() []string`

GetVectorDbIds returns the VectorDbIds field if non-nil, zero value otherwise.

### GetVectorDbIdsOk

`func (o *QueryRequest) GetVectorDbIdsOk() (*[]string, bool)`

GetVectorDbIdsOk returns a tuple with the VectorDbIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVectorDbIds

`func (o *QueryRequest) SetVectorDbIds(v []string)`

SetVectorDbIds sets VectorDbIds field to given value.


### GetQueryConfig

`func (o *QueryRequest) GetQueryConfig() RAGQueryConfig`

GetQueryConfig returns the QueryConfig field if non-nil, zero value otherwise.

### GetQueryConfigOk

`func (o *QueryRequest) GetQueryConfigOk() (*RAGQueryConfig, bool)`

GetQueryConfigOk returns a tuple with the QueryConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryConfig

`func (o *QueryRequest) SetQueryConfig(v RAGQueryConfig)`

SetQueryConfig sets QueryConfig field to given value.

### HasQueryConfig

`func (o *QueryRequest) HasQueryConfig() bool`

HasQueryConfig returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


