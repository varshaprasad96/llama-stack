# GrammarResponseFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Must be \&quot;grammar\&quot; to identify this format type | [default to "grammar"]
**Bnf** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | The BNF grammar specification the response should conform to | 

## Methods

### NewGrammarResponseFormat

`func NewGrammarResponseFormat(type_ string, bnf map[string]AppendRowsRequestRowsInnerValue, ) *GrammarResponseFormat`

NewGrammarResponseFormat instantiates a new GrammarResponseFormat object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGrammarResponseFormatWithDefaults

`func NewGrammarResponseFormatWithDefaults() *GrammarResponseFormat`

NewGrammarResponseFormatWithDefaults instantiates a new GrammarResponseFormat object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *GrammarResponseFormat) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *GrammarResponseFormat) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *GrammarResponseFormat) SetType(v string)`

SetType sets Type field to given value.


### GetBnf

`func (o *GrammarResponseFormat) GetBnf() map[string]AppendRowsRequestRowsInnerValue`

GetBnf returns the Bnf field if non-nil, zero value otherwise.

### GetBnfOk

`func (o *GrammarResponseFormat) GetBnfOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetBnfOk returns a tuple with the Bnf field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBnf

`func (o *GrammarResponseFormat) SetBnf(v map[string]AppendRowsRequestRowsInnerValue)`

SetBnf sets Bnf field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


