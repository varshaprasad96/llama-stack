# ToolExecutionStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TurnId** | **string** | The ID of the turn. | 
**StepId** | **string** | The ID of the step. | 
**StartedAt** | Pointer to **time.Time** | The time the step started. | [optional] 
**CompletedAt** | Pointer to **time.Time** | The time the step completed. | [optional] 
**StepType** | **string** |  | [default to "tool_execution"]
**ToolCalls** | [**[]ToolCall**](ToolCall.md) | The tool calls to execute. | 
**ToolResponses** | [**[]ToolResponse**](ToolResponse.md) | The tool responses from the tool calls. | 

## Methods

### NewToolExecutionStep

`func NewToolExecutionStep(turnId string, stepId string, stepType string, toolCalls []ToolCall, toolResponses []ToolResponse, ) *ToolExecutionStep`

NewToolExecutionStep instantiates a new ToolExecutionStep object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolExecutionStepWithDefaults

`func NewToolExecutionStepWithDefaults() *ToolExecutionStep`

NewToolExecutionStepWithDefaults instantiates a new ToolExecutionStep object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTurnId

`func (o *ToolExecutionStep) GetTurnId() string`

GetTurnId returns the TurnId field if non-nil, zero value otherwise.

### GetTurnIdOk

`func (o *ToolExecutionStep) GetTurnIdOk() (*string, bool)`

GetTurnIdOk returns a tuple with the TurnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurnId

`func (o *ToolExecutionStep) SetTurnId(v string)`

SetTurnId sets TurnId field to given value.


### GetStepId

`func (o *ToolExecutionStep) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *ToolExecutionStep) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *ToolExecutionStep) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetStartedAt

`func (o *ToolExecutionStep) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *ToolExecutionStep) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *ToolExecutionStep) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *ToolExecutionStep) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### GetCompletedAt

`func (o *ToolExecutionStep) GetCompletedAt() time.Time`

GetCompletedAt returns the CompletedAt field if non-nil, zero value otherwise.

### GetCompletedAtOk

`func (o *ToolExecutionStep) GetCompletedAtOk() (*time.Time, bool)`

GetCompletedAtOk returns a tuple with the CompletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletedAt

`func (o *ToolExecutionStep) SetCompletedAt(v time.Time)`

SetCompletedAt sets CompletedAt field to given value.

### HasCompletedAt

`func (o *ToolExecutionStep) HasCompletedAt() bool`

HasCompletedAt returns a boolean if a field has been set.

### GetStepType

`func (o *ToolExecutionStep) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *ToolExecutionStep) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *ToolExecutionStep) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetToolCalls

`func (o *ToolExecutionStep) GetToolCalls() []ToolCall`

GetToolCalls returns the ToolCalls field if non-nil, zero value otherwise.

### GetToolCallsOk

`func (o *ToolExecutionStep) GetToolCallsOk() (*[]ToolCall, bool)`

GetToolCallsOk returns a tuple with the ToolCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCalls

`func (o *ToolExecutionStep) SetToolCalls(v []ToolCall)`

SetToolCalls sets ToolCalls field to given value.


### GetToolResponses

`func (o *ToolExecutionStep) GetToolResponses() []ToolResponse`

GetToolResponses returns the ToolResponses field if non-nil, zero value otherwise.

### GetToolResponsesOk

`func (o *ToolExecutionStep) GetToolResponsesOk() (*[]ToolResponse, bool)`

GetToolResponsesOk returns a tuple with the ToolResponses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolResponses

`func (o *ToolExecutionStep) SetToolResponses(v []ToolResponse)`

SetToolResponses sets ToolResponses field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


