# SupervisedFineTuneRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobUuid** | **string** |  | 
**TrainingConfig** | [**TrainingConfig**](TrainingConfig.md) |  | 
**HyperparamSearchConfig** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 
**LoggerConfig** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 
**Model** | Pointer to **string** |  | [optional] 
**CheckpointDir** | Pointer to **string** |  | [optional] 
**AlgorithmConfig** | Pointer to [**AlgorithmConfig**](AlgorithmConfig.md) |  | [optional] 

## Methods

### NewSupervisedFineTuneRequest

`func NewSupervisedFineTuneRequest(jobUuid string, trainingConfig TrainingConfig, hyperparamSearchConfig map[string]AppendRowsRequestRowsInnerValue, loggerConfig map[string]AppendRowsRequestRowsInnerValue, ) *SupervisedFineTuneRequest`

NewSupervisedFineTuneRequest instantiates a new SupervisedFineTuneRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSupervisedFineTuneRequestWithDefaults

`func NewSupervisedFineTuneRequestWithDefaults() *SupervisedFineTuneRequest`

NewSupervisedFineTuneRequestWithDefaults instantiates a new SupervisedFineTuneRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetJobUuid

`func (o *SupervisedFineTuneRequest) GetJobUuid() string`

GetJobUuid returns the JobUuid field if non-nil, zero value otherwise.

### GetJobUuidOk

`func (o *SupervisedFineTuneRequest) GetJobUuidOk() (*string, bool)`

GetJobUuidOk returns a tuple with the JobUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobUuid

`func (o *SupervisedFineTuneRequest) SetJobUuid(v string)`

SetJobUuid sets JobUuid field to given value.


### GetTrainingConfig

`func (o *SupervisedFineTuneRequest) GetTrainingConfig() TrainingConfig`

GetTrainingConfig returns the TrainingConfig field if non-nil, zero value otherwise.

### GetTrainingConfigOk

`func (o *SupervisedFineTuneRequest) GetTrainingConfigOk() (*TrainingConfig, bool)`

GetTrainingConfigOk returns a tuple with the TrainingConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrainingConfig

`func (o *SupervisedFineTuneRequest) SetTrainingConfig(v TrainingConfig)`

SetTrainingConfig sets TrainingConfig field to given value.


### GetHyperparamSearchConfig

`func (o *SupervisedFineTuneRequest) GetHyperparamSearchConfig() map[string]AppendRowsRequestRowsInnerValue`

GetHyperparamSearchConfig returns the HyperparamSearchConfig field if non-nil, zero value otherwise.

### GetHyperparamSearchConfigOk

`func (o *SupervisedFineTuneRequest) GetHyperparamSearchConfigOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetHyperparamSearchConfigOk returns a tuple with the HyperparamSearchConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHyperparamSearchConfig

`func (o *SupervisedFineTuneRequest) SetHyperparamSearchConfig(v map[string]AppendRowsRequestRowsInnerValue)`

SetHyperparamSearchConfig sets HyperparamSearchConfig field to given value.


### GetLoggerConfig

`func (o *SupervisedFineTuneRequest) GetLoggerConfig() map[string]AppendRowsRequestRowsInnerValue`

GetLoggerConfig returns the LoggerConfig field if non-nil, zero value otherwise.

### GetLoggerConfigOk

`func (o *SupervisedFineTuneRequest) GetLoggerConfigOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetLoggerConfigOk returns a tuple with the LoggerConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoggerConfig

`func (o *SupervisedFineTuneRequest) SetLoggerConfig(v map[string]AppendRowsRequestRowsInnerValue)`

SetLoggerConfig sets LoggerConfig field to given value.


### GetModel

`func (o *SupervisedFineTuneRequest) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *SupervisedFineTuneRequest) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *SupervisedFineTuneRequest) SetModel(v string)`

SetModel sets Model field to given value.

### HasModel

`func (o *SupervisedFineTuneRequest) HasModel() bool`

HasModel returns a boolean if a field has been set.

### GetCheckpointDir

`func (o *SupervisedFineTuneRequest) GetCheckpointDir() string`

GetCheckpointDir returns the CheckpointDir field if non-nil, zero value otherwise.

### GetCheckpointDirOk

`func (o *SupervisedFineTuneRequest) GetCheckpointDirOk() (*string, bool)`

GetCheckpointDirOk returns a tuple with the CheckpointDir field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckpointDir

`func (o *SupervisedFineTuneRequest) SetCheckpointDir(v string)`

SetCheckpointDir sets CheckpointDir field to given value.

### HasCheckpointDir

`func (o *SupervisedFineTuneRequest) HasCheckpointDir() bool`

HasCheckpointDir returns a boolean if a field has been set.

### GetAlgorithmConfig

`func (o *SupervisedFineTuneRequest) GetAlgorithmConfig() AlgorithmConfig`

GetAlgorithmConfig returns the AlgorithmConfig field if non-nil, zero value otherwise.

### GetAlgorithmConfigOk

`func (o *SupervisedFineTuneRequest) GetAlgorithmConfigOk() (*AlgorithmConfig, bool)`

GetAlgorithmConfigOk returns a tuple with the AlgorithmConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlgorithmConfig

`func (o *SupervisedFineTuneRequest) SetAlgorithmConfig(v AlgorithmConfig)`

SetAlgorithmConfig sets AlgorithmConfig field to given value.

### HasAlgorithmConfig

`func (o *SupervisedFineTuneRequest) HasAlgorithmConfig() bool`

HasAlgorithmConfig returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


