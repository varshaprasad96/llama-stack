# EfficiencyConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EnableActivationCheckpointing** | Pointer to **bool** |  | [optional] [default to false]
**EnableActivationOffloading** | Pointer to **bool** |  | [optional] [default to false]
**MemoryEfficientFsdpWrap** | Pointer to **bool** |  | [optional] [default to false]
**FsdpCpuOffload** | Pointer to **bool** |  | [optional] [default to false]

## Methods

### NewEfficiencyConfig

`func NewEfficiencyConfig() *EfficiencyConfig`

NewEfficiencyConfig instantiates a new EfficiencyConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEfficiencyConfigWithDefaults

`func NewEfficiencyConfigWithDefaults() *EfficiencyConfig`

NewEfficiencyConfigWithDefaults instantiates a new EfficiencyConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnableActivationCheckpointing

`func (o *EfficiencyConfig) GetEnableActivationCheckpointing() bool`

GetEnableActivationCheckpointing returns the EnableActivationCheckpointing field if non-nil, zero value otherwise.

### GetEnableActivationCheckpointingOk

`func (o *EfficiencyConfig) GetEnableActivationCheckpointingOk() (*bool, bool)`

GetEnableActivationCheckpointingOk returns a tuple with the EnableActivationCheckpointing field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableActivationCheckpointing

`func (o *EfficiencyConfig) SetEnableActivationCheckpointing(v bool)`

SetEnableActivationCheckpointing sets EnableActivationCheckpointing field to given value.

### HasEnableActivationCheckpointing

`func (o *EfficiencyConfig) HasEnableActivationCheckpointing() bool`

HasEnableActivationCheckpointing returns a boolean if a field has been set.

### GetEnableActivationOffloading

`func (o *EfficiencyConfig) GetEnableActivationOffloading() bool`

GetEnableActivationOffloading returns the EnableActivationOffloading field if non-nil, zero value otherwise.

### GetEnableActivationOffloadingOk

`func (o *EfficiencyConfig) GetEnableActivationOffloadingOk() (*bool, bool)`

GetEnableActivationOffloadingOk returns a tuple with the EnableActivationOffloading field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableActivationOffloading

`func (o *EfficiencyConfig) SetEnableActivationOffloading(v bool)`

SetEnableActivationOffloading sets EnableActivationOffloading field to given value.

### HasEnableActivationOffloading

`func (o *EfficiencyConfig) HasEnableActivationOffloading() bool`

HasEnableActivationOffloading returns a boolean if a field has been set.

### GetMemoryEfficientFsdpWrap

`func (o *EfficiencyConfig) GetMemoryEfficientFsdpWrap() bool`

GetMemoryEfficientFsdpWrap returns the MemoryEfficientFsdpWrap field if non-nil, zero value otherwise.

### GetMemoryEfficientFsdpWrapOk

`func (o *EfficiencyConfig) GetMemoryEfficientFsdpWrapOk() (*bool, bool)`

GetMemoryEfficientFsdpWrapOk returns a tuple with the MemoryEfficientFsdpWrap field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemoryEfficientFsdpWrap

`func (o *EfficiencyConfig) SetMemoryEfficientFsdpWrap(v bool)`

SetMemoryEfficientFsdpWrap sets MemoryEfficientFsdpWrap field to given value.

### HasMemoryEfficientFsdpWrap

`func (o *EfficiencyConfig) HasMemoryEfficientFsdpWrap() bool`

HasMemoryEfficientFsdpWrap returns a boolean if a field has been set.

### GetFsdpCpuOffload

`func (o *EfficiencyConfig) GetFsdpCpuOffload() bool`

GetFsdpCpuOffload returns the FsdpCpuOffload field if non-nil, zero value otherwise.

### GetFsdpCpuOffloadOk

`func (o *EfficiencyConfig) GetFsdpCpuOffloadOk() (*bool, bool)`

GetFsdpCpuOffloadOk returns a tuple with the FsdpCpuOffload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFsdpCpuOffload

`func (o *EfficiencyConfig) SetFsdpCpuOffload(v bool)`

SetFsdpCpuOffload sets FsdpCpuOffload field to given value.

### HasFsdpCpuOffload

`func (o *EfficiencyConfig) HasFsdpCpuOffload() bool`

HasFsdpCpuOffload returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


