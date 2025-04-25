# ChatCompletionResponseStreamChunk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Metrics** | Pointer to [**[]MetricInResponse**](MetricInResponse.md) |  | [optional] 
**Event** | [**ChatCompletionResponseEvent**](ChatCompletionResponseEvent.md) | The event containing the new content | 

## Methods

### NewChatCompletionResponseStreamChunk

`func NewChatCompletionResponseStreamChunk(event ChatCompletionResponseEvent, ) *ChatCompletionResponseStreamChunk`

NewChatCompletionResponseStreamChunk instantiates a new ChatCompletionResponseStreamChunk object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChatCompletionResponseStreamChunkWithDefaults

`func NewChatCompletionResponseStreamChunkWithDefaults() *ChatCompletionResponseStreamChunk`

NewChatCompletionResponseStreamChunkWithDefaults instantiates a new ChatCompletionResponseStreamChunk object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMetrics

`func (o *ChatCompletionResponseStreamChunk) GetMetrics() []MetricInResponse`

GetMetrics returns the Metrics field if non-nil, zero value otherwise.

### GetMetricsOk

`func (o *ChatCompletionResponseStreamChunk) GetMetricsOk() (*[]MetricInResponse, bool)`

GetMetricsOk returns a tuple with the Metrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetrics

`func (o *ChatCompletionResponseStreamChunk) SetMetrics(v []MetricInResponse)`

SetMetrics sets Metrics field to given value.

### HasMetrics

`func (o *ChatCompletionResponseStreamChunk) HasMetrics() bool`

HasMetrics returns a boolean if a field has been set.

### GetEvent

`func (o *ChatCompletionResponseStreamChunk) GetEvent() ChatCompletionResponseEvent`

GetEvent returns the Event field if non-nil, zero value otherwise.

### GetEventOk

`func (o *ChatCompletionResponseStreamChunk) GetEventOk() (*ChatCompletionResponseEvent, bool)`

GetEventOk returns a tuple with the Event field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvent

`func (o *ChatCompletionResponseStreamChunk) SetEvent(v ChatCompletionResponseEvent)`

SetEvent sets Event field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


