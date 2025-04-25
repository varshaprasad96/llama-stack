# OpenAIResponseFormatJSONSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "json_schema"]
**JsonSchema** | [**OpenAIJSONSchema**](OpenAIJSONSchema.md) |  | 

## Methods

### NewOpenAIResponseFormatJSONSchema

`func NewOpenAIResponseFormatJSONSchema(type_ string, jsonSchema OpenAIJSONSchema, ) *OpenAIResponseFormatJSONSchema`

NewOpenAIResponseFormatJSONSchema instantiates a new OpenAIResponseFormatJSONSchema object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIResponseFormatJSONSchemaWithDefaults

`func NewOpenAIResponseFormatJSONSchemaWithDefaults() *OpenAIResponseFormatJSONSchema`

NewOpenAIResponseFormatJSONSchemaWithDefaults instantiates a new OpenAIResponseFormatJSONSchema object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *OpenAIResponseFormatJSONSchema) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *OpenAIResponseFormatJSONSchema) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *OpenAIResponseFormatJSONSchema) SetType(v string)`

SetType sets Type field to given value.


### GetJsonSchema

`func (o *OpenAIResponseFormatJSONSchema) GetJsonSchema() OpenAIJSONSchema`

GetJsonSchema returns the JsonSchema field if non-nil, zero value otherwise.

### GetJsonSchemaOk

`func (o *OpenAIResponseFormatJSONSchema) GetJsonSchemaOk() (*OpenAIJSONSchema, bool)`

GetJsonSchemaOk returns a tuple with the JsonSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJsonSchema

`func (o *OpenAIResponseFormatJSONSchema) SetJsonSchema(v OpenAIJSONSchema)`

SetJsonSchema sets JsonSchema field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


