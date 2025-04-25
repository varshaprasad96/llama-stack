# OpenAIAssistantMessageParam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;assistant\&quot; to identify this as the model&#39;s response | [default to "assistant"]
**Content** | Pointer to [**OpenAIAssistantMessageParamContent**](OpenAIAssistantMessageParamContent.md) |  | [optional] 
**Name** | Pointer to **string** | (Optional) The name of the assistant message participant. | [optional] 
**ToolCalls** | Pointer to [**[]OpenAIChatCompletionToolCall**](OpenAIChatCompletionToolCall.md) | List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object. | [optional] 

## Methods

### NewOpenAIAssistantMessageParam

`func NewOpenAIAssistantMessageParam(role string, ) *OpenAIAssistantMessageParam`

NewOpenAIAssistantMessageParam instantiates a new OpenAIAssistantMessageParam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIAssistantMessageParamWithDefaults

`func NewOpenAIAssistantMessageParamWithDefaults() *OpenAIAssistantMessageParam`

NewOpenAIAssistantMessageParamWithDefaults instantiates a new OpenAIAssistantMessageParam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *OpenAIAssistantMessageParam) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *OpenAIAssistantMessageParam) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *OpenAIAssistantMessageParam) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *OpenAIAssistantMessageParam) GetContent() OpenAIAssistantMessageParamContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *OpenAIAssistantMessageParam) GetContentOk() (*OpenAIAssistantMessageParamContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *OpenAIAssistantMessageParam) SetContent(v OpenAIAssistantMessageParamContent)`

SetContent sets Content field to given value.

### HasContent

`func (o *OpenAIAssistantMessageParam) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetName

`func (o *OpenAIAssistantMessageParam) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *OpenAIAssistantMessageParam) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *OpenAIAssistantMessageParam) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *OpenAIAssistantMessageParam) HasName() bool`

HasName returns a boolean if a field has been set.

### GetToolCalls

`func (o *OpenAIAssistantMessageParam) GetToolCalls() []OpenAIChatCompletionToolCall`

GetToolCalls returns the ToolCalls field if non-nil, zero value otherwise.

### GetToolCallsOk

`func (o *OpenAIAssistantMessageParam) GetToolCallsOk() (*[]OpenAIChatCompletionToolCall, bool)`

GetToolCallsOk returns a tuple with the ToolCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCalls

`func (o *OpenAIAssistantMessageParam) SetToolCalls(v []OpenAIChatCompletionToolCall)`

SetToolCalls sets ToolCalls field to given value.

### HasToolCalls

`func (o *OpenAIAssistantMessageParam) HasToolCalls() bool`

HasToolCalls returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


