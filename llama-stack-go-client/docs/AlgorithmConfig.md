# AlgorithmConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "LoRA"]
**LoraAttnModules** | **[]string** |  | 
**ApplyLoraToMlp** | **bool** |  | 
**ApplyLoraToOutput** | **bool** |  | 
**Rank** | **int32** |  | 
**Alpha** | **int32** |  | 
**UseDora** | Pointer to **bool** |  | [optional] [default to false]
**QuantizeBase** | Pointer to **bool** |  | [optional] [default to false]
**QuantizerName** | **string** |  | 
**GroupSize** | **int32** |  | 

## Methods

### NewAlgorithmConfig

`func NewAlgorithmConfig(type_ string, loraAttnModules []string, applyLoraToMlp bool, applyLoraToOutput bool, rank int32, alpha int32, quantizerName string, groupSize int32, ) *AlgorithmConfig`

NewAlgorithmConfig instantiates a new AlgorithmConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAlgorithmConfigWithDefaults

`func NewAlgorithmConfigWithDefaults() *AlgorithmConfig`

NewAlgorithmConfigWithDefaults instantiates a new AlgorithmConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *AlgorithmConfig) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AlgorithmConfig) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AlgorithmConfig) SetType(v string)`

SetType sets Type field to given value.


### GetLoraAttnModules

`func (o *AlgorithmConfig) GetLoraAttnModules() []string`

GetLoraAttnModules returns the LoraAttnModules field if non-nil, zero value otherwise.

### GetLoraAttnModulesOk

`func (o *AlgorithmConfig) GetLoraAttnModulesOk() (*[]string, bool)`

GetLoraAttnModulesOk returns a tuple with the LoraAttnModules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoraAttnModules

`func (o *AlgorithmConfig) SetLoraAttnModules(v []string)`

SetLoraAttnModules sets LoraAttnModules field to given value.


### GetApplyLoraToMlp

`func (o *AlgorithmConfig) GetApplyLoraToMlp() bool`

GetApplyLoraToMlp returns the ApplyLoraToMlp field if non-nil, zero value otherwise.

### GetApplyLoraToMlpOk

`func (o *AlgorithmConfig) GetApplyLoraToMlpOk() (*bool, bool)`

GetApplyLoraToMlpOk returns a tuple with the ApplyLoraToMlp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplyLoraToMlp

`func (o *AlgorithmConfig) SetApplyLoraToMlp(v bool)`

SetApplyLoraToMlp sets ApplyLoraToMlp field to given value.


### GetApplyLoraToOutput

`func (o *AlgorithmConfig) GetApplyLoraToOutput() bool`

GetApplyLoraToOutput returns the ApplyLoraToOutput field if non-nil, zero value otherwise.

### GetApplyLoraToOutputOk

`func (o *AlgorithmConfig) GetApplyLoraToOutputOk() (*bool, bool)`

GetApplyLoraToOutputOk returns a tuple with the ApplyLoraToOutput field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplyLoraToOutput

`func (o *AlgorithmConfig) SetApplyLoraToOutput(v bool)`

SetApplyLoraToOutput sets ApplyLoraToOutput field to given value.


### GetRank

`func (o *AlgorithmConfig) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *AlgorithmConfig) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *AlgorithmConfig) SetRank(v int32)`

SetRank sets Rank field to given value.


### GetAlpha

`func (o *AlgorithmConfig) GetAlpha() int32`

GetAlpha returns the Alpha field if non-nil, zero value otherwise.

### GetAlphaOk

`func (o *AlgorithmConfig) GetAlphaOk() (*int32, bool)`

GetAlphaOk returns a tuple with the Alpha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlpha

`func (o *AlgorithmConfig) SetAlpha(v int32)`

SetAlpha sets Alpha field to given value.


### GetUseDora

`func (o *AlgorithmConfig) GetUseDora() bool`

GetUseDora returns the UseDora field if non-nil, zero value otherwise.

### GetUseDoraOk

`func (o *AlgorithmConfig) GetUseDoraOk() (*bool, bool)`

GetUseDoraOk returns a tuple with the UseDora field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseDora

`func (o *AlgorithmConfig) SetUseDora(v bool)`

SetUseDora sets UseDora field to given value.

### HasUseDora

`func (o *AlgorithmConfig) HasUseDora() bool`

HasUseDora returns a boolean if a field has been set.

### GetQuantizeBase

`func (o *AlgorithmConfig) GetQuantizeBase() bool`

GetQuantizeBase returns the QuantizeBase field if non-nil, zero value otherwise.

### GetQuantizeBaseOk

`func (o *AlgorithmConfig) GetQuantizeBaseOk() (*bool, bool)`

GetQuantizeBaseOk returns a tuple with the QuantizeBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuantizeBase

`func (o *AlgorithmConfig) SetQuantizeBase(v bool)`

SetQuantizeBase sets QuantizeBase field to given value.

### HasQuantizeBase

`func (o *AlgorithmConfig) HasQuantizeBase() bool`

HasQuantizeBase returns a boolean if a field has been set.

### GetQuantizerName

`func (o *AlgorithmConfig) GetQuantizerName() string`

GetQuantizerName returns the QuantizerName field if non-nil, zero value otherwise.

### GetQuantizerNameOk

`func (o *AlgorithmConfig) GetQuantizerNameOk() (*string, bool)`

GetQuantizerNameOk returns a tuple with the QuantizerName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuantizerName

`func (o *AlgorithmConfig) SetQuantizerName(v string)`

SetQuantizerName sets QuantizerName field to given value.


### GetGroupSize

`func (o *AlgorithmConfig) GetGroupSize() int32`

GetGroupSize returns the GroupSize field if non-nil, zero value otherwise.

### GetGroupSizeOk

`func (o *AlgorithmConfig) GetGroupSizeOk() (*int32, bool)`

GetGroupSizeOk returns a tuple with the GroupSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupSize

`func (o *AlgorithmConfig) SetGroupSize(v int32)`

SetGroupSize sets GroupSize field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


