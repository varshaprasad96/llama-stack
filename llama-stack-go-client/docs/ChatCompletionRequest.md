# ChatCompletionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ModelId** | **string** | The identifier of the model to use. The model must be registered with Llama Stack and available via the /models endpoint. | 
**Messages** | [**[]Message**](Message.md) | List of messages in the conversation | 
**SamplingParams** | Pointer to [**SamplingParams**](SamplingParams.md) | Parameters to control the sampling strategy | [optional] 
**Tools** | Pointer to [**[]ToolDefinition**](ToolDefinition.md) | (Optional) List of tool definitions available to the model | [optional] 
**ToolChoice** | Pointer to **string** | (Optional) Whether tool use is required or automatic. Defaults to ToolChoice.auto. .. deprecated:: Use tool_config instead. | [optional] 
**ToolPromptFormat** | Pointer to **string** | (Optional) Instructs the model how to format tool calls. By default, Llama Stack will attempt to use a format that is best adapted to the model. - &#x60;ToolPromptFormat.json&#x60;: The tool calls are formatted as a JSON object. - &#x60;ToolPromptFormat.function_tag&#x60;: The tool calls are enclosed in a &lt;function&#x3D;function_name&gt; tag. - &#x60;ToolPromptFormat.python_list&#x60;: The tool calls are output as Python syntax -- a list of function calls. .. deprecated:: Use tool_config instead. | [optional] 
**ResponseFormat** | Pointer to [**ResponseFormat**](ResponseFormat.md) | (Optional) Grammar specification for guided (structured) decoding. There are two options: - &#x60;ResponseFormat.json_schema&#x60;: The grammar is a JSON schema. Most providers support this format. - &#x60;ResponseFormat.grammar&#x60;: The grammar is a BNF grammar. This format is more flexible, but not all providers support it. | [optional] 
**Stream** | Pointer to **bool** | (Optional) If True, generate an SSE event stream of the response. Defaults to False. | [optional] 
**Logprobs** | Pointer to [**ChatCompletionRequestLogprobs**](ChatCompletionRequestLogprobs.md) |  | [optional] 
**ToolConfig** | Pointer to [**ToolConfig**](ToolConfig.md) | (Optional) Configuration for tool use. | [optional] 

## Methods

### NewChatCompletionRequest

`func NewChatCompletionRequest(modelId string, messages []Message, ) *ChatCompletionRequest`

NewChatCompletionRequest instantiates a new ChatCompletionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChatCompletionRequestWithDefaults

`func NewChatCompletionRequestWithDefaults() *ChatCompletionRequest`

NewChatCompletionRequestWithDefaults instantiates a new ChatCompletionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModelId

`func (o *ChatCompletionRequest) GetModelId() string`

GetModelId returns the ModelId field if non-nil, zero value otherwise.

### GetModelIdOk

`func (o *ChatCompletionRequest) GetModelIdOk() (*string, bool)`

GetModelIdOk returns a tuple with the ModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelId

`func (o *ChatCompletionRequest) SetModelId(v string)`

SetModelId sets ModelId field to given value.


### GetMessages

`func (o *ChatCompletionRequest) GetMessages() []Message`

GetMessages returns the Messages field if non-nil, zero value otherwise.

### GetMessagesOk

`func (o *ChatCompletionRequest) GetMessagesOk() (*[]Message, bool)`

GetMessagesOk returns a tuple with the Messages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessages

`func (o *ChatCompletionRequest) SetMessages(v []Message)`

SetMessages sets Messages field to given value.


### GetSamplingParams

`func (o *ChatCompletionRequest) GetSamplingParams() SamplingParams`

GetSamplingParams returns the SamplingParams field if non-nil, zero value otherwise.

### GetSamplingParamsOk

`func (o *ChatCompletionRequest) GetSamplingParamsOk() (*SamplingParams, bool)`

GetSamplingParamsOk returns a tuple with the SamplingParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamplingParams

`func (o *ChatCompletionRequest) SetSamplingParams(v SamplingParams)`

SetSamplingParams sets SamplingParams field to given value.

### HasSamplingParams

`func (o *ChatCompletionRequest) HasSamplingParams() bool`

HasSamplingParams returns a boolean if a field has been set.

### GetTools

`func (o *ChatCompletionRequest) GetTools() []ToolDefinition`

GetTools returns the Tools field if non-nil, zero value otherwise.

### GetToolsOk

`func (o *ChatCompletionRequest) GetToolsOk() (*[]ToolDefinition, bool)`

GetToolsOk returns a tuple with the Tools field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTools

`func (o *ChatCompletionRequest) SetTools(v []ToolDefinition)`

SetTools sets Tools field to given value.

### HasTools

`func (o *ChatCompletionRequest) HasTools() bool`

HasTools returns a boolean if a field has been set.

### GetToolChoice

`func (o *ChatCompletionRequest) GetToolChoice() string`

GetToolChoice returns the ToolChoice field if non-nil, zero value otherwise.

### GetToolChoiceOk

`func (o *ChatCompletionRequest) GetToolChoiceOk() (*string, bool)`

GetToolChoiceOk returns a tuple with the ToolChoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolChoice

`func (o *ChatCompletionRequest) SetToolChoice(v string)`

SetToolChoice sets ToolChoice field to given value.

### HasToolChoice

`func (o *ChatCompletionRequest) HasToolChoice() bool`

HasToolChoice returns a boolean if a field has been set.

### GetToolPromptFormat

`func (o *ChatCompletionRequest) GetToolPromptFormat() string`

GetToolPromptFormat returns the ToolPromptFormat field if non-nil, zero value otherwise.

### GetToolPromptFormatOk

`func (o *ChatCompletionRequest) GetToolPromptFormatOk() (*string, bool)`

GetToolPromptFormatOk returns a tuple with the ToolPromptFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolPromptFormat

`func (o *ChatCompletionRequest) SetToolPromptFormat(v string)`

SetToolPromptFormat sets ToolPromptFormat field to given value.

### HasToolPromptFormat

`func (o *ChatCompletionRequest) HasToolPromptFormat() bool`

HasToolPromptFormat returns a boolean if a field has been set.

### GetResponseFormat

`func (o *ChatCompletionRequest) GetResponseFormat() ResponseFormat`

GetResponseFormat returns the ResponseFormat field if non-nil, zero value otherwise.

### GetResponseFormatOk

`func (o *ChatCompletionRequest) GetResponseFormatOk() (*ResponseFormat, bool)`

GetResponseFormatOk returns a tuple with the ResponseFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseFormat

`func (o *ChatCompletionRequest) SetResponseFormat(v ResponseFormat)`

SetResponseFormat sets ResponseFormat field to given value.

### HasResponseFormat

`func (o *ChatCompletionRequest) HasResponseFormat() bool`

HasResponseFormat returns a boolean if a field has been set.

### GetStream

`func (o *ChatCompletionRequest) GetStream() bool`

GetStream returns the Stream field if non-nil, zero value otherwise.

### GetStreamOk

`func (o *ChatCompletionRequest) GetStreamOk() (*bool, bool)`

GetStreamOk returns a tuple with the Stream field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStream

`func (o *ChatCompletionRequest) SetStream(v bool)`

SetStream sets Stream field to given value.

### HasStream

`func (o *ChatCompletionRequest) HasStream() bool`

HasStream returns a boolean if a field has been set.

### GetLogprobs

`func (o *ChatCompletionRequest) GetLogprobs() ChatCompletionRequestLogprobs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *ChatCompletionRequest) GetLogprobsOk() (*ChatCompletionRequestLogprobs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *ChatCompletionRequest) SetLogprobs(v ChatCompletionRequestLogprobs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *ChatCompletionRequest) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.

### GetToolConfig

`func (o *ChatCompletionRequest) GetToolConfig() ToolConfig`

GetToolConfig returns the ToolConfig field if non-nil, zero value otherwise.

### GetToolConfigOk

`func (o *ChatCompletionRequest) GetToolConfigOk() (*ToolConfig, bool)`

GetToolConfigOk returns a tuple with the ToolConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolConfig

`func (o *ChatCompletionRequest) SetToolConfig(v ToolConfig)`

SetToolConfig sets ToolConfig field to given value.

### HasToolConfig

`func (o *ChatCompletionRequest) HasToolConfig() bool`

HasToolConfig returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


