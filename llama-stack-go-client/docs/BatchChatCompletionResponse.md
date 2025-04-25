# BatchChatCompletionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Batch** | [**[]ChatCompletionResponse**](ChatCompletionResponse.md) |  | 

## Methods

### NewBatchChatCompletionResponse

`func NewBatchChatCompletionResponse(batch []ChatCompletionResponse, ) *BatchChatCompletionResponse`

NewBatchChatCompletionResponse instantiates a new BatchChatCompletionResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBatchChatCompletionResponseWithDefaults

`func NewBatchChatCompletionResponseWithDefaults() *BatchChatCompletionResponse`

NewBatchChatCompletionResponseWithDefaults instantiates a new BatchChatCompletionResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBatch

`func (o *BatchChatCompletionResponse) GetBatch() []ChatCompletionResponse`

GetBatch returns the Batch field if non-nil, zero value otherwise.

### GetBatchOk

`func (o *BatchChatCompletionResponse) GetBatchOk() (*[]ChatCompletionResponse, bool)`

GetBatchOk returns a tuple with the Batch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBatch

`func (o *BatchChatCompletionResponse) SetBatch(v []ChatCompletionResponse)`

SetBatch sets Batch field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


