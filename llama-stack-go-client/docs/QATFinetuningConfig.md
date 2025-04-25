# QATFinetuningConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "QAT"]
**QuantizerName** | **string** |  | 
**GroupSize** | **int32** |  | 

## Methods

### NewQATFinetuningConfig

`func NewQATFinetuningConfig(type_ string, quantizerName string, groupSize int32, ) *QATFinetuningConfig`

NewQATFinetuningConfig instantiates a new QATFinetuningConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQATFinetuningConfigWithDefaults

`func NewQATFinetuningConfigWithDefaults() *QATFinetuningConfig`

NewQATFinetuningConfigWithDefaults instantiates a new QATFinetuningConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *QATFinetuningConfig) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *QATFinetuningConfig) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *QATFinetuningConfig) SetType(v string)`

SetType sets Type field to given value.


### GetQuantizerName

`func (o *QATFinetuningConfig) GetQuantizerName() string`

GetQuantizerName returns the QuantizerName field if non-nil, zero value otherwise.

### GetQuantizerNameOk

`func (o *QATFinetuningConfig) GetQuantizerNameOk() (*string, bool)`

GetQuantizerNameOk returns a tuple with the QuantizerName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuantizerName

`func (o *QATFinetuningConfig) SetQuantizerName(v string)`

SetQuantizerName sets QuantizerName field to given value.


### GetGroupSize

`func (o *QATFinetuningConfig) GetGroupSize() int32`

GetGroupSize returns the GroupSize field if non-nil, zero value otherwise.

### GetGroupSizeOk

`func (o *QATFinetuningConfig) GetGroupSizeOk() (*int32, bool)`

GetGroupSizeOk returns a tuple with the GroupSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupSize

`func (o *QATFinetuningConfig) SetGroupSize(v int32)`

SetGroupSize sets GroupSize field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


