# ToolCallDeltaToolCall

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CallId** | **string** |  | 
**ToolName** | [**ToolCallToolName**](ToolCallToolName.md) |  | 
**Arguments** | [**ToolCallArguments**](ToolCallArguments.md) |  | 
**ArgumentsJson** | Pointer to **string** |  | [optional] 

## Methods

### NewToolCallDeltaToolCall

`func NewToolCallDeltaToolCall(callId string, toolName ToolCallToolName, arguments ToolCallArguments, ) *ToolCallDeltaToolCall`

NewToolCallDeltaToolCall instantiates a new ToolCallDeltaToolCall object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolCallDeltaToolCallWithDefaults

`func NewToolCallDeltaToolCallWithDefaults() *ToolCallDeltaToolCall`

NewToolCallDeltaToolCallWithDefaults instantiates a new ToolCallDeltaToolCall object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCallId

`func (o *ToolCallDeltaToolCall) GetCallId() string`

GetCallId returns the CallId field if non-nil, zero value otherwise.

### GetCallIdOk

`func (o *ToolCallDeltaToolCall) GetCallIdOk() (*string, bool)`

GetCallIdOk returns a tuple with the CallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCallId

`func (o *ToolCallDeltaToolCall) SetCallId(v string)`

SetCallId sets CallId field to given value.


### GetToolName

`func (o *ToolCallDeltaToolCall) GetToolName() ToolCallToolName`

GetToolName returns the ToolName field if non-nil, zero value otherwise.

### GetToolNameOk

`func (o *ToolCallDeltaToolCall) GetToolNameOk() (*ToolCallToolName, bool)`

GetToolNameOk returns a tuple with the ToolName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolName

`func (o *ToolCallDeltaToolCall) SetToolName(v ToolCallToolName)`

SetToolName sets ToolName field to given value.


### GetArguments

`func (o *ToolCallDeltaToolCall) GetArguments() ToolCallArguments`

GetArguments returns the Arguments field if non-nil, zero value otherwise.

### GetArgumentsOk

`func (o *ToolCallDeltaToolCall) GetArgumentsOk() (*ToolCallArguments, bool)`

GetArgumentsOk returns a tuple with the Arguments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArguments

`func (o *ToolCallDeltaToolCall) SetArguments(v ToolCallArguments)`

SetArguments sets Arguments field to given value.


### GetArgumentsJson

`func (o *ToolCallDeltaToolCall) GetArgumentsJson() string`

GetArgumentsJson returns the ArgumentsJson field if non-nil, zero value otherwise.

### GetArgumentsJsonOk

`func (o *ToolCallDeltaToolCall) GetArgumentsJsonOk() (*string, bool)`

GetArgumentsJsonOk returns a tuple with the ArgumentsJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArgumentsJson

`func (o *ToolCallDeltaToolCall) SetArgumentsJson(v string)`

SetArgumentsJson sets ArgumentsJson field to given value.

### HasArgumentsJson

`func (o *ToolCallDeltaToolCall) HasArgumentsJson() bool`

HasArgumentsJson returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


