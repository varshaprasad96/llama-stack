# ToolDef

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Parameters** | Pointer to [**[]ToolParameter**](ToolParameter.md) |  | [optional] 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewToolDef

`func NewToolDef(name string, ) *ToolDef`

NewToolDef instantiates a new ToolDef object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolDefWithDefaults

`func NewToolDefWithDefaults() *ToolDef`

NewToolDefWithDefaults instantiates a new ToolDef object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ToolDef) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ToolDef) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ToolDef) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ToolDef) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ToolDef) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ToolDef) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ToolDef) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetParameters

`func (o *ToolDef) GetParameters() []ToolParameter`

GetParameters returns the Parameters field if non-nil, zero value otherwise.

### GetParametersOk

`func (o *ToolDef) GetParametersOk() (*[]ToolParameter, bool)`

GetParametersOk returns a tuple with the Parameters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParameters

`func (o *ToolDef) SetParameters(v []ToolParameter)`

SetParameters sets Parameters field to given value.

### HasParameters

`func (o *ToolDef) HasParameters() bool`

HasParameters returns a boolean if a field has been set.

### GetMetadata

`func (o *ToolDef) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ToolDef) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ToolDef) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ToolDef) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


