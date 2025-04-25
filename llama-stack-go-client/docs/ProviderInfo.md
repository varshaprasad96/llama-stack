# ProviderInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Api** | **string** |  | 
**ProviderId** | **string** |  | 
**ProviderType** | **string** |  | 
**Config** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 
**Health** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewProviderInfo

`func NewProviderInfo(api string, providerId string, providerType string, config map[string]AppendRowsRequestRowsInnerValue, health map[string]AppendRowsRequestRowsInnerValue, ) *ProviderInfo`

NewProviderInfo instantiates a new ProviderInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProviderInfoWithDefaults

`func NewProviderInfoWithDefaults() *ProviderInfo`

NewProviderInfoWithDefaults instantiates a new ProviderInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApi

`func (o *ProviderInfo) GetApi() string`

GetApi returns the Api field if non-nil, zero value otherwise.

### GetApiOk

`func (o *ProviderInfo) GetApiOk() (*string, bool)`

GetApiOk returns a tuple with the Api field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApi

`func (o *ProviderInfo) SetApi(v string)`

SetApi sets Api field to given value.


### GetProviderId

`func (o *ProviderInfo) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *ProviderInfo) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *ProviderInfo) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetProviderType

`func (o *ProviderInfo) GetProviderType() string`

GetProviderType returns the ProviderType field if non-nil, zero value otherwise.

### GetProviderTypeOk

`func (o *ProviderInfo) GetProviderTypeOk() (*string, bool)`

GetProviderTypeOk returns a tuple with the ProviderType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderType

`func (o *ProviderInfo) SetProviderType(v string)`

SetProviderType sets ProviderType field to given value.


### GetConfig

`func (o *ProviderInfo) GetConfig() map[string]AppendRowsRequestRowsInnerValue`

GetConfig returns the Config field if non-nil, zero value otherwise.

### GetConfigOk

`func (o *ProviderInfo) GetConfigOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetConfigOk returns a tuple with the Config field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfig

`func (o *ProviderInfo) SetConfig(v map[string]AppendRowsRequestRowsInnerValue)`

SetConfig sets Config field to given value.


### GetHealth

`func (o *ProviderInfo) GetHealth() map[string]AppendRowsRequestRowsInnerValue`

GetHealth returns the Health field if non-nil, zero value otherwise.

### GetHealthOk

`func (o *ProviderInfo) GetHealthOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetHealthOk returns a tuple with the Health field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHealth

`func (o *ProviderInfo) SetHealth(v map[string]AppendRowsRequestRowsInnerValue)`

SetHealth sets Health field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


