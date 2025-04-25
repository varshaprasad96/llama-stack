# Agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AgentId** | **string** |  | 
**AgentConfig** | [**AgentConfig**](AgentConfig.md) |  | 
**CreatedAt** | **time.Time** |  | 

## Methods

### NewAgent

`func NewAgent(agentId string, agentConfig AgentConfig, createdAt time.Time, ) *Agent`

NewAgent instantiates a new Agent object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentWithDefaults

`func NewAgentWithDefaults() *Agent`

NewAgentWithDefaults instantiates a new Agent object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAgentId

`func (o *Agent) GetAgentId() string`

GetAgentId returns the AgentId field if non-nil, zero value otherwise.

### GetAgentIdOk

`func (o *Agent) GetAgentIdOk() (*string, bool)`

GetAgentIdOk returns a tuple with the AgentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAgentId

`func (o *Agent) SetAgentId(v string)`

SetAgentId sets AgentId field to given value.


### GetAgentConfig

`func (o *Agent) GetAgentConfig() AgentConfig`

GetAgentConfig returns the AgentConfig field if non-nil, zero value otherwise.

### GetAgentConfigOk

`func (o *Agent) GetAgentConfigOk() (*AgentConfig, bool)`

GetAgentConfigOk returns a tuple with the AgentConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAgentConfig

`func (o *Agent) SetAgentConfig(v AgentConfig)`

SetAgentConfig sets AgentConfig field to given value.


### GetCreatedAt

`func (o *Agent) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Agent) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Agent) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


