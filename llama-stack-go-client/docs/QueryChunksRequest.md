# QueryChunksRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VectorDbId** | **string** |  | 
**Query** | [**InterleavedContent**](InterleavedContent.md) |  | 
**Params** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewQueryChunksRequest

`func NewQueryChunksRequest(vectorDbId string, query InterleavedContent, ) *QueryChunksRequest`

NewQueryChunksRequest instantiates a new QueryChunksRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryChunksRequestWithDefaults

`func NewQueryChunksRequestWithDefaults() *QueryChunksRequest`

NewQueryChunksRequestWithDefaults instantiates a new QueryChunksRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVectorDbId

`func (o *QueryChunksRequest) GetVectorDbId() string`

GetVectorDbId returns the VectorDbId field if non-nil, zero value otherwise.

### GetVectorDbIdOk

`func (o *QueryChunksRequest) GetVectorDbIdOk() (*string, bool)`

GetVectorDbIdOk returns a tuple with the VectorDbId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVectorDbId

`func (o *QueryChunksRequest) SetVectorDbId(v string)`

SetVectorDbId sets VectorDbId field to given value.


### GetQuery

`func (o *QueryChunksRequest) GetQuery() InterleavedContent`

GetQuery returns the Query field if non-nil, zero value otherwise.

### GetQueryOk

`func (o *QueryChunksRequest) GetQueryOk() (*InterleavedContent, bool)`

GetQueryOk returns a tuple with the Query field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuery

`func (o *QueryChunksRequest) SetQuery(v InterleavedContent)`

SetQuery sets Query field to given value.


### GetParams

`func (o *QueryChunksRequest) GetParams() map[string]AppendRowsRequestRowsInnerValue`

GetParams returns the Params field if non-nil, zero value otherwise.

### GetParamsOk

`func (o *QueryChunksRequest) GetParamsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetParamsOk returns a tuple with the Params field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParams

`func (o *QueryChunksRequest) SetParams(v map[string]AppendRowsRequestRowsInnerValue)`

SetParams sets Params field to given value.

### HasParams

`func (o *QueryChunksRequest) HasParams() bool`

HasParams returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


