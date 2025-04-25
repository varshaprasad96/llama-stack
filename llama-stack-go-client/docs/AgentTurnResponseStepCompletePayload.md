# AgentTurnResponseStepCompletePayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventType** | **string** |  | [default to "step_complete"]
**StepType** | **string** | Type of the step in an agent turn. | 
**StepId** | **string** |  | 
**StepDetails** | [**TurnStepsInner**](TurnStepsInner.md) |  | 

## Methods

### NewAgentTurnResponseStepCompletePayload

`func NewAgentTurnResponseStepCompletePayload(eventType string, stepType string, stepId string, stepDetails TurnStepsInner, ) *AgentTurnResponseStepCompletePayload`

NewAgentTurnResponseStepCompletePayload instantiates a new AgentTurnResponseStepCompletePayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentTurnResponseStepCompletePayloadWithDefaults

`func NewAgentTurnResponseStepCompletePayloadWithDefaults() *AgentTurnResponseStepCompletePayload`

NewAgentTurnResponseStepCompletePayloadWithDefaults instantiates a new AgentTurnResponseStepCompletePayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEventType

`func (o *AgentTurnResponseStepCompletePayload) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *AgentTurnResponseStepCompletePayload) GetEventTypeOk() (*string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventType

`func (o *AgentTurnResponseStepCompletePayload) SetEventType(v string)`

SetEventType sets EventType field to given value.


### GetStepType

`func (o *AgentTurnResponseStepCompletePayload) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *AgentTurnResponseStepCompletePayload) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *AgentTurnResponseStepCompletePayload) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetStepId

`func (o *AgentTurnResponseStepCompletePayload) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *AgentTurnResponseStepCompletePayload) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *AgentTurnResponseStepCompletePayload) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetStepDetails

`func (o *AgentTurnResponseStepCompletePayload) GetStepDetails() TurnStepsInner`

GetStepDetails returns the StepDetails field if non-nil, zero value otherwise.

### GetStepDetailsOk

`func (o *AgentTurnResponseStepCompletePayload) GetStepDetailsOk() (*TurnStepsInner, bool)`

GetStepDetailsOk returns a tuple with the StepDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepDetails

`func (o *AgentTurnResponseStepCompletePayload) SetStepDetails(v TurnStepsInner)`

SetStepDetails sets StepDetails field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


