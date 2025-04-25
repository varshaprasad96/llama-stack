# V1OpenaiV1ChatCompletionsPost200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | The ID of the chat completion | 
**Choices** | [**[]OpenAIChunkChoice**](OpenAIChunkChoice.md) | List of choices | 
**Object** | **string** | The object type, which will be \&quot;chat.completion.chunk\&quot; | [default to "chat.completion.chunk"]
**Created** | **int32** | The Unix timestamp in seconds when the chat completion was created | 
**Model** | **string** | The model that was used to generate the chat completion | 

## Methods

### NewV1OpenaiV1ChatCompletionsPost200Response

`func NewV1OpenaiV1ChatCompletionsPost200Response(id string, choices []OpenAIChunkChoice, object string, created int32, model string, ) *V1OpenaiV1ChatCompletionsPost200Response`

NewV1OpenaiV1ChatCompletionsPost200Response instantiates a new V1OpenaiV1ChatCompletionsPost200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewV1OpenaiV1ChatCompletionsPost200ResponseWithDefaults

`func NewV1OpenaiV1ChatCompletionsPost200ResponseWithDefaults() *V1OpenaiV1ChatCompletionsPost200Response`

NewV1OpenaiV1ChatCompletionsPost200ResponseWithDefaults instantiates a new V1OpenaiV1ChatCompletionsPost200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *V1OpenaiV1ChatCompletionsPost200Response) SetId(v string)`

SetId sets Id field to given value.


### GetChoices

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetChoices() []OpenAIChunkChoice`

GetChoices returns the Choices field if non-nil, zero value otherwise.

### GetChoicesOk

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetChoicesOk() (*[]OpenAIChunkChoice, bool)`

GetChoicesOk returns a tuple with the Choices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChoices

`func (o *V1OpenaiV1ChatCompletionsPost200Response) SetChoices(v []OpenAIChunkChoice)`

SetChoices sets Choices field to given value.


### GetObject

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *V1OpenaiV1ChatCompletionsPost200Response) SetObject(v string)`

SetObject sets Object field to given value.


### GetCreated

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetCreated() int32`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetCreatedOk() (*int32, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *V1OpenaiV1ChatCompletionsPost200Response) SetCreated(v int32)`

SetCreated sets Created field to given value.


### GetModel

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *V1OpenaiV1ChatCompletionsPost200Response) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *V1OpenaiV1ChatCompletionsPost200Response) SetModel(v string)`

SetModel sets Model field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


