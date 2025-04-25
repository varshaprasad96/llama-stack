# OpenAIChatCompletion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | The ID of the chat completion | 
**Choices** | [**[]OpenAIChoice**](OpenAIChoice.md) | List of choices | 
**Object** | **string** | The object type, which will be \&quot;chat.completion\&quot; | [default to "chat.completion"]
**Created** | **int32** | The Unix timestamp in seconds when the chat completion was created | 
**Model** | **string** | The model that was used to generate the chat completion | 

## Methods

### NewOpenAIChatCompletion

`func NewOpenAIChatCompletion(id string, choices []OpenAIChoice, object string, created int32, model string, ) *OpenAIChatCompletion`

NewOpenAIChatCompletion instantiates a new OpenAIChatCompletion object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIChatCompletionWithDefaults

`func NewOpenAIChatCompletionWithDefaults() *OpenAIChatCompletion`

NewOpenAIChatCompletionWithDefaults instantiates a new OpenAIChatCompletion object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *OpenAIChatCompletion) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *OpenAIChatCompletion) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *OpenAIChatCompletion) SetId(v string)`

SetId sets Id field to given value.


### GetChoices

`func (o *OpenAIChatCompletion) GetChoices() []OpenAIChoice`

GetChoices returns the Choices field if non-nil, zero value otherwise.

### GetChoicesOk

`func (o *OpenAIChatCompletion) GetChoicesOk() (*[]OpenAIChoice, bool)`

GetChoicesOk returns a tuple with the Choices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChoices

`func (o *OpenAIChatCompletion) SetChoices(v []OpenAIChoice)`

SetChoices sets Choices field to given value.


### GetObject

`func (o *OpenAIChatCompletion) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *OpenAIChatCompletion) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *OpenAIChatCompletion) SetObject(v string)`

SetObject sets Object field to given value.


### GetCreated

`func (o *OpenAIChatCompletion) GetCreated() int32`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *OpenAIChatCompletion) GetCreatedOk() (*int32, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *OpenAIChatCompletion) SetCreated(v int32)`

SetCreated sets Created field to given value.


### GetModel

`func (o *OpenAIChatCompletion) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *OpenAIChatCompletion) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *OpenAIChatCompletion) SetModel(v string)`

SetModel sets Model field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


