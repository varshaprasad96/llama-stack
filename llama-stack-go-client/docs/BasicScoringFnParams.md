# BasicScoringFnParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "basic"]
**AggregationFunctions** | Pointer to [**[]AggregationFunctionType**](AggregationFunctionType.md) |  | [optional] 

## Methods

### NewBasicScoringFnParams

`func NewBasicScoringFnParams(type_ string, ) *BasicScoringFnParams`

NewBasicScoringFnParams instantiates a new BasicScoringFnParams object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBasicScoringFnParamsWithDefaults

`func NewBasicScoringFnParamsWithDefaults() *BasicScoringFnParams`

NewBasicScoringFnParamsWithDefaults instantiates a new BasicScoringFnParams object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *BasicScoringFnParams) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BasicScoringFnParams) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BasicScoringFnParams) SetType(v string)`

SetType sets Type field to given value.


### GetAggregationFunctions

`func (o *BasicScoringFnParams) GetAggregationFunctions() []AggregationFunctionType`

GetAggregationFunctions returns the AggregationFunctions field if non-nil, zero value otherwise.

### GetAggregationFunctionsOk

`func (o *BasicScoringFnParams) GetAggregationFunctionsOk() (*[]AggregationFunctionType, bool)`

GetAggregationFunctionsOk returns a tuple with the AggregationFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAggregationFunctions

`func (o *BasicScoringFnParams) SetAggregationFunctions(v []AggregationFunctionType)`

SetAggregationFunctions sets AggregationFunctions field to given value.

### HasAggregationFunctions

`func (o *BasicScoringFnParams) HasAggregationFunctions() bool`

HasAggregationFunctions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


