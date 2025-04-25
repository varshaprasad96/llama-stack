# ToolInvocationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | Pointer to [**InterleavedContent**](InterleavedContent.md) |  | [optional] 
**ErrorMessage** | Pointer to **string** |  | [optional] 
**ErrorCode** | Pointer to **int32** |  | [optional] 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewToolInvocationResult

`func NewToolInvocationResult() *ToolInvocationResult`

NewToolInvocationResult instantiates a new ToolInvocationResult object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolInvocationResultWithDefaults

`func NewToolInvocationResultWithDefaults() *ToolInvocationResult`

NewToolInvocationResultWithDefaults instantiates a new ToolInvocationResult object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *ToolInvocationResult) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *ToolInvocationResult) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *ToolInvocationResult) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.

### HasContent

`func (o *ToolInvocationResult) HasContent() bool`

HasContent returns a boolean if a field has been set.

### GetErrorMessage

`func (o *ToolInvocationResult) GetErrorMessage() string`

GetErrorMessage returns the ErrorMessage field if non-nil, zero value otherwise.

### GetErrorMessageOk

`func (o *ToolInvocationResult) GetErrorMessageOk() (*string, bool)`

GetErrorMessageOk returns a tuple with the ErrorMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorMessage

`func (o *ToolInvocationResult) SetErrorMessage(v string)`

SetErrorMessage sets ErrorMessage field to given value.

### HasErrorMessage

`func (o *ToolInvocationResult) HasErrorMessage() bool`

HasErrorMessage returns a boolean if a field has been set.

### GetErrorCode

`func (o *ToolInvocationResult) GetErrorCode() int32`

GetErrorCode returns the ErrorCode field if non-nil, zero value otherwise.

### GetErrorCodeOk

`func (o *ToolInvocationResult) GetErrorCodeOk() (*int32, bool)`

GetErrorCodeOk returns a tuple with the ErrorCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorCode

`func (o *ToolInvocationResult) SetErrorCode(v int32)`

SetErrorCode sets ErrorCode field to given value.

### HasErrorCode

`func (o *ToolInvocationResult) HasErrorCode() bool`

HasErrorCode returns a boolean if a field has been set.

### GetMetadata

`func (o *ToolInvocationResult) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ToolInvocationResult) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ToolInvocationResult) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ToolInvocationResult) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


