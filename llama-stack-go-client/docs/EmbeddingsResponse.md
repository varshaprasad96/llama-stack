# EmbeddingsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Embeddings** | **[][]float32** | List of embedding vectors, one per input content. Each embedding is a list of floats. The dimensionality of the embedding is model-specific; you can check model metadata using /models/{model_id} | 

## Methods

### NewEmbeddingsResponse

`func NewEmbeddingsResponse(embeddings [][]float32, ) *EmbeddingsResponse`

NewEmbeddingsResponse instantiates a new EmbeddingsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEmbeddingsResponseWithDefaults

`func NewEmbeddingsResponseWithDefaults() *EmbeddingsResponse`

NewEmbeddingsResponseWithDefaults instantiates a new EmbeddingsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEmbeddings

`func (o *EmbeddingsResponse) GetEmbeddings() [][]float32`

GetEmbeddings returns the Embeddings field if non-nil, zero value otherwise.

### GetEmbeddingsOk

`func (o *EmbeddingsResponse) GetEmbeddingsOk() (*[][]float32, bool)`

GetEmbeddingsOk returns a tuple with the Embeddings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddings

`func (o *EmbeddingsResponse) SetEmbeddings(v [][]float32)`

SetEmbeddings sets Embeddings field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


