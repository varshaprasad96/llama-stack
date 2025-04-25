# Shield

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Identifier** | **string** |  | 
**ProviderResourceId** | **string** |  | 
**ProviderId** | **string** |  | 
**Type** | **string** |  | [default to "shield"]
**Params** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewShield

`func NewShield(identifier string, providerResourceId string, providerId string, type_ string, ) *Shield`

NewShield instantiates a new Shield object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewShieldWithDefaults

`func NewShieldWithDefaults() *Shield`

NewShieldWithDefaults instantiates a new Shield object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdentifier

`func (o *Shield) GetIdentifier() string`

GetIdentifier returns the Identifier field if non-nil, zero value otherwise.

### GetIdentifierOk

`func (o *Shield) GetIdentifierOk() (*string, bool)`

GetIdentifierOk returns a tuple with the Identifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifier

`func (o *Shield) SetIdentifier(v string)`

SetIdentifier sets Identifier field to given value.


### GetProviderResourceId

`func (o *Shield) GetProviderResourceId() string`

GetProviderResourceId returns the ProviderResourceId field if non-nil, zero value otherwise.

### GetProviderResourceIdOk

`func (o *Shield) GetProviderResourceIdOk() (*string, bool)`

GetProviderResourceIdOk returns a tuple with the ProviderResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderResourceId

`func (o *Shield) SetProviderResourceId(v string)`

SetProviderResourceId sets ProviderResourceId field to given value.


### GetProviderId

`func (o *Shield) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *Shield) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *Shield) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetType

`func (o *Shield) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Shield) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Shield) SetType(v string)`

SetType sets Type field to given value.


### GetParams

`func (o *Shield) GetParams() map[string]AppendRowsRequestRowsInnerValue`

GetParams returns the Params field if non-nil, zero value otherwise.

### GetParamsOk

`func (o *Shield) GetParamsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetParamsOk returns a tuple with the Params field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParams

`func (o *Shield) SetParams(v map[string]AppendRowsRequestRowsInnerValue)`

SetParams sets Params field to given value.

### HasParams

`func (o *Shield) HasParams() bool`

HasParams returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


