# QueryCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Key** | **string** |  | 
**Op** | [**QueryConditionOp**](QueryConditionOp.md) |  | 
**Value** | [**NullableAppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewQueryCondition

`func NewQueryCondition(key string, op QueryConditionOp, value NullableAppendRowsRequestRowsInnerValue, ) *QueryCondition`

NewQueryCondition instantiates a new QueryCondition object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryConditionWithDefaults

`func NewQueryConditionWithDefaults() *QueryCondition`

NewQueryConditionWithDefaults instantiates a new QueryCondition object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetKey

`func (o *QueryCondition) GetKey() string`

GetKey returns the Key field if non-nil, zero value otherwise.

### GetKeyOk

`func (o *QueryCondition) GetKeyOk() (*string, bool)`

GetKeyOk returns a tuple with the Key field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKey

`func (o *QueryCondition) SetKey(v string)`

SetKey sets Key field to given value.


### GetOp

`func (o *QueryCondition) GetOp() QueryConditionOp`

GetOp returns the Op field if non-nil, zero value otherwise.

### GetOpOk

`func (o *QueryCondition) GetOpOk() (*QueryConditionOp, bool)`

GetOpOk returns a tuple with the Op field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOp

`func (o *QueryCondition) SetOp(v QueryConditionOp)`

SetOp sets Op field to given value.


### GetValue

`func (o *QueryCondition) GetValue() AppendRowsRequestRowsInnerValue`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *QueryCondition) GetValueOk() (*AppendRowsRequestRowsInnerValue, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *QueryCondition) SetValue(v AppendRowsRequestRowsInnerValue)`

SetValue sets Value field to given value.


### SetValueNil

`func (o *QueryCondition) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *QueryCondition) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


