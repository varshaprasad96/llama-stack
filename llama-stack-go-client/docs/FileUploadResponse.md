# FileUploadResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | ID of the upload session | 
**Url** | **string** | Upload URL for the file or file parts | 
**Offset** | **int32** | Upload content offset | 
**Size** | **int32** | Upload content size | 

## Methods

### NewFileUploadResponse

`func NewFileUploadResponse(id string, url string, offset int32, size int32, ) *FileUploadResponse`

NewFileUploadResponse instantiates a new FileUploadResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileUploadResponseWithDefaults

`func NewFileUploadResponseWithDefaults() *FileUploadResponse`

NewFileUploadResponseWithDefaults instantiates a new FileUploadResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *FileUploadResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *FileUploadResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *FileUploadResponse) SetId(v string)`

SetId sets Id field to given value.


### GetUrl

`func (o *FileUploadResponse) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *FileUploadResponse) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *FileUploadResponse) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetOffset

`func (o *FileUploadResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *FileUploadResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *FileUploadResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.


### GetSize

`func (o *FileUploadResponse) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *FileUploadResponse) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *FileUploadResponse) SetSize(v int32)`

SetSize sets Size field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


