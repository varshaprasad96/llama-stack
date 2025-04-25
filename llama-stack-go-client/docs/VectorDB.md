# VectorDB

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Identifier** | **string** |  | 
**ProviderResourceId** | **string** |  | 
**ProviderId** | **string** |  | 
**Type** | **string** |  | [default to "vector_db"]
**EmbeddingModel** | **string** |  | 
**EmbeddingDimension** | **int32** |  | 

## Methods

### NewVectorDB

`func NewVectorDB(identifier string, providerResourceId string, providerId string, type_ string, embeddingModel string, embeddingDimension int32, ) *VectorDB`

NewVectorDB instantiates a new VectorDB object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVectorDBWithDefaults

`func NewVectorDBWithDefaults() *VectorDB`

NewVectorDBWithDefaults instantiates a new VectorDB object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdentifier

`func (o *VectorDB) GetIdentifier() string`

GetIdentifier returns the Identifier field if non-nil, zero value otherwise.

### GetIdentifierOk

`func (o *VectorDB) GetIdentifierOk() (*string, bool)`

GetIdentifierOk returns a tuple with the Identifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifier

`func (o *VectorDB) SetIdentifier(v string)`

SetIdentifier sets Identifier field to given value.


### GetProviderResourceId

`func (o *VectorDB) GetProviderResourceId() string`

GetProviderResourceId returns the ProviderResourceId field if non-nil, zero value otherwise.

### GetProviderResourceIdOk

`func (o *VectorDB) GetProviderResourceIdOk() (*string, bool)`

GetProviderResourceIdOk returns a tuple with the ProviderResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderResourceId

`func (o *VectorDB) SetProviderResourceId(v string)`

SetProviderResourceId sets ProviderResourceId field to given value.


### GetProviderId

`func (o *VectorDB) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *VectorDB) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *VectorDB) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetType

`func (o *VectorDB) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *VectorDB) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *VectorDB) SetType(v string)`

SetType sets Type field to given value.


### GetEmbeddingModel

`func (o *VectorDB) GetEmbeddingModel() string`

GetEmbeddingModel returns the EmbeddingModel field if non-nil, zero value otherwise.

### GetEmbeddingModelOk

`func (o *VectorDB) GetEmbeddingModelOk() (*string, bool)`

GetEmbeddingModelOk returns a tuple with the EmbeddingModel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddingModel

`func (o *VectorDB) SetEmbeddingModel(v string)`

SetEmbeddingModel sets EmbeddingModel field to given value.


### GetEmbeddingDimension

`func (o *VectorDB) GetEmbeddingDimension() int32`

GetEmbeddingDimension returns the EmbeddingDimension field if non-nil, zero value otherwise.

### GetEmbeddingDimensionOk

`func (o *VectorDB) GetEmbeddingDimensionOk() (*int32, bool)`

GetEmbeddingDimensionOk returns a tuple with the EmbeddingDimension field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddingDimension

`func (o *VectorDB) SetEmbeddingDimension(v int32)`

SetEmbeddingDimension sets EmbeddingDimension field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


