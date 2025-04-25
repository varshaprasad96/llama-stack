# OpenAIChunkChoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Delta** | [**OpenAIChoiceDelta**](OpenAIChoiceDelta.md) | The delta from the chunk | 
**FinishReason** | **string** | The reason the model stopped generating | 
**Index** | **int32** | The index of the choice | 
**Logprobs** | Pointer to [**OpenAIChoiceLogprobs**](OpenAIChoiceLogprobs.md) | (Optional) The log probabilities for the tokens in the message | [optional] 

## Methods

### NewOpenAIChunkChoice

`func NewOpenAIChunkChoice(delta OpenAIChoiceDelta, finishReason string, index int32, ) *OpenAIChunkChoice`

NewOpenAIChunkChoice instantiates a new OpenAIChunkChoice object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIChunkChoiceWithDefaults

`func NewOpenAIChunkChoiceWithDefaults() *OpenAIChunkChoice`

NewOpenAIChunkChoiceWithDefaults instantiates a new OpenAIChunkChoice object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDelta

`func (o *OpenAIChunkChoice) GetDelta() OpenAIChoiceDelta`

GetDelta returns the Delta field if non-nil, zero value otherwise.

### GetDeltaOk

`func (o *OpenAIChunkChoice) GetDeltaOk() (*OpenAIChoiceDelta, bool)`

GetDeltaOk returns a tuple with the Delta field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDelta

`func (o *OpenAIChunkChoice) SetDelta(v OpenAIChoiceDelta)`

SetDelta sets Delta field to given value.


### GetFinishReason

`func (o *OpenAIChunkChoice) GetFinishReason() string`

GetFinishReason returns the FinishReason field if non-nil, zero value otherwise.

### GetFinishReasonOk

`func (o *OpenAIChunkChoice) GetFinishReasonOk() (*string, bool)`

GetFinishReasonOk returns a tuple with the FinishReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishReason

`func (o *OpenAIChunkChoice) SetFinishReason(v string)`

SetFinishReason sets FinishReason field to given value.


### GetIndex

`func (o *OpenAIChunkChoice) GetIndex() int32`

GetIndex returns the Index field if non-nil, zero value otherwise.

### GetIndexOk

`func (o *OpenAIChunkChoice) GetIndexOk() (*int32, bool)`

GetIndexOk returns a tuple with the Index field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndex

`func (o *OpenAIChunkChoice) SetIndex(v int32)`

SetIndex sets Index field to given value.


### GetLogprobs

`func (o *OpenAIChunkChoice) GetLogprobs() OpenAIChoiceLogprobs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *OpenAIChunkChoice) GetLogprobsOk() (*OpenAIChoiceLogprobs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *OpenAIChunkChoice) SetLogprobs(v OpenAIChoiceLogprobs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *OpenAIChunkChoice) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


