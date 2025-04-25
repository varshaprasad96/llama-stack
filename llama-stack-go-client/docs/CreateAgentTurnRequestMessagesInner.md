# CreateAgentTurnRequestMessagesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;tool\&quot; to identify this as a tool response | [default to "tool"]
**Content** | [**InterleavedContent**](InterleavedContent.md) | The response content from the tool | 
**Context** | Pointer to [**InterleavedContent**](InterleavedContent.md) | (Optional) This field is used internally by Llama Stack to pass RAG context. This field may be removed in the API in the future. | [optional] 
**CallId** | **string** | Unique identifier for the tool call this response is for | 

## Methods

### NewCreateAgentTurnRequestMessagesInner

`func NewCreateAgentTurnRequestMessagesInner(role string, content InterleavedContent, callId string, ) *CreateAgentTurnRequestMessagesInner`

NewCreateAgentTurnRequestMessagesInner instantiates a new CreateAgentTurnRequestMessagesInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAgentTurnRequestMessagesInnerWithDefaults

`func NewCreateAgentTurnRequestMessagesInnerWithDefaults() *CreateAgentTurnRequestMessagesInner`

NewCreateAgentTurnRequestMessagesInnerWithDefaults instantiates a new CreateAgentTurnRequestMessagesInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *CreateAgentTurnRequestMessagesInner) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *CreateAgentTurnRequestMessagesInner) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *CreateAgentTurnRequestMessagesInner) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *CreateAgentTurnRequestMessagesInner) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *CreateAgentTurnRequestMessagesInner) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *CreateAgentTurnRequestMessagesInner) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.


### GetContext

`func (o *CreateAgentTurnRequestMessagesInner) GetContext() InterleavedContent`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *CreateAgentTurnRequestMessagesInner) GetContextOk() (*InterleavedContent, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *CreateAgentTurnRequestMessagesInner) SetContext(v InterleavedContent)`

SetContext sets Context field to given value.

### HasContext

`func (o *CreateAgentTurnRequestMessagesInner) HasContext() bool`

HasContext returns a boolean if a field has been set.

### GetCallId

`func (o *CreateAgentTurnRequestMessagesInner) GetCallId() string`

GetCallId returns the CallId field if non-nil, zero value otherwise.

### GetCallIdOk

`func (o *CreateAgentTurnRequestMessagesInner) GetCallIdOk() (*string, bool)`

GetCallIdOk returns a tuple with the CallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCallId

`func (o *CreateAgentTurnRequestMessagesInner) SetCallId(v string)`

SetCallId sets CallId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


