# DPOAlignmentConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RewardScale** | **float32** |  | 
**RewardClip** | **float32** |  | 
**Epsilon** | **float32** |  | 
**Gamma** | **float32** |  | 

## Methods

### NewDPOAlignmentConfig

`func NewDPOAlignmentConfig(rewardScale float32, rewardClip float32, epsilon float32, gamma float32, ) *DPOAlignmentConfig`

NewDPOAlignmentConfig instantiates a new DPOAlignmentConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDPOAlignmentConfigWithDefaults

`func NewDPOAlignmentConfigWithDefaults() *DPOAlignmentConfig`

NewDPOAlignmentConfigWithDefaults instantiates a new DPOAlignmentConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRewardScale

`func (o *DPOAlignmentConfig) GetRewardScale() float32`

GetRewardScale returns the RewardScale field if non-nil, zero value otherwise.

### GetRewardScaleOk

`func (o *DPOAlignmentConfig) GetRewardScaleOk() (*float32, bool)`

GetRewardScaleOk returns a tuple with the RewardScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRewardScale

`func (o *DPOAlignmentConfig) SetRewardScale(v float32)`

SetRewardScale sets RewardScale field to given value.


### GetRewardClip

`func (o *DPOAlignmentConfig) GetRewardClip() float32`

GetRewardClip returns the RewardClip field if non-nil, zero value otherwise.

### GetRewardClipOk

`func (o *DPOAlignmentConfig) GetRewardClipOk() (*float32, bool)`

GetRewardClipOk returns a tuple with the RewardClip field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRewardClip

`func (o *DPOAlignmentConfig) SetRewardClip(v float32)`

SetRewardClip sets RewardClip field to given value.


### GetEpsilon

`func (o *DPOAlignmentConfig) GetEpsilon() float32`

GetEpsilon returns the Epsilon field if non-nil, zero value otherwise.

### GetEpsilonOk

`func (o *DPOAlignmentConfig) GetEpsilonOk() (*float32, bool)`

GetEpsilonOk returns a tuple with the Epsilon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEpsilon

`func (o *DPOAlignmentConfig) SetEpsilon(v float32)`

SetEpsilon sets Epsilon field to given value.


### GetGamma

`func (o *DPOAlignmentConfig) GetGamma() float32`

GetGamma returns the Gamma field if non-nil, zero value otherwise.

### GetGammaOk

`func (o *DPOAlignmentConfig) GetGammaOk() (*float32, bool)`

GetGammaOk returns a tuple with the Gamma field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGamma

`func (o *DPOAlignmentConfig) SetGamma(v float32)`

SetGamma sets Gamma field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


