# ImageContentItemImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Url** | Pointer to [**URL**](URL.md) | A URL of the image or data URL in the format of data:image/{type};base64,{data}. Note that URL could have length limits. | [optional] 
**Data** | Pointer to **string** | base64 encoded image data as string | [optional] 

## Methods

### NewImageContentItemImage

`func NewImageContentItemImage() *ImageContentItemImage`

NewImageContentItemImage instantiates a new ImageContentItemImage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewImageContentItemImageWithDefaults

`func NewImageContentItemImageWithDefaults() *ImageContentItemImage`

NewImageContentItemImageWithDefaults instantiates a new ImageContentItemImage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUrl

`func (o *ImageContentItemImage) GetUrl() URL`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *ImageContentItemImage) GetUrlOk() (*URL, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *ImageContentItemImage) SetUrl(v URL)`

SetUrl sets Url field to given value.

### HasUrl

`func (o *ImageContentItemImage) HasUrl() bool`

HasUrl returns a boolean if a field has been set.

### GetData

`func (o *ImageContentItemImage) GetData() string`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ImageContentItemImage) GetDataOk() (*string, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ImageContentItemImage) SetData(v string)`

SetData sets Data field to given value.

### HasData

`func (o *ImageContentItemImage) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


