# QuerySpansRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AttributeFilters** | [**[]QueryCondition**](QueryCondition.md) |  | 
**AttributesToReturn** | **[]string** |  | 
**MaxDepth** | Pointer to **int32** |  | [optional] 

## Methods

### NewQuerySpansRequest

`func NewQuerySpansRequest(attributeFilters []QueryCondition, attributesToReturn []string, ) *QuerySpansRequest`

NewQuerySpansRequest instantiates a new QuerySpansRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQuerySpansRequestWithDefaults

`func NewQuerySpansRequestWithDefaults() *QuerySpansRequest`

NewQuerySpansRequestWithDefaults instantiates a new QuerySpansRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAttributeFilters

`func (o *QuerySpansRequest) GetAttributeFilters() []QueryCondition`

GetAttributeFilters returns the AttributeFilters field if non-nil, zero value otherwise.

### GetAttributeFiltersOk

`func (o *QuerySpansRequest) GetAttributeFiltersOk() (*[]QueryCondition, bool)`

GetAttributeFiltersOk returns a tuple with the AttributeFilters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributeFilters

`func (o *QuerySpansRequest) SetAttributeFilters(v []QueryCondition)`

SetAttributeFilters sets AttributeFilters field to given value.


### GetAttributesToReturn

`func (o *QuerySpansRequest) GetAttributesToReturn() []string`

GetAttributesToReturn returns the AttributesToReturn field if non-nil, zero value otherwise.

### GetAttributesToReturnOk

`func (o *QuerySpansRequest) GetAttributesToReturnOk() (*[]string, bool)`

GetAttributesToReturnOk returns a tuple with the AttributesToReturn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributesToReturn

`func (o *QuerySpansRequest) SetAttributesToReturn(v []string)`

SetAttributesToReturn sets AttributesToReturn field to given value.


### GetMaxDepth

`func (o *QuerySpansRequest) GetMaxDepth() int32`

GetMaxDepth returns the MaxDepth field if non-nil, zero value otherwise.

### GetMaxDepthOk

`func (o *QuerySpansRequest) GetMaxDepthOk() (*int32, bool)`

GetMaxDepthOk returns a tuple with the MaxDepth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDepth

`func (o *QuerySpansRequest) SetMaxDepth(v int32)`

SetMaxDepth sets MaxDepth field to given value.

### HasMaxDepth

`func (o *QuerySpansRequest) HasMaxDepth() bool`

HasMaxDepth returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


