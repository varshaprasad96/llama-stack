# AgentTurnResponseTurnAwaitingInputPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventType** | **string** |  | [default to "turn_awaiting_input"]
**Turn** | [**Turn**](Turn.md) |  | 

## Methods

### NewAgentTurnResponseTurnAwaitingInputPayload

`func NewAgentTurnResponseTurnAwaitingInputPayload(eventType string, turn Turn, ) *AgentTurnResponseTurnAwaitingInputPayload`

NewAgentTurnResponseTurnAwaitingInputPayload instantiates a new AgentTurnResponseTurnAwaitingInputPayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentTurnResponseTurnAwaitingInputPayloadWithDefaults

`func NewAgentTurnResponseTurnAwaitingInputPayloadWithDefaults() *AgentTurnResponseTurnAwaitingInputPayload`

NewAgentTurnResponseTurnAwaitingInputPayloadWithDefaults instantiates a new AgentTurnResponseTurnAwaitingInputPayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEventType

`func (o *AgentTurnResponseTurnAwaitingInputPayload) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *AgentTurnResponseTurnAwaitingInputPayload) GetEventTypeOk() (*string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventType

`func (o *AgentTurnResponseTurnAwaitingInputPayload) SetEventType(v string)`

SetEventType sets EventType field to given value.


### GetTurn

`func (o *AgentTurnResponseTurnAwaitingInputPayload) GetTurn() Turn`

GetTurn returns the Turn field if non-nil, zero value otherwise.

### GetTurnOk

`func (o *AgentTurnResponseTurnAwaitingInputPayload) GetTurnOk() (*Turn, bool)`

GetTurnOk returns a tuple with the Turn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurn

`func (o *AgentTurnResponseTurnAwaitingInputPayload) SetTurn(v Turn)`

SetTurn sets Turn field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


