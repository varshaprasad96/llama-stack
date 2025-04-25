# OpenAIChoiceLogprobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | Pointer to [**[]OpenAITokenLogProb**](OpenAITokenLogProb.md) | (Optional) The log probabilities for the tokens in the message | [optional] 
**Refusal** | Pointer to [**[]OpenAITokenLogProb**](OpenAITokenLogProb.md) | (Optional) The log probabilities for the tokens in the message | [optional] 

## Methods

### NewOpenAIChoiceLogprobs

`func NewOpenAIChoiceLogprobs() *OpenAIChoiceLogprobs`

NewOpenAIChoiceLogprobs instantiates a new OpenAIChoiceLogprobs object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIChoiceLogprobsWithDefaults

`func NewOpenAIChoiceLogprobsWithDefaults() *OpenAIChoiceLogprobs`

NewOpenAIChoiceLogprobsWithDefaults instantiates a new OpenAIChoiceLogprobs object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *OpenAIChoiceLogprobs) GetContent() []OpenAITokenLogProb`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *OpenAIChoiceLogprobs) GetContentOk() (*[]OpenAITokenLogProb, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *OpenAIChoiceLogprobs) SetContent(v []OpenAITokenLogProb)`

SetContent sets Content field to given value.

### HasContent

`func (o *OpenAIChoiceLogprobs) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetRefusal

`func (o *OpenAIChoiceLogprobs) GetRefusal() []OpenAITokenLogProb`

GetRefusal returns the Refusal field if non-nil, zero value otherwise.

### GetRefusalOk

`func (o *OpenAIChoiceLogprobs) GetRefusalOk() (*[]OpenAITokenLogProb, bool)`

GetRefusalOk returns a tuple with the Refusal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefusal

`func (o *OpenAIChoiceLogprobs) SetRefusal(v []OpenAITokenLogProb)`

SetRefusal sets Refusal field to given value.

### HasRefusal

`func (o *OpenAIChoiceLogprobs) HasRefusal() bool`

HasRefusal returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


