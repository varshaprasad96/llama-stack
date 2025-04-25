# QueryTracesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AttributeFilters** | Pointer to [**[]QueryCondition**](QueryCondition.md) |  | [optional] 
**Limit** | Pointer to **int32** |  | [optional] 
**Offset** | Pointer to **int32** |  | [optional] 
**OrderBy** | Pointer to **[]string** |  | [optional] 

## Methods

### NewQueryTracesRequest

`func NewQueryTracesRequest() *QueryTracesRequest`

NewQueryTracesRequest instantiates a new QueryTracesRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQueryTracesRequestWithDefaults

`func NewQueryTracesRequestWithDefaults() *QueryTracesRequest`

NewQueryTracesRequestWithDefaults instantiates a new QueryTracesRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAttributeFilters

`func (o *QueryTracesRequest) GetAttributeFilters() []QueryCondition`

GetAttributeFilters returns the AttributeFilters field if non-nil, zero value otherwise.

### GetAttributeFiltersOk

`func (o *QueryTracesRequest) GetAttributeFiltersOk() (*[]QueryCondition, bool)`

GetAttributeFiltersOk returns a tuple with the AttributeFilters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributeFilters

`func (o *QueryTracesRequest) SetAttributeFilters(v []QueryCondition)`

SetAttributeFilters sets AttributeFilters field to given value.

### HasAttributeFilters

`func (o *QueryTracesRequest) HasAttributeFilters() bool`

HasAttributeFilters returns a boolean if a field has been set.

### GetLimit

`func (o *QueryTracesRequest) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *QueryTracesRequest) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *QueryTracesRequest) SetLimit(v int32)`

SetLimit sets Limit field to given value.

### HasLimit

`func (o *QueryTracesRequest) HasLimit() bool`

HasLimit returns a boolean if a field has been set.

### GetOffset

`func (o *QueryTracesRequest) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *QueryTracesRequest) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *QueryTracesRequest) SetOffset(v int32)`

SetOffset sets Offset field to given value.

### HasOffset

`func (o *QueryTracesRequest) HasOffset() bool`

HasOffset returns a boolean if a field has been set.

### GetOrderBy

`func (o *QueryTracesRequest) GetOrderBy() []string`

GetOrderBy returns the OrderBy field if non-nil, zero value otherwise.

### GetOrderByOk

`func (o *QueryTracesRequest) GetOrderByOk() (*[]string, bool)`

GetOrderByOk returns a tuple with the OrderBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOrderBy

`func (o *QueryTracesRequest) SetOrderBy(v []string)`

SetOrderBy sets OrderBy field to given value.

### HasOrderBy

`func (o *QueryTracesRequest) HasOrderBy() bool`

HasOrderBy returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


