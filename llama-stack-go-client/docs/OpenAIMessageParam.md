# OpenAIMessageParam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;developer\&quot; to identify this as a developer message | [default to "developer"]
**Content** | [**OpenAIDeveloperMessageParamContent**](OpenAIDeveloperMessageParamContent.md) |  | 
**Name** | Pointer to **string** | (Optional) The name of the developer message participant. | [optional] 
**ToolCalls** | Pointer to [**[]OpenAIChatCompletionToolCall**](OpenAIChatCompletionToolCall.md) | List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object. | [optional] 
**ToolCallId** | **string** | Unique identifier for the tool call this response is for | 

## Methods

### NewOpenAIMessageParam

`func NewOpenAIMessageParam(role string, content OpenAIDeveloperMessageParamContent, toolCallId string, ) *OpenAIMessageParam`

NewOpenAIMessageParam instantiates a new OpenAIMessageParam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIMessageParamWithDefaults

`func NewOpenAIMessageParamWithDefaults() *OpenAIMessageParam`

NewOpenAIMessageParamWithDefaults instantiates a new OpenAIMessageParam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *OpenAIMessageParam) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *OpenAIMessageParam) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *OpenAIMessageParam) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *OpenAIMessageParam) GetContent() OpenAIDeveloperMessageParamContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *OpenAIMessageParam) GetContentOk() (*OpenAIDeveloperMessageParamContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *OpenAIMessageParam) SetContent(v OpenAIDeveloperMessageParamContent)`

SetContent sets Content field to given value.


### GetName

`func (o *OpenAIMessageParam) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *OpenAIMessageParam) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *OpenAIMessageParam) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *OpenAIMessageParam) HasName() bool`

HasName returns a boolean if a field has been set.

### GetToolCalls

`func (o *OpenAIMessageParam) GetToolCalls() []OpenAIChatCompletionToolCall`

GetToolCalls returns the ToolCalls field if non-nil, zero value otherwise.

### GetToolCallsOk

`func (o *OpenAIMessageParam) GetToolCallsOk() (*[]OpenAIChatCompletionToolCall, bool)`

GetToolCallsOk returns a tuple with the ToolCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCalls

`func (o *OpenAIMessageParam) SetToolCalls(v []OpenAIChatCompletionToolCall)`

SetToolCalls sets ToolCalls field to given value.

### HasToolCalls

`func (o *OpenAIMessageParam) HasToolCalls() bool`

HasToolCalls returns a boolean if a field has been set.

### GetToolCallId

`func (o *OpenAIMessageParam) GetToolCallId() string`

GetToolCallId returns the ToolCallId field if non-nil, zero value otherwise.

### GetToolCallIdOk

`func (o *OpenAIMessageParam) GetToolCallIdOk() (*string, bool)`

GetToolCallIdOk returns a tuple with the ToolCallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCallId

`func (o *OpenAIMessageParam) SetToolCallId(v string)`

SetToolCallId sets ToolCallId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


