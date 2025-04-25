# ToolParamDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ParamType** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Required** | Pointer to **bool** |  | [optional] [default to true]
**Default** | Pointer to [**NullableAppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewToolParamDefinition

`func NewToolParamDefinition(paramType string, ) *ToolParamDefinition`

NewToolParamDefinition instantiates a new ToolParamDefinition object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolParamDefinitionWithDefaults

`func NewToolParamDefinitionWithDefaults() *ToolParamDefinition`

NewToolParamDefinitionWithDefaults instantiates a new ToolParamDefinition object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetParamType

`func (o *ToolParamDefinition) GetParamType() string`

GetParamType returns the ParamType field if non-nil, zero value otherwise.

### GetParamTypeOk

`func (o *ToolParamDefinition) GetParamTypeOk() (*string, bool)`

GetParamTypeOk returns a tuple with the ParamType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParamType

`func (o *ToolParamDefinition) SetParamType(v string)`

SetParamType sets ParamType field to given value.


### GetDescription

`func (o *ToolParamDefinition) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ToolParamDefinition) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ToolParamDefinition) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ToolParamDefinition) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetRequired

`func (o *ToolParamDefinition) GetRequired() bool`

GetRequired returns the Required field if non-nil, zero value otherwise.

### GetRequiredOk

`func (o *ToolParamDefinition) GetRequiredOk() (*bool, bool)`

GetRequiredOk returns a tuple with the Required field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequired

`func (o *ToolParamDefinition) SetRequired(v bool)`

SetRequired sets Required field to given value.

### HasRequired

`func (o *ToolParamDefinition) HasRequired() bool`

HasRequired returns a boolean if a field has been set.

### GetDefault

`func (o *ToolParamDefinition) GetDefault() AppendRowsRequestRowsInnerValue`

GetDefault returns the Default field if non-nil, zero value otherwise.

### GetDefaultOk

`func (o *ToolParamDefinition) GetDefaultOk() (*AppendRowsRequestRowsInnerValue, bool)`

GetDefaultOk returns a tuple with the Default field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefault

`func (o *ToolParamDefinition) SetDefault(v AppendRowsRequestRowsInnerValue)`

SetDefault sets Default field to given value.

### HasDefault

`func (o *ToolParamDefinition) HasDefault() bool`

HasDefault returns a boolean if a field has been set.

### SetDefaultNil

`func (o *ToolParamDefinition) SetDefaultNil(b bool)`

 SetDefaultNil sets the value for Default to be an explicit nil

### UnsetDefault
`func (o *ToolParamDefinition) UnsetDefault()`

UnsetDefault ensures that no value is present for Default, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


