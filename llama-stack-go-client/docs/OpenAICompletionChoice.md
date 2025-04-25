# OpenAICompletionChoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FinishReason** | **string** |  | 
**Text** | **string** |  | 
**Index** | **int32** |  | 
**Logprobs** | Pointer to [**OpenAIChoiceLogprobs**](OpenAIChoiceLogprobs.md) |  | [optional] 

## Methods

### NewOpenAICompletionChoice

`func NewOpenAICompletionChoice(finishReason string, text string, index int32, ) *OpenAICompletionChoice`

NewOpenAICompletionChoice instantiates a new OpenAICompletionChoice object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAICompletionChoiceWithDefaults

`func NewOpenAICompletionChoiceWithDefaults() *OpenAICompletionChoice`

NewOpenAICompletionChoiceWithDefaults instantiates a new OpenAICompletionChoice object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFinishReason

`func (o *OpenAICompletionChoice) GetFinishReason() string`

GetFinishReason returns the FinishReason field if non-nil, zero value otherwise.

### GetFinishReasonOk

`func (o *OpenAICompletionChoice) GetFinishReasonOk() (*string, bool)`

GetFinishReasonOk returns a tuple with the FinishReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishReason

`func (o *OpenAICompletionChoice) SetFinishReason(v string)`

SetFinishReason sets FinishReason field to given value.


### GetText

`func (o *OpenAICompletionChoice) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *OpenAICompletionChoice) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *OpenAICompletionChoice) SetText(v string)`

SetText sets Text field to given value.


### GetIndex

`func (o *OpenAICompletionChoice) GetIndex() int32`

GetIndex returns the Index field if non-nil, zero value otherwise.

### GetIndexOk

`func (o *OpenAICompletionChoice) GetIndexOk() (*int32, bool)`

GetIndexOk returns a tuple with the Index field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndex

`func (o *OpenAICompletionChoice) SetIndex(v int32)`

SetIndex sets Index field to given value.


### GetLogprobs

`func (o *OpenAICompletionChoice) GetLogprobs() OpenAIChoiceLogprobs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *OpenAICompletionChoice) GetLogprobsOk() (*OpenAIChoiceLogprobs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *OpenAICompletionChoice) SetLogprobs(v OpenAIChoiceLogprobs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *OpenAICompletionChoice) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


