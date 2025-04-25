# ScoringFnParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "llm_as_judge"]
**JudgeModel** | **string** |  | 
**PromptTemplate** | Pointer to **string** |  | [optional] 
**JudgeScoreRegexes** | Pointer to **[]string** |  | [optional] 
**AggregationFunctions** | Pointer to [**[]AggregationFunctionType**](AggregationFunctionType.md) |  | [optional] 
**ParsingRegexes** | Pointer to **[]string** |  | [optional] 

## Methods

### NewScoringFnParams

`func NewScoringFnParams(type_ string, judgeModel string, ) *ScoringFnParams`

NewScoringFnParams instantiates a new ScoringFnParams object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewScoringFnParamsWithDefaults

`func NewScoringFnParamsWithDefaults() *ScoringFnParams`

NewScoringFnParamsWithDefaults instantiates a new ScoringFnParams object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *ScoringFnParams) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ScoringFnParams) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ScoringFnParams) SetType(v string)`

SetType sets Type field to given value.


### GetJudgeModel

`func (o *ScoringFnParams) GetJudgeModel() string`

GetJudgeModel returns the JudgeModel field if non-nil, zero value otherwise.

### GetJudgeModelOk

`func (o *ScoringFnParams) GetJudgeModelOk() (*string, bool)`

GetJudgeModelOk returns a tuple with the JudgeModel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJudgeModel

`func (o *ScoringFnParams) SetJudgeModel(v string)`

SetJudgeModel sets JudgeModel field to given value.


### GetPromptTemplate

`func (o *ScoringFnParams) GetPromptTemplate() string`

GetPromptTemplate returns the PromptTemplate field if non-nil, zero value otherwise.

### GetPromptTemplateOk

`func (o *ScoringFnParams) GetPromptTemplateOk() (*string, bool)`

GetPromptTemplateOk returns a tuple with the PromptTemplate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromptTemplate

`func (o *ScoringFnParams) SetPromptTemplate(v string)`

SetPromptTemplate sets PromptTemplate field to given value.

### HasPromptTemplate

`func (o *ScoringFnParams) HasPromptTemplate() bool`

HasPromptTemplate returns a boolean if a field has been set.

### GetJudgeScoreRegexes

`func (o *ScoringFnParams) GetJudgeScoreRegexes() []string`

GetJudgeScoreRegexes returns the JudgeScoreRegexes field if non-nil, zero value otherwise.

### GetJudgeScoreRegexesOk

`func (o *ScoringFnParams) GetJudgeScoreRegexesOk() (*[]string, bool)`

GetJudgeScoreRegexesOk returns a tuple with the JudgeScoreRegexes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJudgeScoreRegexes

`func (o *ScoringFnParams) SetJudgeScoreRegexes(v []string)`

SetJudgeScoreRegexes sets JudgeScoreRegexes field to given value.

### HasJudgeScoreRegexes

`func (o *ScoringFnParams) HasJudgeScoreRegexes() bool`

HasJudgeScoreRegexes returns a boolean if a field has been set.

### GetAggregationFunctions

`func (o *ScoringFnParams) GetAggregationFunctions() []AggregationFunctionType`

GetAggregationFunctions returns the AggregationFunctions field if non-nil, zero value otherwise.

### GetAggregationFunctionsOk

`func (o *ScoringFnParams) GetAggregationFunctionsOk() (*[]AggregationFunctionType, bool)`

GetAggregationFunctionsOk returns a tuple with the AggregationFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAggregationFunctions

`func (o *ScoringFnParams) SetAggregationFunctions(v []AggregationFunctionType)`

SetAggregationFunctions sets AggregationFunctions field to given value.

### HasAggregationFunctions

`func (o *ScoringFnParams) HasAggregationFunctions() bool`

HasAggregationFunctions returns a boolean if a field has been set.

### GetParsingRegexes

`func (o *ScoringFnParams) GetParsingRegexes() []string`

GetParsingRegexes returns the ParsingRegexes field if non-nil, zero value otherwise.

### GetParsingRegexesOk

`func (o *ScoringFnParams) GetParsingRegexesOk() (*[]string, bool)`

GetParsingRegexesOk returns a tuple with the ParsingRegexes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParsingRegexes

`func (o *ScoringFnParams) SetParsingRegexes(v []string)`

SetParsingRegexes sets ParsingRegexes field to given value.

### HasParsingRegexes

`func (o *ScoringFnParams) HasParsingRegexes() bool`

HasParsingRegexes returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


