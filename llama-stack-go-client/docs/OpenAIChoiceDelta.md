# OpenAIChoiceDelta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | Pointer to **string** | (Optional) The content of the delta | [optional] 
**Refusal** | Pointer to **string** | (Optional) The refusal of the delta | [optional] 
**Role** | Pointer to **string** | (Optional) The role of the delta | [optional] 
**ToolCalls** | Pointer to [**[]OpenAIChatCompletionToolCall**](OpenAIChatCompletionToolCall.md) | (Optional) The tool calls of the delta | [optional] 

## Methods

### NewOpenAIChoiceDelta

`func NewOpenAIChoiceDelta() *OpenAIChoiceDelta`

NewOpenAIChoiceDelta instantiates a new OpenAIChoiceDelta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIChoiceDeltaWithDefaults

`func NewOpenAIChoiceDeltaWithDefaults() *OpenAIChoiceDelta`

NewOpenAIChoiceDeltaWithDefaults instantiates a new OpenAIChoiceDelta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *OpenAIChoiceDelta) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *OpenAIChoiceDelta) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *OpenAIChoiceDelta) SetContent(v string)`

SetContent sets Content field to given value.

### HasContent

`func (o *OpenAIChoiceDelta) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetRefusal

`func (o *OpenAIChoiceDelta) GetRefusal() string`

GetRefusal returns the Refusal field if non-nil, zero value otherwise.

### GetRefusalOk

`func (o *OpenAIChoiceDelta) GetRefusalOk() (*string, bool)`

GetRefusalOk returns a tuple with the Refusal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefusal

`func (o *OpenAIChoiceDelta) SetRefusal(v string)`

SetRefusal sets Refusal field to given value.

### HasRefusal

`func (o *OpenAIChoiceDelta) HasRefusal() bool`

HasRefusal returns a boolean if a field has been set.

### GetRole

`func (o *OpenAIChoiceDelta) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *OpenAIChoiceDelta) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *OpenAIChoiceDelta) SetRole(v string)`

SetRole sets Role field to given value.

### HasRole

`func (o *OpenAIChoiceDelta) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetToolCalls

`func (o *OpenAIChoiceDelta) GetToolCalls() []OpenAIChatCompletionToolCall`

GetToolCalls returns the ToolCalls field if non-nil, zero value otherwise.

### GetToolCallsOk

`func (o *OpenAIChoiceDelta) GetToolCallsOk() (*[]OpenAIChatCompletionToolCall, bool)`

GetToolCallsOk returns a tuple with the ToolCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCalls

`func (o *OpenAIChoiceDelta) SetToolCalls(v []OpenAIChatCompletionToolCall)`

SetToolCalls sets ToolCalls field to given value.

### HasToolCalls

`func (o *OpenAIChoiceDelta) HasToolCalls() bool`

HasToolCalls returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


