# ImageContentItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Discriminator type of the content item. Always \&quot;image\&quot; | [default to "image"]
**Image** | [**ImageContentItemImage**](ImageContentItemImage.md) |  | 

## Methods

### NewImageContentItem

`func NewImageContentItem(type_ string, image ImageContentItemImage, ) *ImageContentItem`

NewImageContentItem instantiates a new ImageContentItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewImageContentItemWithDefaults

`func NewImageContentItemWithDefaults() *ImageContentItem`

NewImageContentItemWithDefaults instantiates a new ImageContentItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *ImageContentItem) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ImageContentItem) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ImageContentItem) SetType(v string)`

SetType sets Type field to given value.


### GetImage

`func (o *ImageContentItem) GetImage() ImageContentItemImage`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *ImageContentItem) GetImageOk() (*ImageContentItemImage, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *ImageContentItem) SetImage(v ImageContentItemImage)`

SetImage sets Image field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


