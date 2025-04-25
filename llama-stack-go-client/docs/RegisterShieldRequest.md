# RegisterShieldRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ShieldId** | **string** |  | 
**ProviderShieldId** | Pointer to **string** |  | [optional] 
**ProviderId** | Pointer to **string** |  | [optional] 
**Params** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewRegisterShieldRequest

`func NewRegisterShieldRequest(shieldId string, ) *RegisterShieldRequest`

NewRegisterShieldRequest instantiates a new RegisterShieldRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegisterShieldRequestWithDefaults

`func NewRegisterShieldRequestWithDefaults() *RegisterShieldRequest`

NewRegisterShieldRequestWithDefaults instantiates a new RegisterShieldRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetShieldId

`func (o *RegisterShieldRequest) GetShieldId() string`

GetShieldId returns the ShieldId field if non-nil, zero value otherwise.

### GetShieldIdOk

`func (o *RegisterShieldRequest) GetShieldIdOk() (*string, bool)`

GetShieldIdOk returns a tuple with the ShieldId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShieldId

`func (o *RegisterShieldRequest) SetShieldId(v string)`

SetShieldId sets ShieldId field to given value.


### GetProviderShieldId

`func (o *RegisterShieldRequest) GetProviderShieldId() string`

GetProviderShieldId returns the ProviderShieldId field if non-nil, zero value otherwise.

### GetProviderShieldIdOk

`func (o *RegisterShieldRequest) GetProviderShieldIdOk() (*string, bool)`

GetProviderShieldIdOk returns a tuple with the ProviderShieldId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderShieldId

`func (o *RegisterShieldRequest) SetProviderShieldId(v string)`

SetProviderShieldId sets ProviderShieldId field to given value.

### HasProviderShieldId

`func (o *RegisterShieldRequest) HasProviderShieldId() bool`

HasProviderShieldId returns a boolean if a field has been set.

### GetProviderId

`func (o *RegisterShieldRequest) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *RegisterShieldRequest) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *RegisterShieldRequest) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.

### HasProviderId

`func (o *RegisterShieldRequest) HasProviderId() bool`

HasProviderId returns a boolean if a field has been set.

### GetParams

`func (o *RegisterShieldRequest) GetParams() map[string]AppendRowsRequestRowsInnerValue`

GetParams returns the Params field if non-nil, zero value otherwise.

### GetParamsOk

`func (o *RegisterShieldRequest) GetParamsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetParamsOk returns a tuple with the Params field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParams

`func (o *RegisterShieldRequest) SetParams(v map[string]AppendRowsRequestRowsInnerValue)`

SetParams sets Params field to given value.

### HasParams

`func (o *RegisterShieldRequest) HasParams() bool`

HasParams returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


