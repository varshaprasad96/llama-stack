# Attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | [**AttachmentContent**](AttachmentContent.md) |  | 
**MimeType** | **string** | The MIME type of the attachment. | 

## Methods

### NewAttachment

`func NewAttachment(content AttachmentContent, mimeType string, ) *Attachment`

NewAttachment instantiates a new Attachment object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAttachmentWithDefaults

`func NewAttachmentWithDefaults() *Attachment`

NewAttachmentWithDefaults instantiates a new Attachment object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *Attachment) GetContent() AttachmentContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *Attachment) GetContentOk() (*AttachmentContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *Attachment) SetContent(v AttachmentContent)`

SetContent sets Content field to given value.


### GetMimeType

`func (o *Attachment) GetMimeType() string`

GetMimeType returns the MimeType field if non-nil, zero value otherwise.

### GetMimeTypeOk

`func (o *Attachment) GetMimeTypeOk() (*string, bool)`

GetMimeTypeOk returns a tuple with the MimeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeType

`func (o *Attachment) SetMimeType(v string)`

SetMimeType sets MimeType field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


