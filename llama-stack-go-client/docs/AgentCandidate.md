# AgentCandidate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "agent"]
**Config** | [**AgentConfig**](AgentConfig.md) | The configuration for the agent candidate. | 

## Methods

### NewAgentCandidate

`func NewAgentCandidate(type_ string, config AgentConfig, ) *AgentCandidate`

NewAgentCandidate instantiates a new AgentCandidate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentCandidateWithDefaults

`func NewAgentCandidateWithDefaults() *AgentCandidate`

NewAgentCandidateWithDefaults instantiates a new AgentCandidate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *AgentCandidate) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AgentCandidate) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AgentCandidate) SetType(v string)`

SetType sets Type field to given value.


### GetConfig

`func (o *AgentCandidate) GetConfig() AgentConfig`

GetConfig returns the Config field if non-nil, zero value otherwise.

### GetConfigOk

`func (o *AgentCandidate) GetConfigOk() (*AgentConfig, bool)`

GetConfigOk returns a tuple with the Config field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConfig

`func (o *AgentCandidate) SetConfig(v AgentConfig)`

SetConfig sets Config field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


