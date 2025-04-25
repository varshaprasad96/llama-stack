# AgentTurnResponseEventPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventType** | **string** |  | [default to "turn_awaiting_input"]
**StepType** | **string** | Type of the step in an agent turn. | 
**StepId** | **string** |  | 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 
**Delta** | [**ContentDelta**](ContentDelta.md) |  | 
**StepDetails** | [**TurnStepsInner**](TurnStepsInner.md) |  | 
**TurnId** | **string** |  | 
**Turn** | [**Turn**](Turn.md) |  | 

## Methods

### NewAgentTurnResponseEventPayload

`func NewAgentTurnResponseEventPayload(eventType string, stepType string, stepId string, delta ContentDelta, stepDetails TurnStepsInner, turnId string, turn Turn, ) *AgentTurnResponseEventPayload`

NewAgentTurnResponseEventPayload instantiates a new AgentTurnResponseEventPayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentTurnResponseEventPayloadWithDefaults

`func NewAgentTurnResponseEventPayloadWithDefaults() *AgentTurnResponseEventPayload`

NewAgentTurnResponseEventPayloadWithDefaults instantiates a new AgentTurnResponseEventPayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEventType

`func (o *AgentTurnResponseEventPayload) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *AgentTurnResponseEventPayload) GetEventTypeOk() (*string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventType

`func (o *AgentTurnResponseEventPayload) SetEventType(v string)`

SetEventType sets EventType field to given value.


### GetStepType

`func (o *AgentTurnResponseEventPayload) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *AgentTurnResponseEventPayload) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *AgentTurnResponseEventPayload) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetStepId

`func (o *AgentTurnResponseEventPayload) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *AgentTurnResponseEventPayload) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *AgentTurnResponseEventPayload) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetMetadata

`func (o *AgentTurnResponseEventPayload) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *AgentTurnResponseEventPayload) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *AgentTurnResponseEventPayload) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *AgentTurnResponseEventPayload) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetDelta

`func (o *AgentTurnResponseEventPayload) GetDelta() ContentDelta`

GetDelta returns the Delta field if non-nil, zero value otherwise.

### GetDeltaOk

`func (o *AgentTurnResponseEventPayload) GetDeltaOk() (*ContentDelta, bool)`

GetDeltaOk returns a tuple with the Delta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDelta

`func (o *AgentTurnResponseEventPayload) SetDelta(v ContentDelta)`

SetDelta sets Delta field to given value.


### GetStepDetails

`func (o *AgentTurnResponseEventPayload) GetStepDetails() TurnStepsInner`

GetStepDetails returns the StepDetails field if non-nil, zero value otherwise.

### GetStepDetailsOk

`func (o *AgentTurnResponseEventPayload) GetStepDetailsOk() (*TurnStepsInner, bool)`

GetStepDetailsOk returns a tuple with the StepDetails field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepDetails

`func (o *AgentTurnResponseEventPayload) SetStepDetails(v TurnStepsInner)`

SetStepDetails sets StepDetails field to given value.


### GetTurnId

`func (o *AgentTurnResponseEventPayload) GetTurnId() string`

GetTurnId returns the TurnId field if non-nil, zero value otherwise.

### GetTurnIdOk

`func (o *AgentTurnResponseEventPayload) GetTurnIdOk() (*string, bool)`

GetTurnIdOk returns a tuple with the TurnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurnId

`func (o *AgentTurnResponseEventPayload) SetTurnId(v string)`

SetTurnId sets TurnId field to given value.


### GetTurn

`func (o *AgentTurnResponseEventPayload) GetTurn() Turn`

GetTurn returns the Turn field if non-nil, zero value otherwise.

### GetTurnOk

`func (o *AgentTurnResponseEventPayload) GetTurnOk() (*Turn, bool)`

GetTurnOk returns a tuple with the Turn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurn

`func (o *AgentTurnResponseEventPayload) SetTurn(v Turn)`

SetTurn sets Turn field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


