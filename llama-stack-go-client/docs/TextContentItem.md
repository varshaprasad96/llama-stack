# TextContentItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Discriminator type of the content item. Always \&quot;text\&quot; | [default to "text"]
**Text** | **string** | Text content | 

## Methods

### NewTextContentItem

`func NewTextContentItem(type_ string, text string, ) *TextContentItem`

NewTextContentItem instantiates a new TextContentItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTextContentItemWithDefaults

`func NewTextContentItemWithDefaults() *TextContentItem`

NewTextContentItemWithDefaults instantiates a new TextContentItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *TextContentItem) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *TextContentItem) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *TextContentItem) SetType(v string)`

SetType sets Type field to given value.


### GetText

`func (o *TextContentItem) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *TextContentItem) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *TextContentItem) SetText(v string)`

SetText sets Text field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


