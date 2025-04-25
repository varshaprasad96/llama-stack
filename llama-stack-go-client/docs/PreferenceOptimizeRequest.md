# PreferenceOptimizeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobUuid** | **string** |  | 
**FinetunedModel** | **string** |  | 
**AlgorithmConfig** | [**DPOAlignmentConfig**](DPOAlignmentConfig.md) |  | 
**TrainingConfig** | [**TrainingConfig**](TrainingConfig.md) |  | 
**HyperparamSearchConfig** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 
**LoggerConfig** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewPreferenceOptimizeRequest

`func NewPreferenceOptimizeRequest(jobUuid string, finetunedModel string, algorithmConfig DPOAlignmentConfig, trainingConfig TrainingConfig, hyperparamSearchConfig map[string]AppendRowsRequestRowsInnerValue, loggerConfig map[string]AppendRowsRequestRowsInnerValue, ) *PreferenceOptimizeRequest`

NewPreferenceOptimizeRequest instantiates a new PreferenceOptimizeRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPreferenceOptimizeRequestWithDefaults

`func NewPreferenceOptimizeRequestWithDefaults() *PreferenceOptimizeRequest`

NewPreferenceOptimizeRequestWithDefaults instantiates a new PreferenceOptimizeRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetJobUuid

`func (o *PreferenceOptimizeRequest) GetJobUuid() string`

GetJobUuid returns the JobUuid field if non-nil, zero value otherwise.

### GetJobUuidOk

`func (o *PreferenceOptimizeRequest) GetJobUuidOk() (*string, bool)`

GetJobUuidOk returns a tuple with the JobUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobUuid

`func (o *PreferenceOptimizeRequest) SetJobUuid(v string)`

SetJobUuid sets JobUuid field to given value.


### GetFinetunedModel

`func (o *PreferenceOptimizeRequest) GetFinetunedModel() string`

GetFinetunedModel returns the FinetunedModel field if non-nil, zero value otherwise.

### GetFinetunedModelOk

`func (o *PreferenceOptimizeRequest) GetFinetunedModelOk() (*string, bool)`

GetFinetunedModelOk returns a tuple with the FinetunedModel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinetunedModel

`func (o *PreferenceOptimizeRequest) SetFinetunedModel(v string)`

SetFinetunedModel sets FinetunedModel field to given value.


### GetAlgorithmConfig

`func (o *PreferenceOptimizeRequest) GetAlgorithmConfig() DPOAlignmentConfig`

GetAlgorithmConfig returns the AlgorithmConfig field if non-nil, zero value otherwise.

### GetAlgorithmConfigOk

`func (o *PreferenceOptimizeRequest) GetAlgorithmConfigOk() (*DPOAlignmentConfig, bool)`

GetAlgorithmConfigOk returns a tuple with the AlgorithmConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlgorithmConfig

`func (o *PreferenceOptimizeRequest) SetAlgorithmConfig(v DPOAlignmentConfig)`

SetAlgorithmConfig sets AlgorithmConfig field to given value.


### GetTrainingConfig

`func (o *PreferenceOptimizeRequest) GetTrainingConfig() TrainingConfig`

GetTrainingConfig returns the TrainingConfig field if non-nil, zero value otherwise.

### GetTrainingConfigOk

`func (o *PreferenceOptimizeRequest) GetTrainingConfigOk() (*TrainingConfig, bool)`

GetTrainingConfigOk returns a tuple with the TrainingConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrainingConfig

`func (o *PreferenceOptimizeRequest) SetTrainingConfig(v TrainingConfig)`

SetTrainingConfig sets TrainingConfig field to given value.


### GetHyperparamSearchConfig

`func (o *PreferenceOptimizeRequest) GetHyperparamSearchConfig() map[string]AppendRowsRequestRowsInnerValue`

GetHyperparamSearchConfig returns the HyperparamSearchConfig field if non-nil, zero value otherwise.

### GetHyperparamSearchConfigOk

`func (o *PreferenceOptimizeRequest) GetHyperparamSearchConfigOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetHyperparamSearchConfigOk returns a tuple with the HyperparamSearchConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHyperparamSearchConfig

`func (o *PreferenceOptimizeRequest) SetHyperparamSearchConfig(v map[string]AppendRowsRequestRowsInnerValue)`

SetHyperparamSearchConfig sets HyperparamSearchConfig field to given value.


### GetLoggerConfig

`func (o *PreferenceOptimizeRequest) GetLoggerConfig() map[string]AppendRowsRequestRowsInnerValue`

GetLoggerConfig returns the LoggerConfig field if non-nil, zero value otherwise.

### GetLoggerConfigOk

`func (o *PreferenceOptimizeRequest) GetLoggerConfigOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetLoggerConfigOk returns a tuple with the LoggerConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoggerConfig

`func (o *PreferenceOptimizeRequest) SetLoggerConfig(v map[string]AppendRowsRequestRowsInnerValue)`

SetLoggerConfig sets LoggerConfig field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


