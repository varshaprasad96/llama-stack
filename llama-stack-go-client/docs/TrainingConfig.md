# TrainingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**NEpochs** | **int32** |  | 
**MaxStepsPerEpoch** | **int32** |  | [default to 1]
**GradientAccumulationSteps** | **int32** |  | [default to 1]
**MaxValidationSteps** | Pointer to **int32** |  | [optional] [default to 1]
**DataConfig** | Pointer to [**DataConfig**](DataConfig.md) |  | [optional] 
**OptimizerConfig** | Pointer to [**OptimizerConfig**](OptimizerConfig.md) |  | [optional] 
**EfficiencyConfig** | Pointer to [**EfficiencyConfig**](EfficiencyConfig.md) |  | [optional] 
**Dtype** | Pointer to **string** |  | [optional] [default to "bf16"]

## Methods

### NewTrainingConfig

`func NewTrainingConfig(nEpochs int32, maxStepsPerEpoch int32, gradientAccumulationSteps int32, ) *TrainingConfig`

NewTrainingConfig instantiates a new TrainingConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTrainingConfigWithDefaults

`func NewTrainingConfigWithDefaults() *TrainingConfig`

NewTrainingConfigWithDefaults instantiates a new TrainingConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetNEpochs

`func (o *TrainingConfig) GetNEpochs() int32`

GetNEpochs returns the NEpochs field if non-nil, zero value otherwise.

### GetNEpochsOk

`func (o *TrainingConfig) GetNEpochsOk() (*int32, bool)`

GetNEpochsOk returns a tuple with the NEpochs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNEpochs

`func (o *TrainingConfig) SetNEpochs(v int32)`

SetNEpochs sets NEpochs field to given value.


### GetMaxStepsPerEpoch

`func (o *TrainingConfig) GetMaxStepsPerEpoch() int32`

GetMaxStepsPerEpoch returns the MaxStepsPerEpoch field if non-nil, zero value otherwise.

### GetMaxStepsPerEpochOk

`func (o *TrainingConfig) GetMaxStepsPerEpochOk() (*int32, bool)`

GetMaxStepsPerEpochOk returns a tuple with the MaxStepsPerEpoch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxStepsPerEpoch

`func (o *TrainingConfig) SetMaxStepsPerEpoch(v int32)`

SetMaxStepsPerEpoch sets MaxStepsPerEpoch field to given value.


### GetGradientAccumulationSteps

`func (o *TrainingConfig) GetGradientAccumulationSteps() int32`

GetGradientAccumulationSteps returns the GradientAccumulationSteps field if non-nil, zero value otherwise.

### GetGradientAccumulationStepsOk

`func (o *TrainingConfig) GetGradientAccumulationStepsOk() (*int32, bool)`

GetGradientAccumulationStepsOk returns a tuple with the GradientAccumulationSteps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGradientAccumulationSteps

`func (o *TrainingConfig) SetGradientAccumulationSteps(v int32)`

SetGradientAccumulationSteps sets GradientAccumulationSteps field to given value.


### GetMaxValidationSteps

`func (o *TrainingConfig) GetMaxValidationSteps() int32`

GetMaxValidationSteps returns the MaxValidationSteps field if non-nil, zero value otherwise.

### GetMaxValidationStepsOk

`func (o *TrainingConfig) GetMaxValidationStepsOk() (*int32, bool)`

GetMaxValidationStepsOk returns a tuple with the MaxValidationSteps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxValidationSteps

`func (o *TrainingConfig) SetMaxValidationSteps(v int32)`

SetMaxValidationSteps sets MaxValidationSteps field to given value.

### HasMaxValidationSteps

`func (o *TrainingConfig) HasMaxValidationSteps() bool`

HasMaxValidationSteps returns a boolean if a field has been set.

### GetDataConfig

`func (o *TrainingConfig) GetDataConfig() DataConfig`

GetDataConfig returns the DataConfig field if non-nil, zero value otherwise.

### GetDataConfigOk

`func (o *TrainingConfig) GetDataConfigOk() (*DataConfig, bool)`

GetDataConfigOk returns a tuple with the DataConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataConfig

`func (o *TrainingConfig) SetDataConfig(v DataConfig)`

SetDataConfig sets DataConfig field to given value.

### HasDataConfig

`func (o *TrainingConfig) HasDataConfig() bool`

HasDataConfig returns a boolean if a field has been set.

### GetOptimizerConfig

`func (o *TrainingConfig) GetOptimizerConfig() OptimizerConfig`

GetOptimizerConfig returns the OptimizerConfig field if non-nil, zero value otherwise.

### GetOptimizerConfigOk

`func (o *TrainingConfig) GetOptimizerConfigOk() (*OptimizerConfig, bool)`

GetOptimizerConfigOk returns a tuple with the OptimizerConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOptimizerConfig

`func (o *TrainingConfig) SetOptimizerConfig(v OptimizerConfig)`

SetOptimizerConfig sets OptimizerConfig field to given value.

### HasOptimizerConfig

`func (o *TrainingConfig) HasOptimizerConfig() bool`

HasOptimizerConfig returns a boolean if a field has been set.

### GetEfficiencyConfig

`func (o *TrainingConfig) GetEfficiencyConfig() EfficiencyConfig`

GetEfficiencyConfig returns the EfficiencyConfig field if non-nil, zero value otherwise.

### GetEfficiencyConfigOk

`func (o *TrainingConfig) GetEfficiencyConfigOk() (*EfficiencyConfig, bool)`

GetEfficiencyConfigOk returns a tuple with the EfficiencyConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEfficiencyConfig

`func (o *TrainingConfig) SetEfficiencyConfig(v EfficiencyConfig)`

SetEfficiencyConfig sets EfficiencyConfig field to given value.

### HasEfficiencyConfig

`func (o *TrainingConfig) HasEfficiencyConfig() bool`

HasEfficiencyConfig returns a boolean if a field has been set.

### GetDtype

`func (o *TrainingConfig) GetDtype() string`

GetDtype returns the Dtype field if non-nil, zero value otherwise.

### GetDtypeOk

`func (o *TrainingConfig) GetDtypeOk() (*string, bool)`

GetDtypeOk returns a tuple with the Dtype field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDtype

`func (o *TrainingConfig) SetDtype(v string)`

SetDtype sets Dtype field to given value.

### HasDtype

`func (o *TrainingConfig) HasDtype() bool`

HasDtype returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


