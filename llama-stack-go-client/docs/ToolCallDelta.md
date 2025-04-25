# ToolCallDelta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "tool_call"]
**ToolCall** | [**ToolCallDeltaToolCall**](ToolCallDeltaToolCall.md) |  | 
**ParseStatus** | **string** |  | 

## Methods

### NewToolCallDelta

`func NewToolCallDelta(type_ string, toolCall ToolCallDeltaToolCall, parseStatus string, ) *ToolCallDelta`

NewToolCallDelta instantiates a new ToolCallDelta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolCallDeltaWithDefaults

`func NewToolCallDeltaWithDefaults() *ToolCallDelta`

NewToolCallDeltaWithDefaults instantiates a new ToolCallDelta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *ToolCallDelta) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ToolCallDelta) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ToolCallDelta) SetType(v string)`

SetType sets Type field to given value.


### GetToolCall

`func (o *ToolCallDelta) GetToolCall() ToolCallDeltaToolCall`

GetToolCall returns the ToolCall field if non-nil, zero value otherwise.

### GetToolCallOk

`func (o *ToolCallDelta) GetToolCallOk() (*ToolCallDeltaToolCall, bool)`

GetToolCallOk returns a tuple with the ToolCall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCall

`func (o *ToolCallDelta) SetToolCall(v ToolCallDeltaToolCall)`

SetToolCall sets ToolCall field to given value.


### GetParseStatus

`func (o *ToolCallDelta) GetParseStatus() string`

GetParseStatus returns the ParseStatus field if non-nil, zero value otherwise.

### GetParseStatusOk

`func (o *ToolCallDelta) GetParseStatusOk() (*string, bool)`

GetParseStatusOk returns a tuple with the ParseStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParseStatus

`func (o *ToolCallDelta) SetParseStatus(v string)`

SetParseStatus sets ParseStatus field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


