# OpenAIChatCompletionContentPartParam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "text"]
**Text** | **string** |  | 
**ImageUrl** | [**OpenAIImageURL**](OpenAIImageURL.md) |  | 

## Methods

### NewOpenAIChatCompletionContentPartParam

`func NewOpenAIChatCompletionContentPartParam(type_ string, text string, imageUrl OpenAIImageURL, ) *OpenAIChatCompletionContentPartParam`

NewOpenAIChatCompletionContentPartParam instantiates a new OpenAIChatCompletionContentPartParam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIChatCompletionContentPartParamWithDefaults

`func NewOpenAIChatCompletionContentPartParamWithDefaults() *OpenAIChatCompletionContentPartParam`

NewOpenAIChatCompletionContentPartParamWithDefaults instantiates a new OpenAIChatCompletionContentPartParam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *OpenAIChatCompletionContentPartParam) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *OpenAIChatCompletionContentPartParam) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *OpenAIChatCompletionContentPartParam) SetType(v string)`

SetType sets Type field to given value.


### GetText

`func (o *OpenAIChatCompletionContentPartParam) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *OpenAIChatCompletionContentPartParam) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *OpenAIChatCompletionContentPartParam) SetText(v string)`

SetText sets Text field to given value.


### GetImageUrl

`func (o *OpenAIChatCompletionContentPartParam) GetImageUrl() OpenAIImageURL`

GetImageUrl returns the ImageUrl field if non-nil, zero value otherwise.

### GetImageUrlOk

`func (o *OpenAIChatCompletionContentPartParam) GetImageUrlOk() (*OpenAIImageURL, bool)`

GetImageUrlOk returns a tuple with the ImageUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImageUrl

`func (o *OpenAIChatCompletionContentPartParam) SetImageUrl(v OpenAIImageURL)`

SetImageUrl sets ImageUrl field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


