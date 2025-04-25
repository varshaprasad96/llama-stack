# Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | [**DocumentContent**](DocumentContent.md) |  | 
**MimeType** | **string** | The MIME type of the document. | 

## Methods

### NewDocument

`func NewDocument(content DocumentContent, mimeType string, ) *Document`

NewDocument instantiates a new Document object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentWithDefaults

`func NewDocumentWithDefaults() *Document`

NewDocumentWithDefaults instantiates a new Document object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *Document) GetContent() DocumentContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *Document) GetContentOk() (*DocumentContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *Document) SetContent(v DocumentContent)`

SetContent sets Content field to given value.


### GetMimeType

`func (o *Document) GetMimeType() string`

GetMimeType returns the MimeType field if non-nil, zero value otherwise.

### GetMimeTypeOk

`func (o *Document) GetMimeTypeOk() (*string, bool)`

GetMimeTypeOk returns a tuple with the MimeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMimeType

`func (o *Document) SetMimeType(v string)`

SetMimeType sets MimeType field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


