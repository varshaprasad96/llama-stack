# SamplingParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Strategy** | [**SamplingStrategy**](SamplingStrategy.md) | The sampling strategy. | 
**MaxTokens** | Pointer to **int32** | The maximum number of tokens that can be generated in the completion. The token count of your prompt plus max_tokens cannot exceed the model&#39;s context length. | [optional] [default to 0]
**RepetitionPenalty** | Pointer to **float32** | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model&#39;s likelihood to talk about new topics. | [optional] [default to 1.0]
**Stop** | Pointer to **[]string** | Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence. | [optional] 

## Methods

### NewSamplingParams

`func NewSamplingParams(strategy SamplingStrategy, ) *SamplingParams`

NewSamplingParams instantiates a new SamplingParams object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSamplingParamsWithDefaults

`func NewSamplingParamsWithDefaults() *SamplingParams`

NewSamplingParamsWithDefaults instantiates a new SamplingParams object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStrategy

`func (o *SamplingParams) GetStrategy() SamplingStrategy`

GetStrategy returns the Strategy field if non-nil, zero value otherwise.

### GetStrategyOk

`func (o *SamplingParams) GetStrategyOk() (*SamplingStrategy, bool)`

GetStrategyOk returns a tuple with the Strategy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStrategy

`func (o *SamplingParams) SetStrategy(v SamplingStrategy)`

SetStrategy sets Strategy field to given value.


### GetMaxTokens

`func (o *SamplingParams) GetMaxTokens() int32`

GetMaxTokens returns the MaxTokens field if non-nil, zero value otherwise.

### GetMaxTokensOk

`func (o *SamplingParams) GetMaxTokensOk() (*int32, bool)`

GetMaxTokensOk returns a tuple with the MaxTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxTokens

`func (o *SamplingParams) SetMaxTokens(v int32)`

SetMaxTokens sets MaxTokens field to given value.

### HasMaxTokens

`func (o *SamplingParams) HasMaxTokens() bool`

HasMaxTokens returns a boolean if a field has been set.

### GetRepetitionPenalty

`func (o *SamplingParams) GetRepetitionPenalty() float32`

GetRepetitionPenalty returns the RepetitionPenalty field if non-nil, zero value otherwise.

### GetRepetitionPenaltyOk

`func (o *SamplingParams) GetRepetitionPenaltyOk() (*float32, bool)`

GetRepetitionPenaltyOk returns a tuple with the RepetitionPenalty field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRepetitionPenalty

`func (o *SamplingParams) SetRepetitionPenalty(v float32)`

SetRepetitionPenalty sets RepetitionPenalty field to given value.

### HasRepetitionPenalty

`func (o *SamplingParams) HasRepetitionPenalty() bool`

HasRepetitionPenalty returns a boolean if a field has been set.

### GetStop

`func (o *SamplingParams) GetStop() []string`

GetStop returns the Stop field if non-nil, zero value otherwise.

### GetStopOk

`func (o *SamplingParams) GetStopOk() (*[]string, bool)`

GetStopOk returns a tuple with the Stop field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStop

`func (o *SamplingParams) SetStop(v []string)`

SetStop sets Stop field to given value.

### HasStop

`func (o *SamplingParams) HasStop() bool`

HasStop returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


