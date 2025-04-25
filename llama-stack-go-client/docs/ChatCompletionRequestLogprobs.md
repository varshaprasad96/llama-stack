# ChatCompletionRequestLogprobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TopK** | Pointer to **int32** | How many tokens (for each position) to return log probabilities for. | [optional] [default to 0]

## Methods

### NewChatCompletionRequestLogprobs

`func NewChatCompletionRequestLogprobs() *ChatCompletionRequestLogprobs`

NewChatCompletionRequestLogprobs instantiates a new ChatCompletionRequestLogprobs object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChatCompletionRequestLogprobsWithDefaults

`func NewChatCompletionRequestLogprobsWithDefaults() *ChatCompletionRequestLogprobs`

NewChatCompletionRequestLogprobsWithDefaults instantiates a new ChatCompletionRequestLogprobs object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTopK

`func (o *ChatCompletionRequestLogprobs) GetTopK() int32`

GetTopK returns the TopK field if non-nil, zero value otherwise.

### GetTopKOk

`func (o *ChatCompletionRequestLogprobs) GetTopKOk() (*int32, bool)`

GetTopKOk returns a tuple with the TopK field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopK

`func (o *ChatCompletionRequestLogprobs) SetTopK(v int32)`

SetTopK sets TopK field to given value.

### HasTopK

`func (o *ChatCompletionRequestLogprobs) HasTopK() bool`

HasTopK returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


