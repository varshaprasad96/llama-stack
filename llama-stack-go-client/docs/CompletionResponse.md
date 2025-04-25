# CompletionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Metrics** | Pointer to [**[]MetricInResponse**](MetricInResponse.md) |  | [optional] 
**Content** | **string** | The generated completion text | 
**StopReason** | **string** | Reason why generation stopped | 
**Logprobs** | Pointer to [**[]TokenLogProbs**](TokenLogProbs.md) | Optional log probabilities for generated tokens | [optional] 

## Methods

### NewCompletionResponse

`func NewCompletionResponse(content string, stopReason string, ) *CompletionResponse`

NewCompletionResponse instantiates a new CompletionResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompletionResponseWithDefaults

`func NewCompletionResponseWithDefaults() *CompletionResponse`

NewCompletionResponseWithDefaults instantiates a new CompletionResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMetrics

`func (o *CompletionResponse) GetMetrics() []MetricInResponse`

GetMetrics returns the Metrics field if non-nil, zero value otherwise.

### GetMetricsOk

`func (o *CompletionResponse) GetMetricsOk() (*[]MetricInResponse, bool)`

GetMetricsOk returns a tuple with the Metrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetrics

`func (o *CompletionResponse) SetMetrics(v []MetricInResponse)`

SetMetrics sets Metrics field to given value.

### HasMetrics

`func (o *CompletionResponse) HasMetrics() bool`

HasMetrics returns a boolean if a field has been set.

### GetContent

`func (o *CompletionResponse) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *CompletionResponse) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *CompletionResponse) SetContent(v string)`

SetContent sets Content field to given value.


### GetStopReason

`func (o *CompletionResponse) GetStopReason() string`

GetStopReason returns the StopReason field if non-nil, zero value otherwise.

### GetStopReasonOk

`func (o *CompletionResponse) GetStopReasonOk() (*string, bool)`

GetStopReasonOk returns a tuple with the StopReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStopReason

`func (o *CompletionResponse) SetStopReason(v string)`

SetStopReason sets StopReason field to given value.


### GetLogprobs

`func (o *CompletionResponse) GetLogprobs() []TokenLogProbs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *CompletionResponse) GetLogprobsOk() (*[]TokenLogProbs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *CompletionResponse) SetLogprobs(v []TokenLogProbs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *CompletionResponse) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


