# OpenAIResponseFormatParam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "text"]
**JsonSchema** | [**OpenAIJSONSchema**](OpenAIJSONSchema.md) |  | 

## Methods

### NewOpenAIResponseFormatParam

`func NewOpenAIResponseFormatParam(type_ string, jsonSchema OpenAIJSONSchema, ) *OpenAIResponseFormatParam`

NewOpenAIResponseFormatParam instantiates a new OpenAIResponseFormatParam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIResponseFormatParamWithDefaults

`func NewOpenAIResponseFormatParamWithDefaults() *OpenAIResponseFormatParam`

NewOpenAIResponseFormatParamWithDefaults instantiates a new OpenAIResponseFormatParam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *OpenAIResponseFormatParam) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *OpenAIResponseFormatParam) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *OpenAIResponseFormatParam) SetType(v string)`

SetType sets Type field to given value.


### GetJsonSchema

`func (o *OpenAIResponseFormatParam) GetJsonSchema() OpenAIJSONSchema`

GetJsonSchema returns the JsonSchema field if non-nil, zero value otherwise.

### GetJsonSchemaOk

`func (o *OpenAIResponseFormatParam) GetJsonSchemaOk() (*OpenAIJSONSchema, bool)`

GetJsonSchemaOk returns a tuple with the JsonSchema field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJsonSchema

`func (o *OpenAIResponseFormatParam) SetJsonSchema(v OpenAIJSONSchema)`

SetJsonSchema sets JsonSchema field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


