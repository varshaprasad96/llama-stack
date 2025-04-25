# OpenaiChatCompletionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Model** | **string** | The identifier of the model to use. The model must be registered with Llama Stack and available via the /models endpoint. | 
**Messages** | [**[]OpenAIMessageParam**](OpenAIMessageParam.md) | List of messages in the conversation | 
**FrequencyPenalty** | Pointer to **float32** | (Optional) The penalty for repeated tokens | [optional] 
**FunctionCall** | Pointer to [**OpenaiChatCompletionRequestFunctionCall**](OpenaiChatCompletionRequestFunctionCall.md) |  | [optional] 
**Functions** | Pointer to [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | (Optional) List of functions to use | [optional] 
**LogitBias** | Pointer to **map[string]float32** | (Optional) The logit bias to use | [optional] 
**Logprobs** | Pointer to **bool** | (Optional) The log probabilities to use | [optional] 
**MaxCompletionTokens** | Pointer to **int32** | (Optional) The maximum number of tokens to generate | [optional] 
**MaxTokens** | Pointer to **int32** | (Optional) The maximum number of tokens to generate | [optional] 
**N** | Pointer to **int32** | (Optional) The number of completions to generate | [optional] 
**ParallelToolCalls** | Pointer to **bool** | (Optional) Whether to parallelize tool calls | [optional] 
**PresencePenalty** | Pointer to **float32** | (Optional) The penalty for repeated tokens | [optional] 
**ResponseFormat** | Pointer to [**OpenAIResponseFormatParam**](OpenAIResponseFormatParam.md) | (Optional) The response format to use | [optional] 
**Seed** | Pointer to **int32** | (Optional) The seed to use | [optional] 
**Stop** | Pointer to [**OpenaiChatCompletionRequestStop**](OpenaiChatCompletionRequestStop.md) |  | [optional] 
**Stream** | Pointer to **bool** | (Optional) Whether to stream the response | [optional] 
**StreamOptions** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | (Optional) The stream options to use | [optional] 
**Temperature** | Pointer to **float32** | (Optional) The temperature to use | [optional] 
**ToolChoice** | Pointer to [**OpenaiChatCompletionRequestToolChoice**](OpenaiChatCompletionRequestToolChoice.md) |  | [optional] 
**Tools** | Pointer to [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | (Optional) The tools to use | [optional] 
**TopLogprobs** | Pointer to **int32** | (Optional) The top log probabilities to use | [optional] 
**TopP** | Pointer to **float32** | (Optional) The top p to use | [optional] 
**User** | Pointer to **string** | (Optional) The user to use | [optional] 

## Methods

### NewOpenaiChatCompletionRequest

`func NewOpenaiChatCompletionRequest(model string, messages []OpenAIMessageParam, ) *OpenaiChatCompletionRequest`

NewOpenaiChatCompletionRequest instantiates a new OpenaiChatCompletionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenaiChatCompletionRequestWithDefaults

`func NewOpenaiChatCompletionRequestWithDefaults() *OpenaiChatCompletionRequest`

NewOpenaiChatCompletionRequestWithDefaults instantiates a new OpenaiChatCompletionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModel

`func (o *OpenaiChatCompletionRequest) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *OpenaiChatCompletionRequest) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *OpenaiChatCompletionRequest) SetModel(v string)`

SetModel sets Model field to given value.


### GetMessages

`func (o *OpenaiChatCompletionRequest) GetMessages() []OpenAIMessageParam`

GetMessages returns the Messages field if non-nil, zero value otherwise.

### GetMessagesOk

`func (o *OpenaiChatCompletionRequest) GetMessagesOk() (*[]OpenAIMessageParam, bool)`

GetMessagesOk returns a tuple with the Messages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessages

`func (o *OpenaiChatCompletionRequest) SetMessages(v []OpenAIMessageParam)`

SetMessages sets Messages field to given value.


### GetFrequencyPenalty

`func (o *OpenaiChatCompletionRequest) GetFrequencyPenalty() float32`

GetFrequencyPenalty returns the FrequencyPenalty field if non-nil, zero value otherwise.

### GetFrequencyPenaltyOk

`func (o *OpenaiChatCompletionRequest) GetFrequencyPenaltyOk() (*float32, bool)`

GetFrequencyPenaltyOk returns a tuple with the FrequencyPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrequencyPenalty

`func (o *OpenaiChatCompletionRequest) SetFrequencyPenalty(v float32)`

SetFrequencyPenalty sets FrequencyPenalty field to given value.

### HasFrequencyPenalty

`func (o *OpenaiChatCompletionRequest) HasFrequencyPenalty() bool`

HasFrequencyPenalty returns a boolean if a field has been set.

### GetFunctionCall

`func (o *OpenaiChatCompletionRequest) GetFunctionCall() OpenaiChatCompletionRequestFunctionCall`

GetFunctionCall returns the FunctionCall field if non-nil, zero value otherwise.

### GetFunctionCallOk

`func (o *OpenaiChatCompletionRequest) GetFunctionCallOk() (*OpenaiChatCompletionRequestFunctionCall, bool)`

GetFunctionCallOk returns a tuple with the FunctionCall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFunctionCall

`func (o *OpenaiChatCompletionRequest) SetFunctionCall(v OpenaiChatCompletionRequestFunctionCall)`

SetFunctionCall sets FunctionCall field to given value.

### HasFunctionCall

`func (o *OpenaiChatCompletionRequest) HasFunctionCall() bool`

HasFunctionCall returns a boolean if a field has been set.

### GetFunctions

`func (o *OpenaiChatCompletionRequest) GetFunctions() []map[string]AppendRowsRequestRowsInnerValue`

GetFunctions returns the Functions field if non-nil, zero value otherwise.

### GetFunctionsOk

`func (o *OpenaiChatCompletionRequest) GetFunctionsOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetFunctionsOk returns a tuple with the Functions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFunctions

`func (o *OpenaiChatCompletionRequest) SetFunctions(v []map[string]AppendRowsRequestRowsInnerValue)`

SetFunctions sets Functions field to given value.

### HasFunctions

`func (o *OpenaiChatCompletionRequest) HasFunctions() bool`

HasFunctions returns a boolean if a field has been set.

### GetLogitBias

`func (o *OpenaiChatCompletionRequest) GetLogitBias() map[string]float32`

GetLogitBias returns the LogitBias field if non-nil, zero value otherwise.

### GetLogitBiasOk

`func (o *OpenaiChatCompletionRequest) GetLogitBiasOk() (*map[string]float32, bool)`

GetLogitBiasOk returns a tuple with the LogitBias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogitBias

`func (o *OpenaiChatCompletionRequest) SetLogitBias(v map[string]float32)`

SetLogitBias sets LogitBias field to given value.

### HasLogitBias

`func (o *OpenaiChatCompletionRequest) HasLogitBias() bool`

HasLogitBias returns a boolean if a field has been set.

### GetLogprobs

`func (o *OpenaiChatCompletionRequest) GetLogprobs() bool`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *OpenaiChatCompletionRequest) GetLogprobsOk() (*bool, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *OpenaiChatCompletionRequest) SetLogprobs(v bool)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *OpenaiChatCompletionRequest) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.

### GetMaxCompletionTokens

`func (o *OpenaiChatCompletionRequest) GetMaxCompletionTokens() int32`

GetMaxCompletionTokens returns the MaxCompletionTokens field if non-nil, zero value otherwise.

### GetMaxCompletionTokensOk

`func (o *OpenaiChatCompletionRequest) GetMaxCompletionTokensOk() (*int32, bool)`

GetMaxCompletionTokensOk returns a tuple with the MaxCompletionTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxCompletionTokens

`func (o *OpenaiChatCompletionRequest) SetMaxCompletionTokens(v int32)`

SetMaxCompletionTokens sets MaxCompletionTokens field to given value.

### HasMaxCompletionTokens

`func (o *OpenaiChatCompletionRequest) HasMaxCompletionTokens() bool`

HasMaxCompletionTokens returns a boolean if a field has been set.

### GetMaxTokens

`func (o *OpenaiChatCompletionRequest) GetMaxTokens() int32`

GetMaxTokens returns the MaxTokens field if non-nil, zero value otherwise.

### GetMaxTokensOk

`func (o *OpenaiChatCompletionRequest) GetMaxTokensOk() (*int32, bool)`

GetMaxTokensOk returns a tuple with the MaxTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxTokens

`func (o *OpenaiChatCompletionRequest) SetMaxTokens(v int32)`

SetMaxTokens sets MaxTokens field to given value.

### HasMaxTokens

`func (o *OpenaiChatCompletionRequest) HasMaxTokens() bool`

HasMaxTokens returns a boolean if a field has been set.

### GetN

`func (o *OpenaiChatCompletionRequest) GetN() int32`

GetN returns the N field if non-nil, zero value otherwise.

### GetNOk

`func (o *OpenaiChatCompletionRequest) GetNOk() (*int32, bool)`

GetNOk returns a tuple with the N field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetN

`func (o *OpenaiChatCompletionRequest) SetN(v int32)`

SetN sets N field to given value.

### HasN

`func (o *OpenaiChatCompletionRequest) HasN() bool`

HasN returns a boolean if a field has been set.

### GetParallelToolCalls

`func (o *OpenaiChatCompletionRequest) GetParallelToolCalls() bool`

GetParallelToolCalls returns the ParallelToolCalls field if non-nil, zero value otherwise.

### GetParallelToolCallsOk

`func (o *OpenaiChatCompletionRequest) GetParallelToolCallsOk() (*bool, bool)`

GetParallelToolCallsOk returns a tuple with the ParallelToolCalls field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParallelToolCalls

`func (o *OpenaiChatCompletionRequest) SetParallelToolCalls(v bool)`

SetParallelToolCalls sets ParallelToolCalls field to given value.

### HasParallelToolCalls

`func (o *OpenaiChatCompletionRequest) HasParallelToolCalls() bool`

HasParallelToolCalls returns a boolean if a field has been set.

### GetPresencePenalty

`func (o *OpenaiChatCompletionRequest) GetPresencePenalty() float32`

GetPresencePenalty returns the PresencePenalty field if non-nil, zero value otherwise.

### GetPresencePenaltyOk

`func (o *OpenaiChatCompletionRequest) GetPresencePenaltyOk() (*float32, bool)`

GetPresencePenaltyOk returns a tuple with the PresencePenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPresencePenalty

`func (o *OpenaiChatCompletionRequest) SetPresencePenalty(v float32)`

SetPresencePenalty sets PresencePenalty field to given value.

### HasPresencePenalty

`func (o *OpenaiChatCompletionRequest) HasPresencePenalty() bool`

HasPresencePenalty returns a boolean if a field has been set.

### GetResponseFormat

`func (o *OpenaiChatCompletionRequest) GetResponseFormat() OpenAIResponseFormatParam`

GetResponseFormat returns the ResponseFormat field if non-nil, zero value otherwise.

### GetResponseFormatOk

`func (o *OpenaiChatCompletionRequest) GetResponseFormatOk() (*OpenAIResponseFormatParam, bool)`

GetResponseFormatOk returns a tuple with the ResponseFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseFormat

`func (o *OpenaiChatCompletionRequest) SetResponseFormat(v OpenAIResponseFormatParam)`

SetResponseFormat sets ResponseFormat field to given value.

### HasResponseFormat

`func (o *OpenaiChatCompletionRequest) HasResponseFormat() bool`

HasResponseFormat returns a boolean if a field has been set.

### GetSeed

`func (o *OpenaiChatCompletionRequest) GetSeed() int32`

GetSeed returns the Seed field if non-nil, zero value otherwise.

### GetSeedOk

`func (o *OpenaiChatCompletionRequest) GetSeedOk() (*int32, bool)`

GetSeedOk returns a tuple with the Seed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeed

`func (o *OpenaiChatCompletionRequest) SetSeed(v int32)`

SetSeed sets Seed field to given value.

### HasSeed

`func (o *OpenaiChatCompletionRequest) HasSeed() bool`

HasSeed returns a boolean if a field has been set.

### GetStop

`func (o *OpenaiChatCompletionRequest) GetStop() OpenaiChatCompletionRequestStop`

GetStop returns the Stop field if non-nil, zero value otherwise.

### GetStopOk

`func (o *OpenaiChatCompletionRequest) GetStopOk() (*OpenaiChatCompletionRequestStop, bool)`

GetStopOk returns a tuple with the Stop field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStop

`func (o *OpenaiChatCompletionRequest) SetStop(v OpenaiChatCompletionRequestStop)`

SetStop sets Stop field to given value.

### HasStop

`func (o *OpenaiChatCompletionRequest) HasStop() bool`

HasStop returns a boolean if a field has been set.

### GetStream

`func (o *OpenaiChatCompletionRequest) GetStream() bool`

GetStream returns the Stream field if non-nil, zero value otherwise.

### GetStreamOk

`func (o *OpenaiChatCompletionRequest) GetStreamOk() (*bool, bool)`

GetStreamOk returns a tuple with the Stream field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStream

`func (o *OpenaiChatCompletionRequest) SetStream(v bool)`

SetStream sets Stream field to given value.

### HasStream

`func (o *OpenaiChatCompletionRequest) HasStream() bool`

HasStream returns a boolean if a field has been set.

### GetStreamOptions

`func (o *OpenaiChatCompletionRequest) GetStreamOptions() map[string]AppendRowsRequestRowsInnerValue`

GetStreamOptions returns the StreamOptions field if non-nil, zero value otherwise.

### GetStreamOptionsOk

`func (o *OpenaiChatCompletionRequest) GetStreamOptionsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetStreamOptionsOk returns a tuple with the StreamOptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamOptions

`func (o *OpenaiChatCompletionRequest) SetStreamOptions(v map[string]AppendRowsRequestRowsInnerValue)`

SetStreamOptions sets StreamOptions field to given value.

### HasStreamOptions

`func (o *OpenaiChatCompletionRequest) HasStreamOptions() bool`

HasStreamOptions returns a boolean if a field has been set.

### GetTemperature

`func (o *OpenaiChatCompletionRequest) GetTemperature() float32`

GetTemperature returns the Temperature field if non-nil, zero value otherwise.

### GetTemperatureOk

`func (o *OpenaiChatCompletionRequest) GetTemperatureOk() (*float32, bool)`

GetTemperatureOk returns a tuple with the Temperature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTemperature

`func (o *OpenaiChatCompletionRequest) SetTemperature(v float32)`

SetTemperature sets Temperature field to given value.

### HasTemperature

`func (o *OpenaiChatCompletionRequest) HasTemperature() bool`

HasTemperature returns a boolean if a field has been set.

### GetToolChoice

`func (o *OpenaiChatCompletionRequest) GetToolChoice() OpenaiChatCompletionRequestToolChoice`

GetToolChoice returns the ToolChoice field if non-nil, zero value otherwise.

### GetToolChoiceOk

`func (o *OpenaiChatCompletionRequest) GetToolChoiceOk() (*OpenaiChatCompletionRequestToolChoice, bool)`

GetToolChoiceOk returns a tuple with the ToolChoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolChoice

`func (o *OpenaiChatCompletionRequest) SetToolChoice(v OpenaiChatCompletionRequestToolChoice)`

SetToolChoice sets ToolChoice field to given value.

### HasToolChoice

`func (o *OpenaiChatCompletionRequest) HasToolChoice() bool`

HasToolChoice returns a boolean if a field has been set.

### GetTools

`func (o *OpenaiChatCompletionRequest) GetTools() []map[string]AppendRowsRequestRowsInnerValue`

GetTools returns the Tools field if non-nil, zero value otherwise.

### GetToolsOk

`func (o *OpenaiChatCompletionRequest) GetToolsOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetToolsOk returns a tuple with the Tools field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTools

`func (o *OpenaiChatCompletionRequest) SetTools(v []map[string]AppendRowsRequestRowsInnerValue)`

SetTools sets Tools field to given value.

### HasTools

`func (o *OpenaiChatCompletionRequest) HasTools() bool`

HasTools returns a boolean if a field has been set.

### GetTopLogprobs

`func (o *OpenaiChatCompletionRequest) GetTopLogprobs() int32`

GetTopLogprobs returns the TopLogprobs field if non-nil, zero value otherwise.

### GetTopLogprobsOk

`func (o *OpenaiChatCompletionRequest) GetTopLogprobsOk() (*int32, bool)`

GetTopLogprobsOk returns a tuple with the TopLogprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopLogprobs

`func (o *OpenaiChatCompletionRequest) SetTopLogprobs(v int32)`

SetTopLogprobs sets TopLogprobs field to given value.

### HasTopLogprobs

`func (o *OpenaiChatCompletionRequest) HasTopLogprobs() bool`

HasTopLogprobs returns a boolean if a field has been set.

### GetTopP

`func (o *OpenaiChatCompletionRequest) GetTopP() float32`

GetTopP returns the TopP field if non-nil, zero value otherwise.

### GetTopPOk

`func (o *OpenaiChatCompletionRequest) GetTopPOk() (*float32, bool)`

GetTopPOk returns a tuple with the TopP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopP

`func (o *OpenaiChatCompletionRequest) SetTopP(v float32)`

SetTopP sets TopP field to given value.

### HasTopP

`func (o *OpenaiChatCompletionRequest) HasTopP() bool`

HasTopP returns a boolean if a field has been set.

### GetUser

`func (o *OpenaiChatCompletionRequest) GetUser() string`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *OpenaiChatCompletionRequest) GetUserOk() (*string, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *OpenaiChatCompletionRequest) SetUser(v string)`

SetUser sets User field to given value.

### HasUser

`func (o *OpenaiChatCompletionRequest) HasUser() bool`

HasUser returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


