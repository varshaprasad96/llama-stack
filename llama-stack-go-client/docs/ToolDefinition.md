# ToolDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ToolName** | [**ToolCallToolName**](ToolCallToolName.md) |  | 
**Description** | Pointer to **string** |  | [optional] 
**Parameters** | Pointer to [**map[string]ToolParamDefinition**](ToolParamDefinition.md) |  | [optional] 

## Methods

### NewToolDefinition

`func NewToolDefinition(toolName ToolCallToolName, ) *ToolDefinition`

NewToolDefinition instantiates a new ToolDefinition object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolDefinitionWithDefaults

`func NewToolDefinitionWithDefaults() *ToolDefinition`

NewToolDefinitionWithDefaults instantiates a new ToolDefinition object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetToolName

`func (o *ToolDefinition) GetToolName() ToolCallToolName`

GetToolName returns the ToolName field if non-nil, zero value otherwise.

### GetToolNameOk

`func (o *ToolDefinition) GetToolNameOk() (*ToolCallToolName, bool)`

GetToolNameOk returns a tuple with the ToolName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolName

`func (o *ToolDefinition) SetToolName(v ToolCallToolName)`

SetToolName sets ToolName field to given value.


### GetDescription

`func (o *ToolDefinition) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ToolDefinition) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ToolDefinition) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ToolDefinition) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetParameters

`func (o *ToolDefinition) GetParameters() map[string]ToolParamDefinition`

GetParameters returns the Parameters field if non-nil, zero value otherwise.

### GetParametersOk

`func (o *ToolDefinition) GetParametersOk() (*map[string]ToolParamDefinition, bool)`

GetParametersOk returns a tuple with the Parameters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParameters

`func (o *ToolDefinition) SetParameters(v map[string]ToolParamDefinition)`

SetParameters sets Parameters field to given value.

### HasParameters

`func (o *ToolDefinition) HasParameters() bool`

HasParameters returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


