# OpenAIChoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Message** | [**OpenAIMessageParam**](OpenAIMessageParam.md) | The message from the model | 
**FinishReason** | **string** | The reason the model stopped generating | 
**Index** | **int32** | The index of the choice | 
**Logprobs** | Pointer to [**OpenAIChoiceLogprobs**](OpenAIChoiceLogprobs.md) | (Optional) The log probabilities for the tokens in the message | [optional] 

## Methods

### NewOpenAIChoice

`func NewOpenAIChoice(message OpenAIMessageParam, finishReason string, index int32, ) *OpenAIChoice`

NewOpenAIChoice instantiates a new OpenAIChoice object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIChoiceWithDefaults

`func NewOpenAIChoiceWithDefaults() *OpenAIChoice`

NewOpenAIChoiceWithDefaults instantiates a new OpenAIChoice object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMessage

`func (o *OpenAIChoice) GetMessage() OpenAIMessageParam`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *OpenAIChoice) GetMessageOk() (*OpenAIMessageParam, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *OpenAIChoice) SetMessage(v OpenAIMessageParam)`

SetMessage sets Message field to given value.


### GetFinishReason

`func (o *OpenAIChoice) GetFinishReason() string`

GetFinishReason returns the FinishReason field if non-nil, zero value otherwise.

### GetFinishReasonOk

`func (o *OpenAIChoice) GetFinishReasonOk() (*string, bool)`

GetFinishReasonOk returns a tuple with the FinishReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFinishReason

`func (o *OpenAIChoice) SetFinishReason(v string)`

SetFinishReason sets FinishReason field to given value.


### GetIndex

`func (o *OpenAIChoice) GetIndex() int32`

GetIndex returns the Index field if non-nil, zero value otherwise.

### GetIndexOk

`func (o *OpenAIChoice) GetIndexOk() (*int32, bool)`

GetIndexOk returns a tuple with the Index field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndex

`func (o *OpenAIChoice) SetIndex(v int32)`

SetIndex sets Index field to given value.


### GetLogprobs

`func (o *OpenAIChoice) GetLogprobs() OpenAIChoiceLogprobs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *OpenAIChoice) GetLogprobsOk() (*OpenAIChoiceLogprobs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *OpenAIChoice) SetLogprobs(v OpenAIChoiceLogprobs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *OpenAIChoice) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


