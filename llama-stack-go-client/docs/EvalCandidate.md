# EvalCandidate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "model"]
**Model** | **string** | The model ID to evaluate. | 
**SamplingParams** | [**SamplingParams**](SamplingParams.md) | The sampling parameters for the model. | 
**SystemMessage** | Pointer to [**SystemMessage**](SystemMessage.md) | (Optional) The system message providing instructions or context to the model. | [optional] 
**Config** | [**AgentConfig**](AgentConfig.md) | The configuration for the agent candidate. | 

## Methods

### NewEvalCandidate

`func NewEvalCandidate(type_ string, model string, samplingParams SamplingParams, config AgentConfig, ) *EvalCandidate`

NewEvalCandidate instantiates a new EvalCandidate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEvalCandidateWithDefaults

`func NewEvalCandidateWithDefaults() *EvalCandidate`

NewEvalCandidateWithDefaults instantiates a new EvalCandidate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *EvalCandidate) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *EvalCandidate) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *EvalCandidate) SetType(v string)`

SetType sets Type field to given value.


### GetModel

`func (o *EvalCandidate) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *EvalCandidate) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *EvalCandidate) SetModel(v string)`

SetModel sets Model field to given value.


### GetSamplingParams

`func (o *EvalCandidate) GetSamplingParams() SamplingParams`

GetSamplingParams returns the SamplingParams field if non-nil, zero value otherwise.

### GetSamplingParamsOk

`func (o *EvalCandidate) GetSamplingParamsOk() (*SamplingParams, bool)`

GetSamplingParamsOk returns a tuple with the SamplingParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamplingParams

`func (o *EvalCandidate) SetSamplingParams(v SamplingParams)`

SetSamplingParams sets SamplingParams field to given value.


### GetSystemMessage

`func (o *EvalCandidate) GetSystemMessage() SystemMessage`

GetSystemMessage returns the SystemMessage field if non-nil, zero value otherwise.

### GetSystemMessageOk

`func (o *EvalCandidate) GetSystemMessageOk() (*SystemMessage, bool)`

GetSystemMessageOk returns a tuple with the SystemMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemMessage

`func (o *EvalCandidate) SetSystemMessage(v SystemMessage)`

SetSystemMessage sets SystemMessage field to given value.

### HasSystemMessage

`func (o *EvalCandidate) HasSystemMessage() bool`

HasSystemMessage returns a boolean if a field has been set.

### GetConfig

`func (o *EvalCandidate) GetConfig() AgentConfig`

GetConfig returns the Config field if non-nil, zero value otherwise.

### GetConfigOk

`func (o *EvalCandidate) GetConfigOk() (*AgentConfig, bool)`

GetConfigOk returns a tuple with the Config field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfig

`func (o *EvalCandidate) SetConfig(v AgentConfig)`

SetConfig sets Config field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


