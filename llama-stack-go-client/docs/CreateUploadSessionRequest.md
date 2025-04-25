# CreateUploadSessionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | **string** | Bucket under which the file is stored (valid chars: a-zA-Z0-9_-) | 
**Key** | **string** | Key under which the file is stored (valid chars: a-zA-Z0-9_-/.) | 
**MimeType** | **string** | MIME type of the file | 
**Size** | **int32** | File size in bytes | 

## Methods

### NewCreateUploadSessionRequest

`func NewCreateUploadSessionRequest(bucket string, key string, mimeType string, size int32, ) *CreateUploadSessionRequest`

NewCreateUploadSessionRequest instantiates a new CreateUploadSessionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateUploadSessionRequestWithDefaults

`func NewCreateUploadSessionRequestWithDefaults() *CreateUploadSessionRequest`

NewCreateUploadSessionRequestWithDefaults instantiates a new CreateUploadSessionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBucket

`func (o *CreateUploadSessionRequest) GetBucket() string`

GetBucket returns the Bucket field if non-nil, zero value otherwise.

### GetBucketOk

`func (o *CreateUploadSessionRequest) GetBucketOk() (*string, bool)`

GetBucketOk returns a tuple with the Bucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBucket

`func (o *CreateUploadSessionRequest) SetBucket(v string)`

SetBucket sets Bucket field to given value.


### GetKey

`func (o *CreateUploadSessionRequest) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *CreateUploadSessionRequest) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *CreateUploadSessionRequest) SetKey(v string)`

SetKey sets Key field to given value.


### GetMimeType

`func (o *CreateUploadSessionRequest) GetMimeType() string`

GetMimeType returns the MimeType field if non-nil, zero value otherwise.

### GetMimeTypeOk

`func (o *CreateUploadSessionRequest) GetMimeTypeOk() (*string, bool)`

GetMimeTypeOk returns a tuple with the MimeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeType

`func (o *CreateUploadSessionRequest) SetMimeType(v string)`

SetMimeType sets MimeType field to given value.


### GetSize

`func (o *CreateUploadSessionRequest) GetSize() int32`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *CreateUploadSessionRequest) GetSizeOk() (*int32, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *CreateUploadSessionRequest) SetSize(v int32)`

SetSize sets Size field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


