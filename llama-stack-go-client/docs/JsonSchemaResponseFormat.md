# JsonSchemaResponseFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Must be \&quot;json_schema\&quot; to identify this format type | [default to "json_schema"]
**JsonSchema** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | The JSON schema the response should conform to. In a Python SDK, this is often a &#x60;pydantic&#x60; model. | 

## Methods

### NewJsonSchemaResponseFormat

`func NewJsonSchemaResponseFormat(type_ string, jsonSchema map[string]AppendRowsRequestRowsInnerValue, ) *JsonSchemaResponseFormat`

NewJsonSchemaResponseFormat instantiates a new JsonSchemaResponseFormat object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewJsonSchemaResponseFormatWithDefaults

`func NewJsonSchemaResponseFormatWithDefaults() *JsonSchemaResponseFormat`

NewJsonSchemaResponseFormatWithDefaults instantiates a new JsonSchemaResponseFormat object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *JsonSchemaResponseFormat) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *JsonSchemaResponseFormat) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *JsonSchemaResponseFormat) SetType(v string)`

SetType sets Type field to given value.


### GetJsonSchema

`func (o *JsonSchemaResponseFormat) GetJsonSchema() map[string]AppendRowsRequestRowsInnerValue`

GetJsonSchema returns the JsonSchema field if non-nil, zero value otherwise.

### GetJsonSchemaOk

`func (o *JsonSchemaResponseFormat) GetJsonSchemaOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetJsonSchemaOk returns a tuple with the JsonSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJsonSchema

`func (o *JsonSchemaResponseFormat) SetJsonSchema(v map[string]AppendRowsRequestRowsInnerValue)`

SetJsonSchema sets JsonSchema field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


