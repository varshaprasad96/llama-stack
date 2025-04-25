# BatchChatCompletionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ModelId** | **string** |  | 
**MessagesBatch** | [**[][]Message**]([]Message.md) |  | 
**SamplingParams** | Pointer to [**SamplingParams**](SamplingParams.md) |  | [optional] 
**Tools** | Pointer to [**[]ToolDefinition**](ToolDefinition.md) |  | [optional] 
**ToolConfig** | Pointer to [**ToolConfig**](ToolConfig.md) |  | [optional] 
**ResponseFormat** | Pointer to [**ResponseFormat**](ResponseFormat.md) |  | [optional] 
**Logprobs** | Pointer to [**LogProbConfig**](LogProbConfig.md) |  | [optional] 

## Methods

### NewBatchChatCompletionRequest

`func NewBatchChatCompletionRequest(modelId string, messagesBatch [][]Message, ) *BatchChatCompletionRequest`

NewBatchChatCompletionRequest instantiates a new BatchChatCompletionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchChatCompletionRequestWithDefaults

`func NewBatchChatCompletionRequestWithDefaults() *BatchChatCompletionRequest`

NewBatchChatCompletionRequestWithDefaults instantiates a new BatchChatCompletionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModelId

`func (o *BatchChatCompletionRequest) GetModelId() string`

GetModelId returns the ModelId field if non-nil, zero value otherwise.

### GetModelIdOk

`func (o *BatchChatCompletionRequest) GetModelIdOk() (*string, bool)`

GetModelIdOk returns a tuple with the ModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelId

`func (o *BatchChatCompletionRequest) SetModelId(v string)`

SetModelId sets ModelId field to given value.


### GetMessagesBatch

`func (o *BatchChatCompletionRequest) GetMessagesBatch() [][]Message`

GetMessagesBatch returns the MessagesBatch field if non-nil, zero value otherwise.

### GetMessagesBatchOk

`func (o *BatchChatCompletionRequest) GetMessagesBatchOk() (*[][]Message, bool)`

GetMessagesBatchOk returns a tuple with the MessagesBatch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessagesBatch

`func (o *BatchChatCompletionRequest) SetMessagesBatch(v [][]Message)`

SetMessagesBatch sets MessagesBatch field to given value.


### GetSamplingParams

`func (o *BatchChatCompletionRequest) GetSamplingParams() SamplingParams`

GetSamplingParams returns the SamplingParams field if non-nil, zero value otherwise.

### GetSamplingParamsOk

`func (o *BatchChatCompletionRequest) GetSamplingParamsOk() (*SamplingParams, bool)`

GetSamplingParamsOk returns a tuple with the SamplingParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamplingParams

`func (o *BatchChatCompletionRequest) SetSamplingParams(v SamplingParams)`

SetSamplingParams sets SamplingParams field to given value.

### HasSamplingParams

`func (o *BatchChatCompletionRequest) HasSamplingParams() bool`

HasSamplingParams returns a boolean if a field has been set.

### GetTools

`func (o *BatchChatCompletionRequest) GetTools() []ToolDefinition`

GetTools returns the Tools field if non-nil, zero value otherwise.

### GetToolsOk

`func (o *BatchChatCompletionRequest) GetToolsOk() (*[]ToolDefinition, bool)`

GetToolsOk returns a tuple with the Tools field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTools

`func (o *BatchChatCompletionRequest) SetTools(v []ToolDefinition)`

SetTools sets Tools field to given value.

### HasTools

`func (o *BatchChatCompletionRequest) HasTools() bool`

HasTools returns a boolean if a field has been set.

### GetToolConfig

`func (o *BatchChatCompletionRequest) GetToolConfig() ToolConfig`

GetToolConfig returns the ToolConfig field if non-nil, zero value otherwise.

### GetToolConfigOk

`func (o *BatchChatCompletionRequest) GetToolConfigOk() (*ToolConfig, bool)`

GetToolConfigOk returns a tuple with the ToolConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolConfig

`func (o *BatchChatCompletionRequest) SetToolConfig(v ToolConfig)`

SetToolConfig sets ToolConfig field to given value.

### HasToolConfig

`func (o *BatchChatCompletionRequest) HasToolConfig() bool`

HasToolConfig returns a boolean if a field has been set.

### GetResponseFormat

`func (o *BatchChatCompletionRequest) GetResponseFormat() ResponseFormat`

GetResponseFormat returns the ResponseFormat field if non-nil, zero value otherwise.

### GetResponseFormatOk

`func (o *BatchChatCompletionRequest) GetResponseFormatOk() (*ResponseFormat, bool)`

GetResponseFormatOk returns a tuple with the ResponseFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseFormat

`func (o *BatchChatCompletionRequest) SetResponseFormat(v ResponseFormat)`

SetResponseFormat sets ResponseFormat field to given value.

### HasResponseFormat

`func (o *BatchChatCompletionRequest) HasResponseFormat() bool`

HasResponseFormat returns a boolean if a field has been set.

### GetLogprobs

`func (o *BatchChatCompletionRequest) GetLogprobs() LogProbConfig`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *BatchChatCompletionRequest) GetLogprobsOk() (*LogProbConfig, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *BatchChatCompletionRequest) SetLogprobs(v LogProbConfig)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *BatchChatCompletionRequest) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


