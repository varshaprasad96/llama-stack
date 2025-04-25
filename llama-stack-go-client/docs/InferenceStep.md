# InferenceStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TurnId** | **string** | The ID of the turn. | 
**StepId** | **string** | The ID of the step. | 
**StartedAt** | Pointer to **time.Time** | The time the step started. | [optional] 
**CompletedAt** | Pointer to **time.Time** | The time the step completed. | [optional] 
**StepType** | **string** |  | [default to "inference"]
**ModelResponse** | [**CompletionMessage**](CompletionMessage.md) | The response from the LLM. | 

## Methods

### NewInferenceStep

`func NewInferenceStep(turnId string, stepId string, stepType string, modelResponse CompletionMessage, ) *InferenceStep`

NewInferenceStep instantiates a new InferenceStep object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInferenceStepWithDefaults

`func NewInferenceStepWithDefaults() *InferenceStep`

NewInferenceStepWithDefaults instantiates a new InferenceStep object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTurnId

`func (o *InferenceStep) GetTurnId() string`

GetTurnId returns the TurnId field if non-nil, zero value otherwise.

### GetTurnIdOk

`func (o *InferenceStep) GetTurnIdOk() (*string, bool)`

GetTurnIdOk returns a tuple with the TurnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurnId

`func (o *InferenceStep) SetTurnId(v string)`

SetTurnId sets TurnId field to given value.


### GetStepId

`func (o *InferenceStep) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *InferenceStep) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *InferenceStep) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetStartedAt

`func (o *InferenceStep) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *InferenceStep) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *InferenceStep) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *InferenceStep) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### GetCompletedAt

`func (o *InferenceStep) GetCompletedAt() time.Time`

GetCompletedAt returns the CompletedAt field if non-nil, zero value otherwise.

### GetCompletedAtOk

`func (o *InferenceStep) GetCompletedAtOk() (*time.Time, bool)`

GetCompletedAtOk returns a tuple with the CompletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletedAt

`func (o *InferenceStep) SetCompletedAt(v time.Time)`

SetCompletedAt sets CompletedAt field to given value.

### HasCompletedAt

`func (o *InferenceStep) HasCompletedAt() bool`

HasCompletedAt returns a boolean if a field has been set.

### GetStepType

`func (o *InferenceStep) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *InferenceStep) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *InferenceStep) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetModelResponse

`func (o *InferenceStep) GetModelResponse() CompletionMessage`

GetModelResponse returns the ModelResponse field if non-nil, zero value otherwise.

### GetModelResponseOk

`func (o *InferenceStep) GetModelResponseOk() (*CompletionMessage, bool)`

GetModelResponseOk returns a tuple with the ModelResponse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelResponse

`func (o *InferenceStep) SetModelResponse(v CompletionMessage)`

SetModelResponse sets ModelResponse field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


