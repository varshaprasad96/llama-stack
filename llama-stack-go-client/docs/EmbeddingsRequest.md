# EmbeddingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ModelId** | **string** | The identifier of the model to use. The model must be an embedding model registered with Llama Stack and available via the /models endpoint. | 
**Contents** | [**EmbeddingsRequestContents**](EmbeddingsRequestContents.md) |  | 
**TextTruncation** | Pointer to **string** | (Optional) Config for how to truncate text for embedding when text is longer than the model&#39;s max sequence length. | [optional] 
**OutputDimension** | Pointer to **int32** | (Optional) Output dimensionality for the embeddings. Only supported by Matryoshka models. | [optional] 
**TaskType** | Pointer to **string** | (Optional) How is the embedding being used? This is only supported by asymmetric embedding models. | [optional] 

## Methods

### NewEmbeddingsRequest

`func NewEmbeddingsRequest(modelId string, contents EmbeddingsRequestContents, ) *EmbeddingsRequest`

NewEmbeddingsRequest instantiates a new EmbeddingsRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEmbeddingsRequestWithDefaults

`func NewEmbeddingsRequestWithDefaults() *EmbeddingsRequest`

NewEmbeddingsRequestWithDefaults instantiates a new EmbeddingsRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModelId

`func (o *EmbeddingsRequest) GetModelId() string`

GetModelId returns the ModelId field if non-nil, zero value otherwise.

### GetModelIdOk

`func (o *EmbeddingsRequest) GetModelIdOk() (*string, bool)`

GetModelIdOk returns a tuple with the ModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelId

`func (o *EmbeddingsRequest) SetModelId(v string)`

SetModelId sets ModelId field to given value.


### GetContents

`func (o *EmbeddingsRequest) GetContents() EmbeddingsRequestContents`

GetContents returns the Contents field if non-nil, zero value otherwise.

### GetContentsOk

`func (o *EmbeddingsRequest) GetContentsOk() (*EmbeddingsRequestContents, bool)`

GetContentsOk returns a tuple with the Contents field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContents

`func (o *EmbeddingsRequest) SetContents(v EmbeddingsRequestContents)`

SetContents sets Contents field to given value.


### GetTextTruncation

`func (o *EmbeddingsRequest) GetTextTruncation() string`

GetTextTruncation returns the TextTruncation field if non-nil, zero value otherwise.

### GetTextTruncationOk

`func (o *EmbeddingsRequest) GetTextTruncationOk() (*string, bool)`

GetTextTruncationOk returns a tuple with the TextTruncation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextTruncation

`func (o *EmbeddingsRequest) SetTextTruncation(v string)`

SetTextTruncation sets TextTruncation field to given value.

### HasTextTruncation

`func (o *EmbeddingsRequest) HasTextTruncation() bool`

HasTextTruncation returns a boolean if a field has been set.

### GetOutputDimension

`func (o *EmbeddingsRequest) GetOutputDimension() int32`

GetOutputDimension returns the OutputDimension field if non-nil, zero value otherwise.

### GetOutputDimensionOk

`func (o *EmbeddingsRequest) GetOutputDimensionOk() (*int32, bool)`

GetOutputDimensionOk returns a tuple with the OutputDimension field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputDimension

`func (o *EmbeddingsRequest) SetOutputDimension(v int32)`

SetOutputDimension sets OutputDimension field to given value.

### HasOutputDimension

`func (o *EmbeddingsRequest) HasOutputDimension() bool`

HasOutputDimension returns a boolean if a field has been set.

### GetTaskType

`func (o *EmbeddingsRequest) GetTaskType() string`

GetTaskType returns the TaskType field if non-nil, zero value otherwise.

### GetTaskTypeOk

`func (o *EmbeddingsRequest) GetTaskTypeOk() (*string, bool)`

GetTaskTypeOk returns a tuple with the TaskType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTaskType

`func (o *EmbeddingsRequest) SetTaskType(v string)`

SetTaskType sets TaskType field to given value.

### HasTaskType

`func (o *EmbeddingsRequest) HasTaskType() bool`

HasTaskType returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


