# FileResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | **string** | Bucket under which the file is stored (valid chars: a-zA-Z0-9_-) | 
**Key** | **string** | Key under which the file is stored (valid chars: a-zA-Z0-9_-/.) | 
**MimeType** | **string** | MIME type of the file | 
**Url** | **string** | Upload URL for the file contents | 
**Bytes** | **int32** | Size of the file in bytes | 
**CreatedAt** | **int32** | Timestamp of when the file was created | 

## Methods

### NewFileResponse

`func NewFileResponse(bucket string, key string, mimeType string, url string, bytes int32, createdAt int32, ) *FileResponse`

NewFileResponse instantiates a new FileResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFileResponseWithDefaults

`func NewFileResponseWithDefaults() *FileResponse`

NewFileResponseWithDefaults instantiates a new FileResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBucket

`func (o *FileResponse) GetBucket() string`

GetBucket returns the Bucket field if non-nil, zero value otherwise.

### GetBucketOk

`func (o *FileResponse) GetBucketOk() (*string, bool)`

GetBucketOk returns a tuple with the Bucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBucket

`func (o *FileResponse) SetBucket(v string)`

SetBucket sets Bucket field to given value.


### GetKey

`func (o *FileResponse) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *FileResponse) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *FileResponse) SetKey(v string)`

SetKey sets Key field to given value.


### GetMimeType

`func (o *FileResponse) GetMimeType() string`

GetMimeType returns the MimeType field if non-nil, zero value otherwise.

### GetMimeTypeOk

`func (o *FileResponse) GetMimeTypeOk() (*string, bool)`

GetMimeTypeOk returns a tuple with the MimeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeType

`func (o *FileResponse) SetMimeType(v string)`

SetMimeType sets MimeType field to given value.


### GetUrl

`func (o *FileResponse) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *FileResponse) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *FileResponse) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetBytes

`func (o *FileResponse) GetBytes() int32`

GetBytes returns the Bytes field if non-nil, zero value otherwise.

### GetBytesOk

`func (o *FileResponse) GetBytesOk() (*int32, bool)`

GetBytesOk returns a tuple with the Bytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBytes

`func (o *FileResponse) SetBytes(v int32)`

SetBytes sets Bytes field to given value.


### GetCreatedAt

`func (o *FileResponse) GetCreatedAt() int32`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *FileResponse) GetCreatedAtOk() (*int32, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *FileResponse) SetCreatedAt(v int32)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


