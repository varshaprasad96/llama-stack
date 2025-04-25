# CreateAgentTurnRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Messages** | [**[]CreateAgentTurnRequestMessagesInner**](CreateAgentTurnRequestMessagesInner.md) | List of messages to start the turn with. | 
**Stream** | Pointer to **bool** | (Optional) If True, generate an SSE event stream of the response. Defaults to False. | [optional] 
**Documents** | Pointer to [**[]Document**](Document.md) | (Optional) List of documents to create the turn with. | [optional] 
**Toolgroups** | Pointer to [**[]AgentTool**](AgentTool.md) | (Optional) List of toolgroups to create the turn with, will be used in addition to the agent&#39;s config toolgroups for the request. | [optional] 
**ToolConfig** | Pointer to [**ToolConfig**](ToolConfig.md) | (Optional) The tool configuration to create the turn with, will be used to override the agent&#39;s tool_config. | [optional] 

## Methods

### NewCreateAgentTurnRequest

`func NewCreateAgentTurnRequest(messages []CreateAgentTurnRequestMessagesInner, ) *CreateAgentTurnRequest`

NewCreateAgentTurnRequest instantiates a new CreateAgentTurnRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAgentTurnRequestWithDefaults

`func NewCreateAgentTurnRequestWithDefaults() *CreateAgentTurnRequest`

NewCreateAgentTurnRequestWithDefaults instantiates a new CreateAgentTurnRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMessages

`func (o *CreateAgentTurnRequest) GetMessages() []CreateAgentTurnRequestMessagesInner`

GetMessages returns the Messages field if non-nil, zero value otherwise.

### GetMessagesOk

`func (o *CreateAgentTurnRequest) GetMessagesOk() (*[]CreateAgentTurnRequestMessagesInner, bool)`

GetMessagesOk returns a tuple with the Messages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessages

`func (o *CreateAgentTurnRequest) SetMessages(v []CreateAgentTurnRequestMessagesInner)`

SetMessages sets Messages field to given value.


### GetStream

`func (o *CreateAgentTurnRequest) GetStream() bool`

GetStream returns the Stream field if non-nil, zero value otherwise.

### GetStreamOk

`func (o *CreateAgentTurnRequest) GetStreamOk() (*bool, bool)`

GetStreamOk returns a tuple with the Stream field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStream

`func (o *CreateAgentTurnRequest) SetStream(v bool)`

SetStream sets Stream field to given value.

### HasStream

`func (o *CreateAgentTurnRequest) HasStream() bool`

HasStream returns a boolean if a field has been set.

### GetDocuments

`func (o *CreateAgentTurnRequest) GetDocuments() []Document`

GetDocuments returns the Documents field if non-nil, zero value otherwise.

### GetDocumentsOk

`func (o *CreateAgentTurnRequest) GetDocumentsOk() (*[]Document, bool)`

GetDocumentsOk returns a tuple with the Documents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDocuments

`func (o *CreateAgentTurnRequest) SetDocuments(v []Document)`

SetDocuments sets Documents field to given value.

### HasDocuments

`func (o *CreateAgentTurnRequest) HasDocuments() bool`

HasDocuments returns a boolean if a field has been set.

### GetToolgroups

`func (o *CreateAgentTurnRequest) GetToolgroups() []AgentTool`

GetToolgroups returns the Toolgroups field if non-nil, zero value otherwise.

### GetToolgroupsOk

`func (o *CreateAgentTurnRequest) GetToolgroupsOk() (*[]AgentTool, bool)`

GetToolgroupsOk returns a tuple with the Toolgroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolgroups

`func (o *CreateAgentTurnRequest) SetToolgroups(v []AgentTool)`

SetToolgroups sets Toolgroups field to given value.

### HasToolgroups

`func (o *CreateAgentTurnRequest) HasToolgroups() bool`

HasToolgroups returns a boolean if a field has been set.

### GetToolConfig

`func (o *CreateAgentTurnRequest) GetToolConfig() ToolConfig`

GetToolConfig returns the ToolConfig field if non-nil, zero value otherwise.

### GetToolConfigOk

`func (o *CreateAgentTurnRequest) GetToolConfigOk() (*ToolConfig, bool)`

GetToolConfigOk returns a tuple with the ToolConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolConfig

`func (o *CreateAgentTurnRequest) SetToolConfig(v ToolConfig)`

SetToolConfig sets ToolConfig field to given value.

### HasToolConfig

`func (o *CreateAgentTurnRequest) HasToolConfig() bool`

HasToolConfig returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


