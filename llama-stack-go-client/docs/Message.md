# Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;assistant\&quot; to identify this as the model&#39;s response | [default to "assistant"]
**Content** | [**InterleavedContent**](InterleavedContent.md) | The content of the model&#39;s response | 
**Context** | Pointer to [**InterleavedContent**](InterleavedContent.md) | (Optional) This field is used internally by Llama Stack to pass RAG context. This field may be removed in the API in the future. | [optional] 
**CallId** | **string** | Unique identifier for the tool call this response is for | 
**StopReason** | **string** | Reason why the model stopped generating. Options are: - &#x60;StopReason.end_of_turn&#x60;: The model finished generating the entire response. - &#x60;StopReason.end_of_message&#x60;: The model finished generating but generated a partial response -- usually, a tool call. The user may call the tool and continue the conversation with the tool&#39;s response. - &#x60;StopReason.out_of_tokens&#x60;: The model ran out of token budget. | 
**ToolCalls** | Pointer to [**[]ToolCall**](ToolCall.md) | List of tool calls. Each tool call is a ToolCall object. | [optional] 

## Methods

### NewMessage

`func NewMessage(role string, content InterleavedContent, callId string, stopReason string, ) *Message`

NewMessage instantiates a new Message object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMessageWithDefaults

`func NewMessageWithDefaults() *Message`

NewMessageWithDefaults instantiates a new Message object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *Message) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *Message) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *Message) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *Message) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *Message) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *Message) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.


### GetContext

`func (o *Message) GetContext() InterleavedContent`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *Message) GetContextOk() (*InterleavedContent, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *Message) SetContext(v InterleavedContent)`

SetContext sets Context field to given value.

### HasContext

`func (o *Message) HasContext() bool`

HasContext returns a boolean if a field has been set.

### GetCallId

`func (o *Message) GetCallId() string`

GetCallId returns the CallId field if non-nil, zero value otherwise.

### GetCallIdOk

`func (o *Message) GetCallIdOk() (*string, bool)`

GetCallIdOk returns a tuple with the CallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCallId

`func (o *Message) SetCallId(v string)`

SetCallId sets CallId field to given value.


### GetStopReason

`func (o *Message) GetStopReason() string`

GetStopReason returns the StopReason field if non-nil, zero value otherwise.

### GetStopReasonOk

`func (o *Message) GetStopReasonOk() (*string, bool)`

GetStopReasonOk returns a tuple with the StopReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStopReason

`func (o *Message) SetStopReason(v string)`

SetStopReason sets StopReason field to given value.


### GetToolCalls

`func (o *Message) GetToolCalls() []ToolCall`

GetToolCalls returns the ToolCalls field if non-nil, zero value otherwise.

### GetToolCallsOk

`func (o *Message) GetToolCallsOk() (*[]ToolCall, bool)`

GetToolCallsOk returns a tuple with the ToolCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCalls

`func (o *Message) SetToolCalls(v []ToolCall)`

SetToolCalls sets ToolCalls field to given value.

### HasToolCalls

`func (o *Message) HasToolCalls() bool`

HasToolCalls returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


