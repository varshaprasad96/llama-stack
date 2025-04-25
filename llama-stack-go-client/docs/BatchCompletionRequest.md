# BatchCompletionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ModelId** | **string** |  | 
**ContentBatch** | [**[]InterleavedContent**](InterleavedContent.md) |  | 
**SamplingParams** | Pointer to [**SamplingParams**](SamplingParams.md) |  | [optional] 
**ResponseFormat** | Pointer to [**ResponseFormat**](ResponseFormat.md) |  | [optional] 
**Logprobs** | Pointer to [**LogProbConfig**](LogProbConfig.md) |  | [optional] 

## Methods

### NewBatchCompletionRequest

`func NewBatchCompletionRequest(modelId string, contentBatch []InterleavedContent, ) *BatchCompletionRequest`

NewBatchCompletionRequest instantiates a new BatchCompletionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchCompletionRequestWithDefaults

`func NewBatchCompletionRequestWithDefaults() *BatchCompletionRequest`

NewBatchCompletionRequestWithDefaults instantiates a new BatchCompletionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModelId

`func (o *BatchCompletionRequest) GetModelId() string`

GetModelId returns the ModelId field if non-nil, zero value otherwise.

### GetModelIdOk

`func (o *BatchCompletionRequest) GetModelIdOk() (*string, bool)`

GetModelIdOk returns a tuple with the ModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelId

`func (o *BatchCompletionRequest) SetModelId(v string)`

SetModelId sets ModelId field to given value.


### GetContentBatch

`func (o *BatchCompletionRequest) GetContentBatch() []InterleavedContent`

GetContentBatch returns the ContentBatch field if non-nil, zero value otherwise.

### GetContentBatchOk

`func (o *BatchCompletionRequest) GetContentBatchOk() (*[]InterleavedContent, bool)`

GetContentBatchOk returns a tuple with the ContentBatch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentBatch

`func (o *BatchCompletionRequest) SetContentBatch(v []InterleavedContent)`

SetContentBatch sets ContentBatch field to given value.


### GetSamplingParams

`func (o *BatchCompletionRequest) GetSamplingParams() SamplingParams`

GetSamplingParams returns the SamplingParams field if non-nil, zero value otherwise.

### GetSamplingParamsOk

`func (o *BatchCompletionRequest) GetSamplingParamsOk() (*SamplingParams, bool)`

GetSamplingParamsOk returns a tuple with the SamplingParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamplingParams

`func (o *BatchCompletionRequest) SetSamplingParams(v SamplingParams)`

SetSamplingParams sets SamplingParams field to given value.

### HasSamplingParams

`func (o *BatchCompletionRequest) HasSamplingParams() bool`

HasSamplingParams returns a boolean if a field has been set.

### GetResponseFormat

`func (o *BatchCompletionRequest) GetResponseFormat() ResponseFormat`

GetResponseFormat returns the ResponseFormat field if non-nil, zero value otherwise.

### GetResponseFormatOk

`func (o *BatchCompletionRequest) GetResponseFormatOk() (*ResponseFormat, bool)`

GetResponseFormatOk returns a tuple with the ResponseFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseFormat

`func (o *BatchCompletionRequest) SetResponseFormat(v ResponseFormat)`

SetResponseFormat sets ResponseFormat field to given value.

### HasResponseFormat

`func (o *BatchCompletionRequest) HasResponseFormat() bool`

HasResponseFormat returns a boolean if a field has been set.

### GetLogprobs

`func (o *BatchCompletionRequest) GetLogprobs() LogProbConfig`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *BatchCompletionRequest) GetLogprobsOk() (*LogProbConfig, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *BatchCompletionRequest) SetLogprobs(v LogProbConfig)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *BatchCompletionRequest) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


