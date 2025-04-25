# CompletionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ModelId** | **string** | The identifier of the model to use. The model must be registered with Llama Stack and available via the /models endpoint. | 
**Content** | [**InterleavedContent**](InterleavedContent.md) | The content to generate a completion for | 
**SamplingParams** | Pointer to [**SamplingParams**](SamplingParams.md) | (Optional) Parameters to control the sampling strategy | [optional] 
**ResponseFormat** | Pointer to [**ResponseFormat**](ResponseFormat.md) | (Optional) Grammar specification for guided (structured) decoding | [optional] 
**Stream** | Pointer to **bool** | (Optional) If True, generate an SSE event stream of the response. Defaults to False. | [optional] 
**Logprobs** | Pointer to [**ChatCompletionRequestLogprobs**](ChatCompletionRequestLogprobs.md) |  | [optional] 

## Methods

### NewCompletionRequest

`func NewCompletionRequest(modelId string, content InterleavedContent, ) *CompletionRequest`

NewCompletionRequest instantiates a new CompletionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCompletionRequestWithDefaults

`func NewCompletionRequestWithDefaults() *CompletionRequest`

NewCompletionRequestWithDefaults instantiates a new CompletionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetModelId

`func (o *CompletionRequest) GetModelId() string`

GetModelId returns the ModelId field if non-nil, zero value otherwise.

### GetModelIdOk

`func (o *CompletionRequest) GetModelIdOk() (*string, bool)`

GetModelIdOk returns a tuple with the ModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelId

`func (o *CompletionRequest) SetModelId(v string)`

SetModelId sets ModelId field to given value.


### GetContent

`func (o *CompletionRequest) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *CompletionRequest) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *CompletionRequest) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.


### GetSamplingParams

`func (o *CompletionRequest) GetSamplingParams() SamplingParams`

GetSamplingParams returns the SamplingParams field if non-nil, zero value otherwise.

### GetSamplingParamsOk

`func (o *CompletionRequest) GetSamplingParamsOk() (*SamplingParams, bool)`

GetSamplingParamsOk returns a tuple with the SamplingParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamplingParams

`func (o *CompletionRequest) SetSamplingParams(v SamplingParams)`

SetSamplingParams sets SamplingParams field to given value.

### HasSamplingParams

`func (o *CompletionRequest) HasSamplingParams() bool`

HasSamplingParams returns a boolean if a field has been set.

### GetResponseFormat

`func (o *CompletionRequest) GetResponseFormat() ResponseFormat`

GetResponseFormat returns the ResponseFormat field if non-nil, zero value otherwise.

### GetResponseFormatOk

`func (o *CompletionRequest) GetResponseFormatOk() (*ResponseFormat, bool)`

GetResponseFormatOk returns a tuple with the ResponseFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseFormat

`func (o *CompletionRequest) SetResponseFormat(v ResponseFormat)`

SetResponseFormat sets ResponseFormat field to given value.

### HasResponseFormat

`func (o *CompletionRequest) HasResponseFormat() bool`

HasResponseFormat returns a boolean if a field has been set.

### GetStream

`func (o *CompletionRequest) GetStream() bool`

GetStream returns the Stream field if non-nil, zero value otherwise.

### GetStreamOk

`func (o *CompletionRequest) GetStreamOk() (*bool, bool)`

GetStreamOk returns a tuple with the Stream field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStream

`func (o *CompletionRequest) SetStream(v bool)`

SetStream sets Stream field to given value.

### HasStream

`func (o *CompletionRequest) HasStream() bool`

HasStream returns a boolean if a field has been set.

### GetLogprobs

`func (o *CompletionRequest) GetLogprobs() ChatCompletionRequestLogprobs`

GetLogprobs returns the Logprobs field if non-nil, zero value otherwise.

### GetLogprobsOk

`func (o *CompletionRequest) GetLogprobsOk() (*ChatCompletionRequestLogprobs, bool)`

GetLogprobsOk returns a tuple with the Logprobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogprobs

`func (o *CompletionRequest) SetLogprobs(v ChatCompletionRequestLogprobs)`

SetLogprobs sets Logprobs field to given value.

### HasLogprobs

`func (o *CompletionRequest) HasLogprobs() bool`

HasLogprobs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


