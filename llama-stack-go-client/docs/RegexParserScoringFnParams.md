# RegexParserScoringFnParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "regex_parser"]
**ParsingRegexes** | Pointer to **[]string** |  | [optional] 
**AggregationFunctions** | Pointer to [**[]AggregationFunctionType**](AggregationFunctionType.md) |  | [optional] 

## Methods

### NewRegexParserScoringFnParams

`func NewRegexParserScoringFnParams(type_ string, ) *RegexParserScoringFnParams`

NewRegexParserScoringFnParams instantiates a new RegexParserScoringFnParams object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegexParserScoringFnParamsWithDefaults

`func NewRegexParserScoringFnParamsWithDefaults() *RegexParserScoringFnParams`

NewRegexParserScoringFnParamsWithDefaults instantiates a new RegexParserScoringFnParams object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *RegexParserScoringFnParams) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RegexParserScoringFnParams) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RegexParserScoringFnParams) SetType(v string)`

SetType sets Type field to given value.


### GetParsingRegexes

`func (o *RegexParserScoringFnParams) GetParsingRegexes() []string`

GetParsingRegexes returns the ParsingRegexes field if non-nil, zero value otherwise.

### GetParsingRegexesOk

`func (o *RegexParserScoringFnParams) GetParsingRegexesOk() (*[]string, bool)`

GetParsingRegexesOk returns a tuple with the ParsingRegexes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParsingRegexes

`func (o *RegexParserScoringFnParams) SetParsingRegexes(v []string)`

SetParsingRegexes sets ParsingRegexes field to given value.

### HasParsingRegexes

`func (o *RegexParserScoringFnParams) HasParsingRegexes() bool`

HasParsingRegexes returns a boolean if a field has been set.

### GetAggregationFunctions

`func (o *RegexParserScoringFnParams) GetAggregationFunctions() []AggregationFunctionType`

GetAggregationFunctions returns the AggregationFunctions field if non-nil, zero value otherwise.

### GetAggregationFunctionsOk

`func (o *RegexParserScoringFnParams) GetAggregationFunctionsOk() (*[]AggregationFunctionType, bool)`

GetAggregationFunctionsOk returns a tuple with the AggregationFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAggregationFunctions

`func (o *RegexParserScoringFnParams) SetAggregationFunctions(v []AggregationFunctionType)`

SetAggregationFunctions sets AggregationFunctions field to given value.

### HasAggregationFunctions

`func (o *RegexParserScoringFnParams) HasAggregationFunctions() bool`

HasAggregationFunctions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


