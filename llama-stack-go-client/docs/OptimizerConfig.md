# OptimizerConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OptimizerType** | [**OptimizerType**](OptimizerType.md) |  | 
**Lr** | **float32** |  | 
**WeightDecay** | **float32** |  | 
**NumWarmupSteps** | **int32** |  | 

## Methods

### NewOptimizerConfig

`func NewOptimizerConfig(optimizerType OptimizerType, lr float32, weightDecay float32, numWarmupSteps int32, ) *OptimizerConfig`

NewOptimizerConfig instantiates a new OptimizerConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOptimizerConfigWithDefaults

`func NewOptimizerConfigWithDefaults() *OptimizerConfig`

NewOptimizerConfigWithDefaults instantiates a new OptimizerConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOptimizerType

`func (o *OptimizerConfig) GetOptimizerType() OptimizerType`

GetOptimizerType returns the OptimizerType field if non-nil, zero value otherwise.

### GetOptimizerTypeOk

`func (o *OptimizerConfig) GetOptimizerTypeOk() (*OptimizerType, bool)`

GetOptimizerTypeOk returns a tuple with the OptimizerType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOptimizerType

`func (o *OptimizerConfig) SetOptimizerType(v OptimizerType)`

SetOptimizerType sets OptimizerType field to given value.


### GetLr

`func (o *OptimizerConfig) GetLr() float32`

GetLr returns the Lr field if non-nil, zero value otherwise.

### GetLrOk

`func (o *OptimizerConfig) GetLrOk() (*float32, bool)`

GetLrOk returns a tuple with the Lr field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLr

`func (o *OptimizerConfig) SetLr(v float32)`

SetLr sets Lr field to given value.


### GetWeightDecay

`func (o *OptimizerConfig) GetWeightDecay() float32`

GetWeightDecay returns the WeightDecay field if non-nil, zero value otherwise.

### GetWeightDecayOk

`func (o *OptimizerConfig) GetWeightDecayOk() (*float32, bool)`

GetWeightDecayOk returns a tuple with the WeightDecay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeightDecay

`func (o *OptimizerConfig) SetWeightDecay(v float32)`

SetWeightDecay sets WeightDecay field to given value.


### GetNumWarmupSteps

`func (o *OptimizerConfig) GetNumWarmupSteps() int32`

GetNumWarmupSteps returns the NumWarmupSteps field if non-nil, zero value otherwise.

### GetNumWarmupStepsOk

`func (o *OptimizerConfig) GetNumWarmupStepsOk() (*int32, bool)`

GetNumWarmupStepsOk returns a tuple with the NumWarmupSteps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumWarmupSteps

`func (o *OptimizerConfig) SetNumWarmupSteps(v int32)`

SetNumWarmupSteps sets NumWarmupSteps field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


