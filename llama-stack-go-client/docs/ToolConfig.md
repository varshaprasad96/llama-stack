# ToolConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ToolChoice** | Pointer to [**ToolConfigToolChoice**](ToolConfigToolChoice.md) |  | [optional] [default to auto]
**ToolPromptFormat** | Pointer to **string** | (Optional) Instructs the model how to format tool calls. By default, Llama Stack will attempt to use a format that is best adapted to the model. - &#x60;ToolPromptFormat.json&#x60;: The tool calls are formatted as a JSON object. - &#x60;ToolPromptFormat.function_tag&#x60;: The tool calls are enclosed in a &lt;function&#x3D;function_name&gt; tag. - &#x60;ToolPromptFormat.python_list&#x60;: The tool calls are output as Python syntax -- a list of function calls. | [optional] 
**SystemMessageBehavior** | Pointer to **string** | (Optional) Config for how to override the default system prompt. - &#x60;SystemMessageBehavior.append&#x60;: Appends the provided system message to the default system prompt. - &#x60;SystemMessageBehavior.replace&#x60;: Replaces the default system prompt with the provided system message. The system message can include the string &#39;{{function_definitions}}&#39; to indicate where the function definitions should be inserted. | [optional] [default to "append"]

## Methods

### NewToolConfig

`func NewToolConfig() *ToolConfig`

NewToolConfig instantiates a new ToolConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolConfigWithDefaults

`func NewToolConfigWithDefaults() *ToolConfig`

NewToolConfigWithDefaults instantiates a new ToolConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetToolChoice

`func (o *ToolConfig) GetToolChoice() ToolConfigToolChoice`

GetToolChoice returns the ToolChoice field if non-nil, zero value otherwise.

### GetToolChoiceOk

`func (o *ToolConfig) GetToolChoiceOk() (*ToolConfigToolChoice, bool)`

GetToolChoiceOk returns a tuple with the ToolChoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolChoice

`func (o *ToolConfig) SetToolChoice(v ToolConfigToolChoice)`

SetToolChoice sets ToolChoice field to given value.

### HasToolChoice

`func (o *ToolConfig) HasToolChoice() bool`

HasToolChoice returns a boolean if a field has been set.

### GetToolPromptFormat

`func (o *ToolConfig) GetToolPromptFormat() string`

GetToolPromptFormat returns the ToolPromptFormat field if non-nil, zero value otherwise.

### GetToolPromptFormatOk

`func (o *ToolConfig) GetToolPromptFormatOk() (*string, bool)`

GetToolPromptFormatOk returns a tuple with the ToolPromptFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolPromptFormat

`func (o *ToolConfig) SetToolPromptFormat(v string)`

SetToolPromptFormat sets ToolPromptFormat field to given value.

### HasToolPromptFormat

`func (o *ToolConfig) HasToolPromptFormat() bool`

HasToolPromptFormat returns a boolean if a field has been set.

### GetSystemMessageBehavior

`func (o *ToolConfig) GetSystemMessageBehavior() string`

GetSystemMessageBehavior returns the SystemMessageBehavior field if non-nil, zero value otherwise.

### GetSystemMessageBehaviorOk

`func (o *ToolConfig) GetSystemMessageBehaviorOk() (*string, bool)`

GetSystemMessageBehaviorOk returns a tuple with the SystemMessageBehavior field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSystemMessageBehavior

`func (o *ToolConfig) SetSystemMessageBehavior(v string)`

SetSystemMessageBehavior sets SystemMessageBehavior field to given value.

### HasSystemMessageBehavior

`func (o *ToolConfig) HasSystemMessageBehavior() bool`

HasSystemMessageBehavior returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


