# TopPSamplingStrategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "top_p"]
**Temperature** | Pointer to **float32** |  | [optional] 
**TopP** | Pointer to **float32** |  | [optional] [default to 0.95]

## Methods

### NewTopPSamplingStrategy

`func NewTopPSamplingStrategy(type_ string, ) *TopPSamplingStrategy`

NewTopPSamplingStrategy instantiates a new TopPSamplingStrategy object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTopPSamplingStrategyWithDefaults

`func NewTopPSamplingStrategyWithDefaults() *TopPSamplingStrategy`

NewTopPSamplingStrategyWithDefaults instantiates a new TopPSamplingStrategy object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *TopPSamplingStrategy) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *TopPSamplingStrategy) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *TopPSamplingStrategy) SetType(v string)`

SetType sets Type field to given value.


### GetTemperature

`func (o *TopPSamplingStrategy) GetTemperature() float32`

GetTemperature returns the Temperature field if non-nil, zero value otherwise.

### GetTemperatureOk

`func (o *TopPSamplingStrategy) GetTemperatureOk() (*float32, bool)`

GetTemperatureOk returns a tuple with the Temperature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTemperature

`func (o *TopPSamplingStrategy) SetTemperature(v float32)`

SetTemperature sets Temperature field to given value.

### HasTemperature

`func (o *TopPSamplingStrategy) HasTemperature() bool`

HasTemperature returns a boolean if a field has been set.

### GetTopP

`func (o *TopPSamplingStrategy) GetTopP() float32`

GetTopP returns the TopP field if non-nil, zero value otherwise.

### GetTopPOk

`func (o *TopPSamplingStrategy) GetTopPOk() (*float32, bool)`

GetTopPOk returns a tuple with the TopP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopP

`func (o *TopPSamplingStrategy) SetTopP(v float32)`

SetTopP sets TopP field to given value.

### HasTopP

`func (o *TopPSamplingStrategy) HasTopP() bool`

HasTopP returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


