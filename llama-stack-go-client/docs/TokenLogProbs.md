# TokenLogProbs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LogprobsByToken** | **map[string]float32** | Dictionary mapping tokens to their log probabilities | 

## Methods

### NewTokenLogProbs

`func NewTokenLogProbs(logprobsByToken map[string]float32, ) *TokenLogProbs`

NewTokenLogProbs instantiates a new TokenLogProbs object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTokenLogProbsWithDefaults

`func NewTokenLogProbsWithDefaults() *TokenLogProbs`

NewTokenLogProbsWithDefaults instantiates a new TokenLogProbs object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLogprobsByToken

`func (o *TokenLogProbs) GetLogprobsByToken() map[string]float32`

GetLogprobsByToken returns the LogprobsByToken field if non-nil, zero value otherwise.

### GetLogprobsByTokenOk

`func (o *TokenLogProbs) GetLogprobsByTokenOk() (*map[string]float32, bool)`

GetLogprobsByTokenOk returns a tuple with the LogprobsByToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobsByToken

`func (o *TokenLogProbs) SetLogprobsByToken(v map[string]float32)`

SetLogprobsByToken sets LogprobsByToken field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


