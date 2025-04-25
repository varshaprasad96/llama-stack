# ChatCompletionResponseEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventType** | **string** | Type of the event | 
**Delta** | [**ContentDelta**](ContentDelta.md) | Content generated since last event. This can be one or more tokens, or a tool call. | 
**Logprobs** | Pointer to [**[]TokenLogProbs**](TokenLogProbs.md) | Optional log probabilities for generated tokens | [optional] 
**StopReason** | Pointer to **string** | Optional reason why generation stopped, if complete | [optional] 

## Methods

### NewChatCompletionResponseEvent

`func NewChatCompletionResponseEvent(eventType string, delta ContentDelta, ) *ChatCompletionResponseEvent`

NewChatCompletionResponseEvent instantiates a new ChatCompletionResponseEvent object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChatCompletionResponseEventWithDefaults

`func NewChatCompletionResponseEventWithDefaults() *ChatCompletionResponseEvent`

NewChatCompletionResponseEventWithDefaults instantiates a new ChatCompletionResponseEvent object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEventType

`func (o *ChatCompletionResponseEvent) GetEventType() string`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *ChatCompletionResponseEvent) GetEventTypeOk() (*string, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventType

`func (o *ChatCompletionResponseEvent) SetEventType(v string)`

SetEventType sets EventType field to given value.


### GetDelta

`func (o *ChatCompletionResponseEvent) GetDelta() ContentDelta`

GetDelta returns the Delta field if non-nil, zero value otherwise.

### GetDeltaOk

`func (o *ChatCompletionResponseEvent) GetDeltaOk() (*ContentDelta, bool)`

GetDeltaOk returns a tuple with the Delta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDelta

`func (o *ChatCompletionResponseEvent) SetDelta(v ContentDelta)`

SetDelta sets Delta field to given value.


### GetLogprobs

`func (o *ChatCompletionResponseEvent) GetLogprobs() []TokenLogProbs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *ChatCompletionResponseEvent) GetLogprobsOk() (*[]TokenLogProbs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *ChatCompletionResponseEvent) SetLogprobs(v []TokenLogProbs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *ChatCompletionResponseEvent) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.

### GetStopReason

`func (o *ChatCompletionResponseEvent) GetStopReason() string`

GetStopReason returns the StopReason field if non-nil, zero value otherwise.

### GetStopReasonOk

`func (o *ChatCompletionResponseEvent) GetStopReasonOk() (*string, bool)`

GetStopReasonOk returns a tuple with the StopReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStopReason

`func (o *ChatCompletionResponseEvent) SetStopReason(v string)`

SetStopReason sets StopReason field to given value.

### HasStopReason

`func (o *ChatCompletionResponseEvent) HasStopReason() bool`

HasStopReason returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


