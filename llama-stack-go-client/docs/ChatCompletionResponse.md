# ChatCompletionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Metrics** | Pointer to [**[]MetricInResponse**](MetricInResponse.md) |  | [optional] 
**CompletionMessage** | [**CompletionMessage**](CompletionMessage.md) | The complete response message | 
**Logprobs** | Pointer to [**[]TokenLogProbs**](TokenLogProbs.md) | Optional log probabilities for generated tokens | [optional] 

## Methods

### NewChatCompletionResponse

`func NewChatCompletionResponse(completionMessage CompletionMessage, ) *ChatCompletionResponse`

NewChatCompletionResponse instantiates a new ChatCompletionResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChatCompletionResponseWithDefaults

`func NewChatCompletionResponseWithDefaults() *ChatCompletionResponse`

NewChatCompletionResponseWithDefaults instantiates a new ChatCompletionResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMetrics

`func (o *ChatCompletionResponse) GetMetrics() []MetricInResponse`

GetMetrics returns the Metrics field if non-nil, zero value otherwise.

### GetMetricsOk

`func (o *ChatCompletionResponse) GetMetricsOk() (*[]MetricInResponse, bool)`

GetMetricsOk returns a tuple with the Metrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetrics

`func (o *ChatCompletionResponse) SetMetrics(v []MetricInResponse)`

SetMetrics sets Metrics field to given value.

### HasMetrics

`func (o *ChatCompletionResponse) HasMetrics() bool`

HasMetrics returns a boolean if a field has been set.

### GetCompletionMessage

`func (o *ChatCompletionResponse) GetCompletionMessage() CompletionMessage`

GetCompletionMessage returns the CompletionMessage field if non-nil, zero value otherwise.

### GetCompletionMessageOk

`func (o *ChatCompletionResponse) GetCompletionMessageOk() (*CompletionMessage, bool)`

GetCompletionMessageOk returns a tuple with the CompletionMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletionMessage

`func (o *ChatCompletionResponse) SetCompletionMessage(v CompletionMessage)`

SetCompletionMessage sets CompletionMessage field to given value.


### GetLogprobs

`func (o *ChatCompletionResponse) GetLogprobs() []TokenLogProbs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *ChatCompletionResponse) GetLogprobsOk() (*[]TokenLogProbs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *ChatCompletionResponse) SetLogprobs(v []TokenLogProbs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *ChatCompletionResponse) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


