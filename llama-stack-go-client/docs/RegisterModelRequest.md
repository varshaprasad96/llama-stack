# RegisterModelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ModelId** | **string** |  | 
**ProviderModelId** | Pointer to **string** |  | [optional] 
**ProviderId** | Pointer to **string** |  | [optional] 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 
**ModelType** | Pointer to [**ModelType**](ModelType.md) |  | [optional] 

## Methods

### NewRegisterModelRequest

`func NewRegisterModelRequest(modelId string, ) *RegisterModelRequest`

NewRegisterModelRequest instantiates a new RegisterModelRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegisterModelRequestWithDefaults

`func NewRegisterModelRequestWithDefaults() *RegisterModelRequest`

NewRegisterModelRequestWithDefaults instantiates a new RegisterModelRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModelId

`func (o *RegisterModelRequest) GetModelId() string`

GetModelId returns the ModelId field if non-nil, zero value otherwise.

### GetModelIdOk

`func (o *RegisterModelRequest) GetModelIdOk() (*string, bool)`

GetModelIdOk returns a tuple with the ModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelId

`func (o *RegisterModelRequest) SetModelId(v string)`

SetModelId sets ModelId field to given value.


### GetProviderModelId

`func (o *RegisterModelRequest) GetProviderModelId() string`

GetProviderModelId returns the ProviderModelId field if non-nil, zero value otherwise.

### GetProviderModelIdOk

`func (o *RegisterModelRequest) GetProviderModelIdOk() (*string, bool)`

GetProviderModelIdOk returns a tuple with the ProviderModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderModelId

`func (o *RegisterModelRequest) SetProviderModelId(v string)`

SetProviderModelId sets ProviderModelId field to given value.

### HasProviderModelId

`func (o *RegisterModelRequest) HasProviderModelId() bool`

HasProviderModelId returns a boolean if a field has been set.

### GetProviderId

`func (o *RegisterModelRequest) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *RegisterModelRequest) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *RegisterModelRequest) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.

### HasProviderId

`func (o *RegisterModelRequest) HasProviderId() bool`

HasProviderId returns a boolean if a field has been set.

### GetMetadata

`func (o *RegisterModelRequest) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *RegisterModelRequest) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *RegisterModelRequest) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *RegisterModelRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetModelType

`func (o *RegisterModelRequest) GetModelType() ModelType`

GetModelType returns the ModelType field if non-nil, zero value otherwise.

### GetModelTypeOk

`func (o *RegisterModelRequest) GetModelTypeOk() (*ModelType, bool)`

GetModelTypeOk returns a tuple with the ModelType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelType

`func (o *RegisterModelRequest) SetModelType(v ModelType)`

SetModelType sets ModelType field to given value.

### HasModelType

`func (o *RegisterModelRequest) HasModelType() bool`

HasModelType returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


