# RAGQueryConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**QueryGeneratorConfig** | [**RAGQueryGeneratorConfig**](RAGQueryGeneratorConfig.md) |  | 
**MaxTokensInContext** | **int32** |  | [default to 4096]
**MaxChunks** | **int32** |  | [default to 5]

## Methods

### NewRAGQueryConfig

`func NewRAGQueryConfig(queryGeneratorConfig RAGQueryGeneratorConfig, maxTokensInContext int32, maxChunks int32, ) *RAGQueryConfig`

NewRAGQueryConfig instantiates a new RAGQueryConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRAGQueryConfigWithDefaults

`func NewRAGQueryConfigWithDefaults() *RAGQueryConfig`

NewRAGQueryConfigWithDefaults instantiates a new RAGQueryConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQueryGeneratorConfig

`func (o *RAGQueryConfig) GetQueryGeneratorConfig() RAGQueryGeneratorConfig`

GetQueryGeneratorConfig returns the QueryGeneratorConfig field if non-nil, zero value otherwise.

### GetQueryGeneratorConfigOk

`func (o *RAGQueryConfig) GetQueryGeneratorConfigOk() (*RAGQueryGeneratorConfig, bool)`

GetQueryGeneratorConfigOk returns a tuple with the QueryGeneratorConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQueryGeneratorConfig

`func (o *RAGQueryConfig) SetQueryGeneratorConfig(v RAGQueryGeneratorConfig)`

SetQueryGeneratorConfig sets QueryGeneratorConfig field to given value.


### GetMaxTokensInContext

`func (o *RAGQueryConfig) GetMaxTokensInContext() int32`

GetMaxTokensInContext returns the MaxTokensInContext field if non-nil, zero value otherwise.

### GetMaxTokensInContextOk

`func (o *RAGQueryConfig) GetMaxTokensInContextOk() (*int32, bool)`

GetMaxTokensInContextOk returns a tuple with the MaxTokensInContext field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxTokensInContext

`func (o *RAGQueryConfig) SetMaxTokensInContext(v int32)`

SetMaxTokensInContext sets MaxTokensInContext field to given value.


### GetMaxChunks

`func (o *RAGQueryConfig) GetMaxChunks() int32`

GetMaxChunks returns the MaxChunks field if non-nil, zero value otherwise.

### GetMaxChunksOk

`func (o *RAGQueryConfig) GetMaxChunksOk() (*int32, bool)`

GetMaxChunksOk returns a tuple with the MaxChunks field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxChunks

`func (o *RAGQueryConfig) SetMaxChunks(v int32)`

SetMaxChunks sets MaxChunks field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


