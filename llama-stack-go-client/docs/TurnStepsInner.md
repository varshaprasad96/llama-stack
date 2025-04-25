# TurnStepsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TurnId** | **string** | The ID of the turn. | 
**StepId** | **string** | The ID of the step. | 
**StartedAt** | Pointer to **time.Time** | The time the step started. | [optional] 
**CompletedAt** | Pointer to **time.Time** | The time the step completed. | [optional] 
**StepType** | **string** |  | [default to "memory_retrieval"]
**ModelResponse** | [**CompletionMessage**](CompletionMessage.md) | The response from the LLM. | 
**ToolCalls** | [**[]ToolCall**](ToolCall.md) | The tool calls to execute. | 
**ToolResponses** | [**[]ToolResponse**](ToolResponse.md) | The tool responses from the tool calls. | 
**Violation** | Pointer to [**SafetyViolation**](SafetyViolation.md) | The violation from the shield call. | [optional] 
**VectorDbIds** | **string** | The IDs of the vector databases to retrieve context from. | 
**InsertedContext** | [**InterleavedContent**](InterleavedContent.md) | The context retrieved from the vector databases. | 

## Methods

### NewTurnStepsInner

`func NewTurnStepsInner(turnId string, stepId string, stepType string, modelResponse CompletionMessage, toolCalls []ToolCall, toolResponses []ToolResponse, vectorDbIds string, insertedContext InterleavedContent, ) *TurnStepsInner`

NewTurnStepsInner instantiates a new TurnStepsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTurnStepsInnerWithDefaults

`func NewTurnStepsInnerWithDefaults() *TurnStepsInner`

NewTurnStepsInnerWithDefaults instantiates a new TurnStepsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTurnId

`func (o *TurnStepsInner) GetTurnId() string`

GetTurnId returns the TurnId field if non-nil, zero value otherwise.

### GetTurnIdOk

`func (o *TurnStepsInner) GetTurnIdOk() (*string, bool)`

GetTurnIdOk returns a tuple with the TurnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurnId

`func (o *TurnStepsInner) SetTurnId(v string)`

SetTurnId sets TurnId field to given value.


### GetStepId

`func (o *TurnStepsInner) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *TurnStepsInner) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *TurnStepsInner) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetStartedAt

`func (o *TurnStepsInner) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *TurnStepsInner) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *TurnStepsInner) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *TurnStepsInner) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### GetCompletedAt

`func (o *TurnStepsInner) GetCompletedAt() time.Time`

GetCompletedAt returns the CompletedAt field if non-nil, zero value otherwise.

### GetCompletedAtOk

`func (o *TurnStepsInner) GetCompletedAtOk() (*time.Time, bool)`

GetCompletedAtOk returns a tuple with the CompletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletedAt

`func (o *TurnStepsInner) SetCompletedAt(v time.Time)`

SetCompletedAt sets CompletedAt field to given value.

### HasCompletedAt

`func (o *TurnStepsInner) HasCompletedAt() bool`

HasCompletedAt returns a boolean if a field has been set.

### GetStepType

`func (o *TurnStepsInner) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *TurnStepsInner) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *TurnStepsInner) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetModelResponse

`func (o *TurnStepsInner) GetModelResponse() CompletionMessage`

GetModelResponse returns the ModelResponse field if non-nil, zero value otherwise.

### GetModelResponseOk

`func (o *TurnStepsInner) GetModelResponseOk() (*CompletionMessage, bool)`

GetModelResponseOk returns a tuple with the ModelResponse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelResponse

`func (o *TurnStepsInner) SetModelResponse(v CompletionMessage)`

SetModelResponse sets ModelResponse field to given value.


### GetToolCalls

`func (o *TurnStepsInner) GetToolCalls() []ToolCall`

GetToolCalls returns the ToolCalls field if non-nil, zero value otherwise.

### GetToolCallsOk

`func (o *TurnStepsInner) GetToolCallsOk() (*[]ToolCall, bool)`

GetToolCallsOk returns a tuple with the ToolCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCalls

`func (o *TurnStepsInner) SetToolCalls(v []ToolCall)`

SetToolCalls sets ToolCalls field to given value.


### GetToolResponses

`func (o *TurnStepsInner) GetToolResponses() []ToolResponse`

GetToolResponses returns the ToolResponses field if non-nil, zero value otherwise.

### GetToolResponsesOk

`func (o *TurnStepsInner) GetToolResponsesOk() (*[]ToolResponse, bool)`

GetToolResponsesOk returns a tuple with the ToolResponses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolResponses

`func (o *TurnStepsInner) SetToolResponses(v []ToolResponse)`

SetToolResponses sets ToolResponses field to given value.


### GetViolation

`func (o *TurnStepsInner) GetViolation() SafetyViolation`

GetViolation returns the Violation field if non-nil, zero value otherwise.

### GetViolationOk

`func (o *TurnStepsInner) GetViolationOk() (*SafetyViolation, bool)`

GetViolationOk returns a tuple with the Violation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViolation

`func (o *TurnStepsInner) SetViolation(v SafetyViolation)`

SetViolation sets Violation field to given value.

### HasViolation

`func (o *TurnStepsInner) HasViolation() bool`

HasViolation returns a boolean if a field has been set.

### GetVectorDbIds

`func (o *TurnStepsInner) GetVectorDbIds() string`

GetVectorDbIds returns the VectorDbIds field if non-nil, zero value otherwise.

### GetVectorDbIdsOk

`func (o *TurnStepsInner) GetVectorDbIdsOk() (*string, bool)`

GetVectorDbIdsOk returns a tuple with the VectorDbIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVectorDbIds

`func (o *TurnStepsInner) SetVectorDbIds(v string)`

SetVectorDbIds sets VectorDbIds field to given value.


### GetInsertedContext

`func (o *TurnStepsInner) GetInsertedContext() InterleavedContent`

GetInsertedContext returns the InsertedContext field if non-nil, zero value otherwise.

### GetInsertedContextOk

`func (o *TurnStepsInner) GetInsertedContextOk() (*InterleavedContent, bool)`

GetInsertedContextOk returns a tuple with the InsertedContext field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInsertedContext

`func (o *TurnStepsInner) SetInsertedContext(v InterleavedContent)`

SetInsertedContext sets InsertedContext field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


