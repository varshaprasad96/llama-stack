# InvokeToolRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ToolName** | **string** |  | 
**Kwargs** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewInvokeToolRequest

`func NewInvokeToolRequest(toolName string, kwargs map[string]AppendRowsRequestRowsInnerValue, ) *InvokeToolRequest`

NewInvokeToolRequest instantiates a new InvokeToolRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInvokeToolRequestWithDefaults

`func NewInvokeToolRequestWithDefaults() *InvokeToolRequest`

NewInvokeToolRequestWithDefaults instantiates a new InvokeToolRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetToolName

`func (o *InvokeToolRequest) GetToolName() string`

GetToolName returns the ToolName field if non-nil, zero value otherwise.

### GetToolNameOk

`func (o *InvokeToolRequest) GetToolNameOk() (*string, bool)`

GetToolNameOk returns a tuple with the ToolName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolName

`func (o *InvokeToolRequest) SetToolName(v string)`

SetToolName sets ToolName field to given value.


### GetKwargs

`func (o *InvokeToolRequest) GetKwargs() map[string]AppendRowsRequestRowsInnerValue`

GetKwargs returns the Kwargs field if non-nil, zero value otherwise.

### GetKwargsOk

`func (o *InvokeToolRequest) GetKwargsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetKwargsOk returns a tuple with the Kwargs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKwargs

`func (o *InvokeToolRequest) SetKwargs(v map[string]AppendRowsRequestRowsInnerValue)`

SetKwargs sets Kwargs field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


