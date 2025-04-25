# RegisterVectorDbRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VectorDbId** | **string** |  | 
**EmbeddingModel** | **string** |  | 
**EmbeddingDimension** | Pointer to **int32** |  | [optional] 
**ProviderId** | Pointer to **string** |  | [optional] 
**ProviderVectorDbId** | Pointer to **string** |  | [optional] 

## Methods

### NewRegisterVectorDbRequest

`func NewRegisterVectorDbRequest(vectorDbId string, embeddingModel string, ) *RegisterVectorDbRequest`

NewRegisterVectorDbRequest instantiates a new RegisterVectorDbRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegisterVectorDbRequestWithDefaults

`func NewRegisterVectorDbRequestWithDefaults() *RegisterVectorDbRequest`

NewRegisterVectorDbRequestWithDefaults instantiates a new RegisterVectorDbRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVectorDbId

`func (o *RegisterVectorDbRequest) GetVectorDbId() string`

GetVectorDbId returns the VectorDbId field if non-nil, zero value otherwise.

### GetVectorDbIdOk

`func (o *RegisterVectorDbRequest) GetVectorDbIdOk() (*string, bool)`

GetVectorDbIdOk returns a tuple with the VectorDbId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVectorDbId

`func (o *RegisterVectorDbRequest) SetVectorDbId(v string)`

SetVectorDbId sets VectorDbId field to given value.


### GetEmbeddingModel

`func (o *RegisterVectorDbRequest) GetEmbeddingModel() string`

GetEmbeddingModel returns the EmbeddingModel field if non-nil, zero value otherwise.

### GetEmbeddingModelOk

`func (o *RegisterVectorDbRequest) GetEmbeddingModelOk() (*string, bool)`

GetEmbeddingModelOk returns a tuple with the EmbeddingModel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddingModel

`func (o *RegisterVectorDbRequest) SetEmbeddingModel(v string)`

SetEmbeddingModel sets EmbeddingModel field to given value.


### GetEmbeddingDimension

`func (o *RegisterVectorDbRequest) GetEmbeddingDimension() int32`

GetEmbeddingDimension returns the EmbeddingDimension field if non-nil, zero value otherwise.

### GetEmbeddingDimensionOk

`func (o *RegisterVectorDbRequest) GetEmbeddingDimensionOk() (*int32, bool)`

GetEmbeddingDimensionOk returns a tuple with the EmbeddingDimension field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddingDimension

`func (o *RegisterVectorDbRequest) SetEmbeddingDimension(v int32)`

SetEmbeddingDimension sets EmbeddingDimension field to given value.

### HasEmbeddingDimension

`func (o *RegisterVectorDbRequest) HasEmbeddingDimension() bool`

HasEmbeddingDimension returns a boolean if a field has been set.

### GetProviderId

`func (o *RegisterVectorDbRequest) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *RegisterVectorDbRequest) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *RegisterVectorDbRequest) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.

### HasProviderId

`func (o *RegisterVectorDbRequest) HasProviderId() bool`

HasProviderId returns a boolean if a field has been set.

### GetProviderVectorDbId

`func (o *RegisterVectorDbRequest) GetProviderVectorDbId() string`

GetProviderVectorDbId returns the ProviderVectorDbId field if non-nil, zero value otherwise.

### GetProviderVectorDbIdOk

`func (o *RegisterVectorDbRequest) GetProviderVectorDbIdOk() (*string, bool)`

GetProviderVectorDbIdOk returns a tuple with the ProviderVectorDbId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderVectorDbId

`func (o *RegisterVectorDbRequest) SetProviderVectorDbId(v string)`

SetProviderVectorDbId sets ProviderVectorDbId field to given value.

### HasProviderVectorDbId

`func (o *RegisterVectorDbRequest) HasProviderVectorDbId() bool`

HasProviderVectorDbId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


