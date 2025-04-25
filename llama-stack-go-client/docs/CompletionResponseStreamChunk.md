# CompletionResponseStreamChunk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Metrics** | Pointer to [**[]MetricInResponse**](MetricInResponse.md) |  | [optional] 
**Delta** | **string** | New content generated since last chunk. This can be one or more tokens. | 
**StopReason** | Pointer to **string** | Optional reason why generation stopped, if complete | [optional] 
**Logprobs** | Pointer to [**[]TokenLogProbs**](TokenLogProbs.md) | Optional log probabilities for generated tokens | [optional] 

## Methods

### NewCompletionResponseStreamChunk

`func NewCompletionResponseStreamChunk(delta string, ) *CompletionResponseStreamChunk`

NewCompletionResponseStreamChunk instantiates a new CompletionResponseStreamChunk object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompletionResponseStreamChunkWithDefaults

`func NewCompletionResponseStreamChunkWithDefaults() *CompletionResponseStreamChunk`

NewCompletionResponseStreamChunkWithDefaults instantiates a new CompletionResponseStreamChunk object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMetrics

`func (o *CompletionResponseStreamChunk) GetMetrics() []MetricInResponse`

GetMetrics returns the Metrics field if non-nil, zero value otherwise.

### GetMetricsOk

`func (o *CompletionResponseStreamChunk) GetMetricsOk() (*[]MetricInResponse, bool)`

GetMetricsOk returns a tuple with the Metrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetrics

`func (o *CompletionResponseStreamChunk) SetMetrics(v []MetricInResponse)`

SetMetrics sets Metrics field to given value.

### HasMetrics

`func (o *CompletionResponseStreamChunk) HasMetrics() bool`

HasMetrics returns a boolean if a field has been set.

### GetDelta

`func (o *CompletionResponseStreamChunk) GetDelta() string`

GetDelta returns the Delta field if non-nil, zero value otherwise.

### GetDeltaOk

`func (o *CompletionResponseStreamChunk) GetDeltaOk() (*string, bool)`

GetDeltaOk returns a tuple with the Delta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDelta

`func (o *CompletionResponseStreamChunk) SetDelta(v string)`

SetDelta sets Delta field to given value.


### GetStopReason

`func (o *CompletionResponseStreamChunk) GetStopReason() string`

GetStopReason returns the StopReason field if non-nil, zero value otherwise.

### GetStopReasonOk

`func (o *CompletionResponseStreamChunk) GetStopReasonOk() (*string, bool)`

GetStopReasonOk returns a tuple with the StopReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStopReason

`func (o *CompletionResponseStreamChunk) SetStopReason(v string)`

SetStopReason sets StopReason field to given value.

### HasStopReason

`func (o *CompletionResponseStreamChunk) HasStopReason() bool`

HasStopReason returns a boolean if a field has been set.

### GetLogprobs

`func (o *CompletionResponseStreamChunk) GetLogprobs() []TokenLogProbs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *CompletionResponseStreamChunk) GetLogprobsOk() (*[]TokenLogProbs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *CompletionResponseStreamChunk) SetLogprobs(v []TokenLogProbs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *CompletionResponseStreamChunk) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


