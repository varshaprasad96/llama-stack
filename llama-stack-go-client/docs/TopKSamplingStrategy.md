# TopKSamplingStrategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "top_k"]
**TopK** | **int32** |  | 

## Methods

### NewTopKSamplingStrategy

`func NewTopKSamplingStrategy(type_ string, topK int32, ) *TopKSamplingStrategy`

NewTopKSamplingStrategy instantiates a new TopKSamplingStrategy object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTopKSamplingStrategyWithDefaults

`func NewTopKSamplingStrategyWithDefaults() *TopKSamplingStrategy`

NewTopKSamplingStrategyWithDefaults instantiates a new TopKSamplingStrategy object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *TopKSamplingStrategy) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *TopKSamplingStrategy) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *TopKSamplingStrategy) SetType(v string)`

SetType sets Type field to given value.


### GetTopK

`func (o *TopKSamplingStrategy) GetTopK() int32`

GetTopK returns the TopK field if non-nil, zero value otherwise.

### GetTopKOk

`func (o *TopKSamplingStrategy) GetTopKOk() (*int32, bool)`

GetTopKOk returns a tuple with the TopK field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTopK

`func (o *TopKSamplingStrategy) SetTopK(v int32)`

SetTopK sets TopK field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


