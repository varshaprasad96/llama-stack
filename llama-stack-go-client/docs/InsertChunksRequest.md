# InsertChunksRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**VectorDbId** | **string** |  | 
**Chunks** | [**[]Chunk**](Chunk.md) |  | 
**TtlSeconds** | Pointer to **int32** |  | [optional] 

## Methods

### NewInsertChunksRequest

`func NewInsertChunksRequest(vectorDbId string, chunks []Chunk, ) *InsertChunksRequest`

NewInsertChunksRequest instantiates a new InsertChunksRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInsertChunksRequestWithDefaults

`func NewInsertChunksRequestWithDefaults() *InsertChunksRequest`

NewInsertChunksRequestWithDefaults instantiates a new InsertChunksRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVectorDbId

`func (o *InsertChunksRequest) GetVectorDbId() string`

GetVectorDbId returns the VectorDbId field if non-nil, zero value otherwise.

### GetVectorDbIdOk

`func (o *InsertChunksRequest) GetVectorDbIdOk() (*string, bool)`

GetVectorDbIdOk returns a tuple with the VectorDbId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVectorDbId

`func (o *InsertChunksRequest) SetVectorDbId(v string)`

SetVectorDbId sets VectorDbId field to given value.


### GetChunks

`func (o *InsertChunksRequest) GetChunks() []Chunk`

GetChunks returns the Chunks field if non-nil, zero value otherwise.

### GetChunksOk

`func (o *InsertChunksRequest) GetChunksOk() (*[]Chunk, bool)`

GetChunksOk returns a tuple with the Chunks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChunks

`func (o *InsertChunksRequest) SetChunks(v []Chunk)`

SetChunks sets Chunks field to given value.


### GetTtlSeconds

`func (o *InsertChunksRequest) GetTtlSeconds() int32`

GetTtlSeconds returns the TtlSeconds field if non-nil, zero value otherwise.

### GetTtlSecondsOk

`func (o *InsertChunksRequest) GetTtlSecondsOk() (*int32, bool)`

GetTtlSecondsOk returns a tuple with the TtlSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTtlSeconds

`func (o *InsertChunksRequest) SetTtlSeconds(v int32)`

SetTtlSeconds sets TtlSeconds field to given value.

### HasTtlSeconds

`func (o *InsertChunksRequest) HasTtlSeconds() bool`

HasTtlSeconds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


