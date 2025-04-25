# OpenAIJSONSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Description** | Pointer to **string** |  | [optional] 
**Strict** | Pointer to **bool** |  | [optional] 
**Schema** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewOpenAIJSONSchema

`func NewOpenAIJSONSchema(name string, ) *OpenAIJSONSchema`

NewOpenAIJSONSchema instantiates a new OpenAIJSONSchema object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIJSONSchemaWithDefaults

`func NewOpenAIJSONSchemaWithDefaults() *OpenAIJSONSchema`

NewOpenAIJSONSchemaWithDefaults instantiates a new OpenAIJSONSchema object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *OpenAIJSONSchema) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *OpenAIJSONSchema) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *OpenAIJSONSchema) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *OpenAIJSONSchema) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *OpenAIJSONSchema) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *OpenAIJSONSchema) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *OpenAIJSONSchema) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetStrict

`func (o *OpenAIJSONSchema) GetStrict() bool`

GetStrict returns the Strict field if non-nil, zero value otherwise.

### GetStrictOk

`func (o *OpenAIJSONSchema) GetStrictOk() (*bool, bool)`

GetStrictOk returns a tuple with the Strict field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStrict

`func (o *OpenAIJSONSchema) SetStrict(v bool)`

SetStrict sets Strict field to given value.

### HasStrict

`func (o *OpenAIJSONSchema) HasStrict() bool`

HasStrict returns a boolean if a field has been set.

### GetSchema

`func (o *OpenAIJSONSchema) GetSchema() map[string]AppendRowsRequestRowsInnerValue`

GetSchema returns the Schema field if non-nil, zero value otherwise.

### GetSchemaOk

`func (o *OpenAIJSONSchema) GetSchemaOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetSchemaOk returns a tuple with the Schema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSchema

`func (o *OpenAIJSONSchema) SetSchema(v map[string]AppendRowsRequestRowsInnerValue)`

SetSchema sets Schema field to given value.

### HasSchema

`func (o *OpenAIJSONSchema) HasSchema() bool`

HasSchema returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


