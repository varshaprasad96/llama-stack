# ToolCall

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CallId** | **string** |  | 
**ToolName** | [**ToolCallToolName**](ToolCallToolName.md) |  | 
**Arguments** | [**ToolCallArguments**](ToolCallArguments.md) |  | 
**ArgumentsJson** | Pointer to **string** |  | [optional] 

## Methods

### NewToolCall

`func NewToolCall(callId string, toolName ToolCallToolName, arguments ToolCallArguments, ) *ToolCall`

NewToolCall instantiates a new ToolCall object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolCallWithDefaults

`func NewToolCallWithDefaults() *ToolCall`

NewToolCallWithDefaults instantiates a new ToolCall object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCallId

`func (o *ToolCall) GetCallId() string`

GetCallId returns the CallId field if non-nil, zero value otherwise.

### GetCallIdOk

`func (o *ToolCall) GetCallIdOk() (*string, bool)`

GetCallIdOk returns a tuple with the CallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCallId

`func (o *ToolCall) SetCallId(v string)`

SetCallId sets CallId field to given value.


### GetToolName

`func (o *ToolCall) GetToolName() ToolCallToolName`

GetToolName returns the ToolName field if non-nil, zero value otherwise.

### GetToolNameOk

`func (o *ToolCall) GetToolNameOk() (*ToolCallToolName, bool)`

GetToolNameOk returns a tuple with the ToolName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolName

`func (o *ToolCall) SetToolName(v ToolCallToolName)`

SetToolName sets ToolName field to given value.


### GetArguments

`func (o *ToolCall) GetArguments() ToolCallArguments`

GetArguments returns the Arguments field if non-nil, zero value otherwise.

### GetArgumentsOk

`func (o *ToolCall) GetArgumentsOk() (*ToolCallArguments, bool)`

GetArgumentsOk returns a tuple with the Arguments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArguments

`func (o *ToolCall) SetArguments(v ToolCallArguments)`

SetArguments sets Arguments field to given value.


### GetArgumentsJson

`func (o *ToolCall) GetArgumentsJson() string`

GetArgumentsJson returns the ArgumentsJson field if non-nil, zero value otherwise.

### GetArgumentsJsonOk

`func (o *ToolCall) GetArgumentsJsonOk() (*string, bool)`

GetArgumentsJsonOk returns a tuple with the ArgumentsJson field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArgumentsJson

`func (o *ToolCall) SetArgumentsJson(v string)`

SetArgumentsJson sets ArgumentsJson field to given value.

### HasArgumentsJson

`func (o *ToolCall) HasArgumentsJson() bool`

HasArgumentsJson returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


