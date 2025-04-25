# AgentTurnResponseStepStartPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventType** | **string** |  | [default to "step_start"]
**StepType** | **string** | Type of the step in an agent turn. | 
**StepId** | **string** |  | 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewAgentTurnResponseStepStartPayload

`func NewAgentTurnResponseStepStartPayload(eventType string, stepType string, stepId string, ) *AgentTurnResponseStepStartPayload`

NewAgentTurnResponseStepStartPayload instantiates a new AgentTurnResponseStepStartPayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentTurnResponseStepStartPayloadWithDefaults

`func NewAgentTurnResponseStepStartPayloadWithDefaults() *AgentTurnResponseStepStartPayload`

NewAgentTurnResponseStepStartPayloadWithDefaults instantiates a new AgentTurnResponseStepStartPayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEventType

`func (o *AgentTurnResponseStepStartPayload) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *AgentTurnResponseStepStartPayload) GetEventTypeOk() (*string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventType

`func (o *AgentTurnResponseStepStartPayload) SetEventType(v string)`

SetEventType sets EventType field to given value.


### GetStepType

`func (o *AgentTurnResponseStepStartPayload) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *AgentTurnResponseStepStartPayload) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *AgentTurnResponseStepStartPayload) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetStepId

`func (o *AgentTurnResponseStepStartPayload) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *AgentTurnResponseStepStartPayload) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *AgentTurnResponseStepStartPayload) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetMetadata

`func (o *AgentTurnResponseStepStartPayload) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *AgentTurnResponseStepStartPayload) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *AgentTurnResponseStepStartPayload) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *AgentTurnResponseStepStartPayload) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


