# RAGQueryGeneratorConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "default"]
**Separator** | **string** |  | [default to " "]
**Model** | **string** |  | 
**Template** | **string** |  | 

## Methods

### NewRAGQueryGeneratorConfig

`func NewRAGQueryGeneratorConfig(type_ string, separator string, model string, template string, ) *RAGQueryGeneratorConfig`

NewRAGQueryGeneratorConfig instantiates a new RAGQueryGeneratorConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRAGQueryGeneratorConfigWithDefaults

`func NewRAGQueryGeneratorConfigWithDefaults() *RAGQueryGeneratorConfig`

NewRAGQueryGeneratorConfigWithDefaults instantiates a new RAGQueryGeneratorConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *RAGQueryGeneratorConfig) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RAGQueryGeneratorConfig) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RAGQueryGeneratorConfig) SetType(v string)`

SetType sets Type field to given value.


### GetSeparator

`func (o *RAGQueryGeneratorConfig) GetSeparator() string`

GetSeparator returns the Separator field if non-nil, zero value otherwise.

### GetSeparatorOk

`func (o *RAGQueryGeneratorConfig) GetSeparatorOk() (*string, bool)`

GetSeparatorOk returns a tuple with the Separator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeparator

`func (o *RAGQueryGeneratorConfig) SetSeparator(v string)`

SetSeparator sets Separator field to given value.


### GetModel

`func (o *RAGQueryGeneratorConfig) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *RAGQueryGeneratorConfig) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *RAGQueryGeneratorConfig) SetModel(v string)`

SetModel sets Model field to given value.


### GetTemplate

`func (o *RAGQueryGeneratorConfig) GetTemplate() string`

GetTemplate returns the Template field if non-nil, zero value otherwise.

### GetTemplateOk

`func (o *RAGQueryGeneratorConfig) GetTemplateOk() (*string, bool)`

GetTemplateOk returns a tuple with the Template field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTemplate

`func (o *RAGQueryGeneratorConfig) SetTemplate(v string)`

SetTemplate sets Template field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


