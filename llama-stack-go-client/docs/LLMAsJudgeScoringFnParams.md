# LLMAsJudgeScoringFnParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "llm_as_judge"]
**JudgeModel** | **string** |  | 
**PromptTemplate** | Pointer to **string** |  | [optional] 
**JudgeScoreRegexes** | Pointer to **[]string** |  | [optional] 
**AggregationFunctions** | Pointer to [**[]AggregationFunctionType**](AggregationFunctionType.md) |  | [optional] 

## Methods

### NewLLMAsJudgeScoringFnParams

`func NewLLMAsJudgeScoringFnParams(type_ string, judgeModel string, ) *LLMAsJudgeScoringFnParams`

NewLLMAsJudgeScoringFnParams instantiates a new LLMAsJudgeScoringFnParams object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLLMAsJudgeScoringFnParamsWithDefaults

`func NewLLMAsJudgeScoringFnParamsWithDefaults() *LLMAsJudgeScoringFnParams`

NewLLMAsJudgeScoringFnParamsWithDefaults instantiates a new LLMAsJudgeScoringFnParams object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *LLMAsJudgeScoringFnParams) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *LLMAsJudgeScoringFnParams) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *LLMAsJudgeScoringFnParams) SetType(v string)`

SetType sets Type field to given value.


### GetJudgeModel

`func (o *LLMAsJudgeScoringFnParams) GetJudgeModel() string`

GetJudgeModel returns the JudgeModel field if non-nil, zero value otherwise.

### GetJudgeModelOk

`func (o *LLMAsJudgeScoringFnParams) GetJudgeModelOk() (*string, bool)`

GetJudgeModelOk returns a tuple with the JudgeModel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJudgeModel

`func (o *LLMAsJudgeScoringFnParams) SetJudgeModel(v string)`

SetJudgeModel sets JudgeModel field to given value.


### GetPromptTemplate

`func (o *LLMAsJudgeScoringFnParams) GetPromptTemplate() string`

GetPromptTemplate returns the PromptTemplate field if non-nil, zero value otherwise.

### GetPromptTemplateOk

`func (o *LLMAsJudgeScoringFnParams) GetPromptTemplateOk() (*string, bool)`

GetPromptTemplateOk returns a tuple with the PromptTemplate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPromptTemplate

`func (o *LLMAsJudgeScoringFnParams) SetPromptTemplate(v string)`

SetPromptTemplate sets PromptTemplate field to given value.

### HasPromptTemplate

`func (o *LLMAsJudgeScoringFnParams) HasPromptTemplate() bool`

HasPromptTemplate returns a boolean if a field has been set.

### GetJudgeScoreRegexes

`func (o *LLMAsJudgeScoringFnParams) GetJudgeScoreRegexes() []string`

GetJudgeScoreRegexes returns the JudgeScoreRegexes field if non-nil, zero value otherwise.

### GetJudgeScoreRegexesOk

`func (o *LLMAsJudgeScoringFnParams) GetJudgeScoreRegexesOk() (*[]string, bool)`

GetJudgeScoreRegexesOk returns a tuple with the JudgeScoreRegexes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJudgeScoreRegexes

`func (o *LLMAsJudgeScoringFnParams) SetJudgeScoreRegexes(v []string)`

SetJudgeScoreRegexes sets JudgeScoreRegexes field to given value.

### HasJudgeScoreRegexes

`func (o *LLMAsJudgeScoringFnParams) HasJudgeScoreRegexes() bool`

HasJudgeScoreRegexes returns a boolean if a field has been set.

### GetAggregationFunctions

`func (o *LLMAsJudgeScoringFnParams) GetAggregationFunctions() []AggregationFunctionType`

GetAggregationFunctions returns the AggregationFunctions field if non-nil, zero value otherwise.

### GetAggregationFunctionsOk

`func (o *LLMAsJudgeScoringFnParams) GetAggregationFunctionsOk() (*[]AggregationFunctionType, bool)`

GetAggregationFunctionsOk returns a tuple with the AggregationFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAggregationFunctions

`func (o *LLMAsJudgeScoringFnParams) SetAggregationFunctions(v []AggregationFunctionType)`

SetAggregationFunctions sets AggregationFunctions field to given value.

### HasAggregationFunctions

`func (o *LLMAsJudgeScoringFnParams) HasAggregationFunctions() bool`

HasAggregationFunctions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


