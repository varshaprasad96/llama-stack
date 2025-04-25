# ResponseFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Must be \&quot;json_schema\&quot; to identify this format type | [default to "json_schema"]
**JsonSchema** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | The JSON schema the response should conform to. In a Python SDK, this is often a &#x60;pydantic&#x60; model. | 
**Bnf** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | The BNF grammar specification the response should conform to | 

## Methods

### NewResponseFormat

`func NewResponseFormat(type_ string, jsonSchema map[string]AppendRowsRequestRowsInnerValue, bnf map[string]AppendRowsRequestRowsInnerValue, ) *ResponseFormat`

NewResponseFormat instantiates a new ResponseFormat object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewResponseFormatWithDefaults

`func NewResponseFormatWithDefaults() *ResponseFormat`

NewResponseFormatWithDefaults instantiates a new ResponseFormat object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *ResponseFormat) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ResponseFormat) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ResponseFormat) SetType(v string)`

SetType sets Type field to given value.


### GetJsonSchema

`func (o *ResponseFormat) GetJsonSchema() map[string]AppendRowsRequestRowsInnerValue`

GetJsonSchema returns the JsonSchema field if non-nil, zero value otherwise.

### GetJsonSchemaOk

`func (o *ResponseFormat) GetJsonSchemaOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetJsonSchemaOk returns a tuple with the JsonSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJsonSchema

`func (o *ResponseFormat) SetJsonSchema(v map[string]AppendRowsRequestRowsInnerValue)`

SetJsonSchema sets JsonSchema field to given value.


### GetBnf

`func (o *ResponseFormat) GetBnf() map[string]AppendRowsRequestRowsInnerValue`

GetBnf returns the Bnf field if non-nil, zero value otherwise.

### GetBnfOk

`func (o *ResponseFormat) GetBnfOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetBnfOk returns a tuple with the Bnf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBnf

`func (o *ResponseFormat) SetBnf(v map[string]AppendRowsRequestRowsInnerValue)`

SetBnf sets Bnf field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


