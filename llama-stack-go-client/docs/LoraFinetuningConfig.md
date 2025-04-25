# LoraFinetuningConfig

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

## Methods

### NewLoraFinetuningConfig

`func NewLoraFinetuningConfig(type_ string, loraAttnModules []string, applyLoraToMlp bool, applyLoraToOutput bool, rank int32, alpha int32, ) *LoraFinetuningConfig`

NewLoraFinetuningConfig instantiates a new LoraFinetuningConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLoraFinetuningConfigWithDefaults

`func NewLoraFinetuningConfigWithDefaults() *LoraFinetuningConfig`

NewLoraFinetuningConfigWithDefaults instantiates a new LoraFinetuningConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *LoraFinetuningConfig) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *LoraFinetuningConfig) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *LoraFinetuningConfig) SetType(v string)`

SetType sets Type field to given value.


### GetLoraAttnModules

`func (o *LoraFinetuningConfig) GetLoraAttnModules() []string`

GetLoraAttnModules returns the LoraAttnModules field if non-nil, zero value otherwise.

### GetLoraAttnModulesOk

`func (o *LoraFinetuningConfig) GetLoraAttnModulesOk() (*[]string, bool)`

GetLoraAttnModulesOk returns a tuple with the LoraAttnModules field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoraAttnModules

`func (o *LoraFinetuningConfig) SetLoraAttnModules(v []string)`

SetLoraAttnModules sets LoraAttnModules field to given value.


### GetApplyLoraToMlp

`func (o *LoraFinetuningConfig) GetApplyLoraToMlp() bool`

GetApplyLoraToMlp returns the ApplyLoraToMlp field if non-nil, zero value otherwise.

### GetApplyLoraToMlpOk

`func (o *LoraFinetuningConfig) GetApplyLoraToMlpOk() (*bool, bool)`

GetApplyLoraToMlpOk returns a tuple with the ApplyLoraToMlp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplyLoraToMlp

`func (o *LoraFinetuningConfig) SetApplyLoraToMlp(v bool)`

SetApplyLoraToMlp sets ApplyLoraToMlp field to given value.


### GetApplyLoraToOutput

`func (o *LoraFinetuningConfig) GetApplyLoraToOutput() bool`

GetApplyLoraToOutput returns the ApplyLoraToOutput field if non-nil, zero value otherwise.

### GetApplyLoraToOutputOk

`func (o *LoraFinetuningConfig) GetApplyLoraToOutputOk() (*bool, bool)`

GetApplyLoraToOutputOk returns a tuple with the ApplyLoraToOutput field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApplyLoraToOutput

`func (o *LoraFinetuningConfig) SetApplyLoraToOutput(v bool)`

SetApplyLoraToOutput sets ApplyLoraToOutput field to given value.


### GetRank

`func (o *LoraFinetuningConfig) GetRank() int32`

GetRank returns the Rank field if non-nil, zero value otherwise.

### GetRankOk

`func (o *LoraFinetuningConfig) GetRankOk() (*int32, bool)`

GetRankOk returns a tuple with the Rank field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRank

`func (o *LoraFinetuningConfig) SetRank(v int32)`

SetRank sets Rank field to given value.


### GetAlpha

`func (o *LoraFinetuningConfig) GetAlpha() int32`

GetAlpha returns the Alpha field if non-nil, zero value otherwise.

### GetAlphaOk

`func (o *LoraFinetuningConfig) GetAlphaOk() (*int32, bool)`

GetAlphaOk returns a tuple with the Alpha field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlpha

`func (o *LoraFinetuningConfig) SetAlpha(v int32)`

SetAlpha sets Alpha field to given value.


### GetUseDora

`func (o *LoraFinetuningConfig) GetUseDora() bool`

GetUseDora returns the UseDora field if non-nil, zero value otherwise.

### GetUseDoraOk

`func (o *LoraFinetuningConfig) GetUseDoraOk() (*bool, bool)`

GetUseDoraOk returns a tuple with the UseDora field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUseDora

`func (o *LoraFinetuningConfig) SetUseDora(v bool)`

SetUseDora sets UseDora field to given value.

### HasUseDora

`func (o *LoraFinetuningConfig) HasUseDora() bool`

HasUseDora returns a boolean if a field has been set.

### GetQuantizeBase

`func (o *LoraFinetuningConfig) GetQuantizeBase() bool`

GetQuantizeBase returns the QuantizeBase field if non-nil, zero value otherwise.

### GetQuantizeBaseOk

`func (o *LoraFinetuningConfig) GetQuantizeBaseOk() (*bool, bool)`

GetQuantizeBaseOk returns a tuple with the QuantizeBase field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuantizeBase

`func (o *LoraFinetuningConfig) SetQuantizeBase(v bool)`

SetQuantizeBase sets QuantizeBase field to given value.

### HasQuantizeBase

`func (o *LoraFinetuningConfig) HasQuantizeBase() bool`

HasQuantizeBase returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


