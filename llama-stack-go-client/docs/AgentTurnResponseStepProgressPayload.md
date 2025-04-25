# AgentTurnResponseStepProgressPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventType** | **string** |  | [default to "step_progress"]
**StepType** | **string** | Type of the step in an agent turn. | 
**StepId** | **string** |  | 
**Delta** | [**ContentDelta**](ContentDelta.md) |  | 

## Methods

### NewAgentTurnResponseStepProgressPayload

`func NewAgentTurnResponseStepProgressPayload(eventType string, stepType string, stepId string, delta ContentDelta, ) *AgentTurnResponseStepProgressPayload`

NewAgentTurnResponseStepProgressPayload instantiates a new AgentTurnResponseStepProgressPayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentTurnResponseStepProgressPayloadWithDefaults

`func NewAgentTurnResponseStepProgressPayloadWithDefaults() *AgentTurnResponseStepProgressPayload`

NewAgentTurnResponseStepProgressPayloadWithDefaults instantiates a new AgentTurnResponseStepProgressPayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEventType

`func (o *AgentTurnResponseStepProgressPayload) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *AgentTurnResponseStepProgressPayload) GetEventTypeOk() (*string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventType

`func (o *AgentTurnResponseStepProgressPayload) SetEventType(v string)`

SetEventType sets EventType field to given value.


### GetStepType

`func (o *AgentTurnResponseStepProgressPayload) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *AgentTurnResponseStepProgressPayload) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *AgentTurnResponseStepProgressPayload) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetStepId

`func (o *AgentTurnResponseStepProgressPayload) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *AgentTurnResponseStepProgressPayload) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *AgentTurnResponseStepProgressPayload) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetDelta

`func (o *AgentTurnResponseStepProgressPayload) GetDelta() ContentDelta`

GetDelta returns the Delta field if non-nil, zero value otherwise.

### GetDeltaOk

`func (o *AgentTurnResponseStepProgressPayload) GetDeltaOk() (*ContentDelta, bool)`

GetDeltaOk returns a tuple with the Delta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDelta

`func (o *AgentTurnResponseStepProgressPayload) SetDelta(v ContentDelta)`

SetDelta sets Delta field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


