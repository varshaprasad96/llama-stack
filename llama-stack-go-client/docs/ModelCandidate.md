# ModelCandidate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "model"]
**Model** | **string** | The model ID to evaluate. | 
**SamplingParams** | [**SamplingParams**](SamplingParams.md) | The sampling parameters for the model. | 
**SystemMessage** | Pointer to [**SystemMessage**](SystemMessage.md) | (Optional) The system message providing instructions or context to the model. | [optional] 

## Methods

### NewModelCandidate

`func NewModelCandidate(type_ string, model string, samplingParams SamplingParams, ) *ModelCandidate`

NewModelCandidate instantiates a new ModelCandidate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewModelCandidateWithDefaults

`func NewModelCandidateWithDefaults() *ModelCandidate`

NewModelCandidateWithDefaults instantiates a new ModelCandidate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *ModelCandidate) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ModelCandidate) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ModelCandidate) SetType(v string)`

SetType sets Type field to given value.


### GetModel

`func (o *ModelCandidate) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *ModelCandidate) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *ModelCandidate) SetModel(v string)`

SetModel sets Model field to given value.


### GetSamplingParams

`func (o *ModelCandidate) GetSamplingParams() SamplingParams`

GetSamplingParams returns the SamplingParams field if non-nil, zero value otherwise.

### GetSamplingParamsOk

`func (o *ModelCandidate) GetSamplingParamsOk() (*SamplingParams, bool)`

GetSamplingParamsOk returns a tuple with the SamplingParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamplingParams

`func (o *ModelCandidate) SetSamplingParams(v SamplingParams)`

SetSamplingParams sets SamplingParams field to given value.


### GetSystemMessage

`func (o *ModelCandidate) GetSystemMessage() SystemMessage`

GetSystemMessage returns the SystemMessage field if non-nil, zero value otherwise.

### GetSystemMessageOk

`func (o *ModelCandidate) GetSystemMessageOk() (*SystemMessage, bool)`

GetSystemMessageOk returns a tuple with the SystemMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemMessage

`func (o *ModelCandidate) SetSystemMessage(v SystemMessage)`

SetSystemMessage sets SystemMessage field to given value.

### HasSystemMessage

`func (o *ModelCandidate) HasSystemMessage() bool`

HasSystemMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


