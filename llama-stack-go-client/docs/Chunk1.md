# Chunk1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | [**InterleavedContent**](InterleavedContent.md) |  | 
**Metadata** | [**map[string]Chunk1MetadataValue**](Chunk1MetadataValue.md) |  | 

## Methods

### NewChunk1

`func NewChunk1(content InterleavedContent, metadata map[string]Chunk1MetadataValue, ) *Chunk1`

NewChunk1 instantiates a new Chunk1 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewChunk1WithDefaults

`func NewChunk1WithDefaults() *Chunk1`

NewChunk1WithDefaults instantiates a new Chunk1 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *Chunk1) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *Chunk1) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *Chunk1) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.


### GetMetadata

`func (o *Chunk1) GetMetadata() map[string]Chunk1MetadataValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Chunk1) GetMetadataOk() (*map[string]Chunk1MetadataValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Chunk1) SetMetadata(v map[string]Chunk1MetadataValue)`

SetMetadata sets Metadata field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


