# CreateAgentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AgentConfig** | [**AgentConfig**](AgentConfig.md) | The configuration for the agent. | 

## Methods

### NewCreateAgentRequest

`func NewCreateAgentRequest(agentConfig AgentConfig, ) *CreateAgentRequest`

NewCreateAgentRequest instantiates a new CreateAgentRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAgentRequestWithDefaults

`func NewCreateAgentRequestWithDefaults() *CreateAgentRequest`

NewCreateAgentRequestWithDefaults instantiates a new CreateAgentRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAgentConfig

`func (o *CreateAgentRequest) GetAgentConfig() AgentConfig`

GetAgentConfig returns the AgentConfig field if non-nil, zero value otherwise.

### GetAgentConfigOk

`func (o *CreateAgentRequest) GetAgentConfigOk() (*AgentConfig, bool)`

GetAgentConfigOk returns a tuple with the AgentConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAgentConfig

`func (o *CreateAgentRequest) SetAgentConfig(v AgentConfig)`

SetAgentConfig sets AgentConfig field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


