# QueryChunksResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Chunks** | [**[]Chunk1**](Chunk1.md) |  | 
**Scores** | **[]float32** |  | 

## Methods

### NewQueryChunksResponse

`func NewQueryChunksResponse(chunks []Chunk1, scores []float32, ) *QueryChunksResponse`

NewQueryChunksResponse instantiates a new QueryChunksResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryChunksResponseWithDefaults

`func NewQueryChunksResponseWithDefaults() *QueryChunksResponse`

NewQueryChunksResponseWithDefaults instantiates a new QueryChunksResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetChunks

`func (o *QueryChunksResponse) GetChunks() []Chunk1`

GetChunks returns the Chunks field if non-nil, zero value otherwise.

### GetChunksOk

`func (o *QueryChunksResponse) GetChunksOk() (*[]Chunk1, bool)`

GetChunksOk returns a tuple with the Chunks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChunks

`func (o *QueryChunksResponse) SetChunks(v []Chunk1)`

SetChunks sets Chunks field to given value.


### GetScores

`func (o *QueryChunksResponse) GetScores() []float32`

GetScores returns the Scores field if non-nil, zero value otherwise.

### GetScoresOk

`func (o *QueryChunksResponse) GetScoresOk() (*[]float32, bool)`

GetScoresOk returns a tuple with the Scores field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScores

`func (o *QueryChunksResponse) SetScores(v []float32)`

SetScores sets Scores field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


