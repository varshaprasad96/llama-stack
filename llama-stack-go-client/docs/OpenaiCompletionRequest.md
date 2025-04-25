# OpenaiCompletionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Model** | **string** | The identifier of the model to use. The model must be registered with Llama Stack and available via the /models endpoint. | 
**Prompt** | [**OpenaiCompletionRequestPrompt**](OpenaiCompletionRequestPrompt.md) |  | 
**BestOf** | Pointer to **int32** | (Optional) The number of completions to generate | [optional] 
**Echo** | Pointer to **bool** | (Optional) Whether to echo the prompt | [optional] 
**FrequencyPenalty** | Pointer to **float32** | (Optional) The penalty for repeated tokens | [optional] 
**LogitBias** | Pointer to **map[string]float32** | (Optional) The logit bias to use | [optional] 
**Logprobs** | Pointer to **bool** | (Optional) The log probabilities to use | [optional] 
**MaxTokens** | Pointer to **int32** | (Optional) The maximum number of tokens to generate | [optional] 
**N** | Pointer to **int32** | (Optional) The number of completions to generate | [optional] 
**PresencePenalty** | Pointer to **float32** | (Optional) The penalty for repeated tokens | [optional] 
**Seed** | Pointer to **int32** | (Optional) The seed to use | [optional] 
**Stop** | Pointer to [**OpenaiChatCompletionRequestStop**](OpenaiChatCompletionRequestStop.md) |  | [optional] 
**Stream** | Pointer to **bool** | (Optional) Whether to stream the response | [optional] 
**StreamOptions** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | (Optional) The stream options to use | [optional] 
**Temperature** | Pointer to **float32** | (Optional) The temperature to use | [optional] 
**TopP** | Pointer to **float32** | (Optional) The top p to use | [optional] 
**User** | Pointer to **string** | (Optional) The user to use | [optional] 
**GuidedChoice** | Pointer to **[]string** |  | [optional] 
**PromptLogprobs** | Pointer to **int32** |  | [optional] 

## Methods

### NewOpenaiCompletionRequest

`func NewOpenaiCompletionRequest(model string, prompt OpenaiCompletionRequestPrompt, ) *OpenaiCompletionRequest`

NewOpenaiCompletionRequest instantiates a new OpenaiCompletionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenaiCompletionRequestWithDefaults

`func NewOpenaiCompletionRequestWithDefaults() *OpenaiCompletionRequest`

NewOpenaiCompletionRequestWithDefaults instantiates a new OpenaiCompletionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModel

`func (o *OpenaiCompletionRequest) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *OpenaiCompletionRequest) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *OpenaiCompletionRequest) SetModel(v string)`

SetModel sets Model field to given value.


### GetPrompt

`func (o *OpenaiCompletionRequest) GetPrompt() OpenaiCompletionRequestPrompt`

GetPrompt returns the Prompt field if non-nil, zero value otherwise.

### GetPromptOk

`func (o *OpenaiCompletionRequest) GetPromptOk() (*OpenaiCompletionRequestPrompt, bool)`

GetPromptOk returns a tuple with the Prompt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrompt

`func (o *OpenaiCompletionRequest) SetPrompt(v OpenaiCompletionRequestPrompt)`

SetPrompt sets Prompt field to given value.


### GetBestOf

`func (o *OpenaiCompletionRequest) GetBestOf() int32`

GetBestOf returns the BestOf field if non-nil, zero value otherwise.

### GetBestOfOk

`func (o *OpenaiCompletionRequest) GetBestOfOk() (*int32, bool)`

GetBestOfOk returns a tuple with the BestOf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBestOf

`func (o *OpenaiCompletionRequest) SetBestOf(v int32)`

SetBestOf sets BestOf field to given value.

### HasBestOf

`func (o *OpenaiCompletionRequest) HasBestOf() bool`

HasBestOf returns a boolean if a field has been set.

### GetEcho

`func (o *OpenaiCompletionRequest) GetEcho() bool`

GetEcho returns the Echo field if non-nil, zero value otherwise.

### GetEchoOk

`func (o *OpenaiCompletionRequest) GetEchoOk() (*bool, bool)`

GetEchoOk returns a tuple with the Echo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEcho

`func (o *OpenaiCompletionRequest) SetEcho(v bool)`

SetEcho sets Echo field to given value.

### HasEcho

`func (o *OpenaiCompletionRequest) HasEcho() bool`

HasEcho returns a boolean if a field has been set.

### GetFrequencyPenalty

`func (o *OpenaiCompletionRequest) GetFrequencyPenalty() float32`

GetFrequencyPenalty returns the FrequencyPenalty field if non-nil, zero value otherwise.

### GetFrequencyPenaltyOk

`func (o *OpenaiCompletionRequest) GetFrequencyPenaltyOk() (*float32, bool)`

GetFrequencyPenaltyOk returns a tuple with the FrequencyPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFrequencyPenalty

`func (o *OpenaiCompletionRequest) SetFrequencyPenalty(v float32)`

SetFrequencyPenalty sets FrequencyPenalty field to given value.

### HasFrequencyPenalty

`func (o *OpenaiCompletionRequest) HasFrequencyPenalty() bool`

HasFrequencyPenalty returns a boolean if a field has been set.

### GetLogitBias

`func (o *OpenaiCompletionRequest) GetLogitBias() map[string]float32`

GetLogitBias returns the LogitBias field if non-nil, zero value otherwise.

### GetLogitBiasOk

`func (o *OpenaiCompletionRequest) GetLogitBiasOk() (*map[string]float32, bool)`

GetLogitBiasOk returns a tuple with the LogitBias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogitBias

`func (o *OpenaiCompletionRequest) SetLogitBias(v map[string]float32)`

SetLogitBias sets LogitBias field to given value.

### HasLogitBias

`func (o *OpenaiCompletionRequest) HasLogitBias() bool`

HasLogitBias returns a boolean if a field has been set.

### GetLogprobs

`func (o *OpenaiCompletionRequest) GetLogprobs() bool`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *OpenaiCompletionRequest) GetLogprobsOk() (*bool, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *OpenaiCompletionRequest) SetLogprobs(v bool)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *OpenaiCompletionRequest) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.

### GetMaxTokens

`func (o *OpenaiCompletionRequest) GetMaxTokens() int32`

GetMaxTokens returns the MaxTokens field if non-nil, zero value otherwise.

### GetMaxTokensOk

`func (o *OpenaiCompletionRequest) GetMaxTokensOk() (*int32, bool)`

GetMaxTokensOk returns a tuple with the MaxTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxTokens

`func (o *OpenaiCompletionRequest) SetMaxTokens(v int32)`

SetMaxTokens sets MaxTokens field to given value.

### HasMaxTokens

`func (o *OpenaiCompletionRequest) HasMaxTokens() bool`

HasMaxTokens returns a boolean if a field has been set.

### GetN

`func (o *OpenaiCompletionRequest) GetN() int32`

GetN returns the N field if non-nil, zero value otherwise.

### GetNOk

`func (o *OpenaiCompletionRequest) GetNOk() (*int32, bool)`

GetNOk returns a tuple with the N field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetN

`func (o *OpenaiCompletionRequest) SetN(v int32)`

SetN sets N field to given value.

### HasN

`func (o *OpenaiCompletionRequest) HasN() bool`

HasN returns a boolean if a field has been set.

### GetPresencePenalty

`func (o *OpenaiCompletionRequest) GetPresencePenalty() float32`

GetPresencePenalty returns the PresencePenalty field if non-nil, zero value otherwise.

### GetPresencePenaltyOk

`func (o *OpenaiCompletionRequest) GetPresencePenaltyOk() (*float32, bool)`

GetPresencePenaltyOk returns a tuple with the PresencePenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPresencePenalty

`func (o *OpenaiCompletionRequest) SetPresencePenalty(v float32)`

SetPresencePenalty sets PresencePenalty field to given value.

### HasPresencePenalty

`func (o *OpenaiCompletionRequest) HasPresencePenalty() bool`

HasPresencePenalty returns a boolean if a field has been set.

### GetSeed

`func (o *OpenaiCompletionRequest) GetSeed() int32`

GetSeed returns the Seed field if non-nil, zero value otherwise.

### GetSeedOk

`func (o *OpenaiCompletionRequest) GetSeedOk() (*int32, bool)`

GetSeedOk returns a tuple with the Seed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeed

`func (o *OpenaiCompletionRequest) SetSeed(v int32)`

SetSeed sets Seed field to given value.

### HasSeed

`func (o *OpenaiCompletionRequest) HasSeed() bool`

HasSeed returns a boolean if a field has been set.

### GetStop

`func (o *OpenaiCompletionRequest) GetStop() OpenaiChatCompletionRequestStop`

GetStop returns the Stop field if non-nil, zero value otherwise.

### GetStopOk

`func (o *OpenaiCompletionRequest) GetStopOk() (*OpenaiChatCompletionRequestStop, bool)`

GetStopOk returns a tuple with the Stop field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStop

`func (o *OpenaiCompletionRequest) SetStop(v OpenaiChatCompletionRequestStop)`

SetStop sets Stop field to given value.

### HasStop

`func (o *OpenaiCompletionRequest) HasStop() bool`

HasStop returns a boolean if a field has been set.

### GetStream

`func (o *OpenaiCompletionRequest) GetStream() bool`

GetStream returns the Stream field if non-nil, zero value otherwise.

### GetStreamOk

`func (o *OpenaiCompletionRequest) GetStreamOk() (*bool, bool)`

GetStreamOk returns a tuple with the Stream field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStream

`func (o *OpenaiCompletionRequest) SetStream(v bool)`

SetStream sets Stream field to given value.

### HasStream

`func (o *OpenaiCompletionRequest) HasStream() bool`

HasStream returns a boolean if a field has been set.

### GetStreamOptions

`func (o *OpenaiCompletionRequest) GetStreamOptions() map[string]AppendRowsRequestRowsInnerValue`

GetStreamOptions returns the StreamOptions field if non-nil, zero value otherwise.

### GetStreamOptionsOk

`func (o *OpenaiCompletionRequest) GetStreamOptionsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetStreamOptionsOk returns a tuple with the StreamOptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreamOptions

`func (o *OpenaiCompletionRequest) SetStreamOptions(v map[string]AppendRowsRequestRowsInnerValue)`

SetStreamOptions sets StreamOptions field to given value.

### HasStreamOptions

`func (o *OpenaiCompletionRequest) HasStreamOptions() bool`

HasStreamOptions returns a boolean if a field has been set.

### GetTemperature

`func (o *OpenaiCompletionRequest) GetTemperature() float32`

GetTemperature returns the Temperature field if non-nil, zero value otherwise.

### GetTemperatureOk

`func (o *OpenaiCompletionRequest) GetTemperatureOk() (*float32, bool)`

GetTemperatureOk returns a tuple with the Temperature field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTemperature

`func (o *OpenaiCompletionRequest) SetTemperature(v float32)`

SetTemperature sets Temperature field to given value.

### HasTemperature

`func (o *OpenaiCompletionRequest) HasTemperature() bool`

HasTemperature returns a boolean if a field has been set.

### GetTopP

`func (o *OpenaiCompletionRequest) GetTopP() float32`

GetTopP returns the TopP field if non-nil, zero value otherwise.

### GetTopPOk

`func (o *OpenaiCompletionRequest) GetTopPOk() (*float32, bool)`

GetTopPOk returns a tuple with the TopP field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopP

`func (o *OpenaiCompletionRequest) SetTopP(v float32)`

SetTopP sets TopP field to given value.

### HasTopP

`func (o *OpenaiCompletionRequest) HasTopP() bool`

HasTopP returns a boolean if a field has been set.

### GetUser

`func (o *OpenaiCompletionRequest) GetUser() string`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *OpenaiCompletionRequest) GetUserOk() (*string, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *OpenaiCompletionRequest) SetUser(v string)`

SetUser sets User field to given value.

### HasUser

`func (o *OpenaiCompletionRequest) HasUser() bool`

HasUser returns a boolean if a field has been set.

### GetGuidedChoice

`func (o *OpenaiCompletionRequest) GetGuidedChoice() []string`

GetGuidedChoice returns the GuidedChoice field if non-nil, zero value otherwise.

### GetGuidedChoiceOk

`func (o *OpenaiCompletionRequest) GetGuidedChoiceOk() (*[]string, bool)`

GetGuidedChoiceOk returns a tuple with the GuidedChoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGuidedChoice

`func (o *OpenaiCompletionRequest) SetGuidedChoice(v []string)`

SetGuidedChoice sets GuidedChoice field to given value.

### HasGuidedChoice

`func (o *OpenaiCompletionRequest) HasGuidedChoice() bool`

HasGuidedChoice returns a boolean if a field has been set.

### GetPromptLogprobs

`func (o *OpenaiCompletionRequest) GetPromptLogprobs() int32`

GetPromptLogprobs returns the PromptLogprobs field if non-nil, zero value otherwise.

### GetPromptLogprobsOk

`func (o *OpenaiCompletionRequest) GetPromptLogprobsOk() (*int32, bool)`

GetPromptLogprobsOk returns a tuple with the PromptLogprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromptLogprobs

`func (o *OpenaiCompletionRequest) SetPromptLogprobs(v int32)`

SetPromptLogprobs sets PromptLogprobs field to given value.

### HasPromptLogprobs

`func (o *OpenaiCompletionRequest) HasPromptLogprobs() bool`

HasPromptLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


