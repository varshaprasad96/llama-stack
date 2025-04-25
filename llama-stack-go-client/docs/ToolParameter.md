# ToolParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**ParameterType** | **string** |  | 
**Description** | **string** |  | 
**Required** | **bool** |  | [default to true]
**Default** | Pointer to [**NullableAppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewToolParameter

`func NewToolParameter(name string, parameterType string, description string, required bool, ) *ToolParameter`

NewToolParameter instantiates a new ToolParameter object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolParameterWithDefaults

`func NewToolParameterWithDefaults() *ToolParameter`

NewToolParameterWithDefaults instantiates a new ToolParameter object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ToolParameter) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ToolParameter) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ToolParameter) SetName(v string)`

SetName sets Name field to given value.


### GetParameterType

`func (o *ToolParameter) GetParameterType() string`

GetParameterType returns the ParameterType field if non-nil, zero value otherwise.

### GetParameterTypeOk

`func (o *ToolParameter) GetParameterTypeOk() (*string, bool)`

GetParameterTypeOk returns a tuple with the ParameterType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParameterType

`func (o *ToolParameter) SetParameterType(v string)`

SetParameterType sets ParameterType field to given value.


### GetDescription

`func (o *ToolParameter) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ToolParameter) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ToolParameter) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetRequired

`func (o *ToolParameter) GetRequired() bool`

GetRequired returns the Required field if non-nil, zero value otherwise.

### GetRequiredOk

`func (o *ToolParameter) GetRequiredOk() (*bool, bool)`

GetRequiredOk returns a tuple with the Required field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequired

`func (o *ToolParameter) SetRequired(v bool)`

SetRequired sets Required field to given value.


### GetDefault

`func (o *ToolParameter) GetDefault() AppendRowsRequestRowsInnerValue`

GetDefault returns the Default field if non-nil, zero value otherwise.

### GetDefaultOk

`func (o *ToolParameter) GetDefaultOk() (*AppendRowsRequestRowsInnerValue, bool)`

GetDefaultOk returns a tuple with the Default field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefault

`func (o *ToolParameter) SetDefault(v AppendRowsRequestRowsInnerValue)`

SetDefault sets Default field to given value.

### HasDefault

`func (o *ToolParameter) HasDefault() bool`

HasDefault returns a boolean if a field has been set.

### SetDefaultNil

`func (o *ToolParameter) SetDefaultNil(b bool)`

 SetDefaultNil sets the value for Default to be an explicit nil

### UnsetDefault
`func (o *ToolParameter) UnsetDefault()`

UnsetDefault ensures that no value is present for Default, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


