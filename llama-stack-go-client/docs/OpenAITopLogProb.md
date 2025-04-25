# OpenAITopLogProb

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Token** | **string** |  | 
**Bytes** | Pointer to **[]int32** |  | [optional] 
**Logprob** | **float32** |  | 

## Methods

### NewOpenAITopLogProb

`func NewOpenAITopLogProb(token string, logprob float32, ) *OpenAITopLogProb`

NewOpenAITopLogProb instantiates a new OpenAITopLogProb object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAITopLogProbWithDefaults

`func NewOpenAITopLogProbWithDefaults() *OpenAITopLogProb`

NewOpenAITopLogProbWithDefaults instantiates a new OpenAITopLogProb object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetToken

`func (o *OpenAITopLogProb) GetToken() string`

GetToken returns the Token field if non-nil, zero value otherwise.

### GetTokenOk

`func (o *OpenAITopLogProb) GetTokenOk() (*string, bool)`

GetTokenOk returns a tuple with the Token field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToken

`func (o *OpenAITopLogProb) SetToken(v string)`

SetToken sets Token field to given value.


### GetBytes

`func (o *OpenAITopLogProb) GetBytes() []int32`

GetBytes returns the Bytes field if non-nil, zero value otherwise.

### GetBytesOk

`func (o *OpenAITopLogProb) GetBytesOk() (*[]int32, bool)`

GetBytesOk returns a tuple with the Bytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBytes

`func (o *OpenAITopLogProb) SetBytes(v []int32)`

SetBytes sets Bytes field to given value.

### HasBytes

`func (o *OpenAITopLogProb) HasBytes() bool`

HasBytes returns a boolean if a field has been set.

### GetLogprob

`func (o *OpenAITopLogProb) GetLogprob() float32`

GetLogprob returns the Logprob field if non-nil, zero value otherwise.

### GetLogprobOk

`func (o *OpenAITopLogProb) GetLogprobOk() (*float32, bool)`

GetLogprobOk returns a tuple with the Logprob field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprob

`func (o *OpenAITopLogProb) SetLogprob(v float32)`

SetLogprob sets Logprob field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


