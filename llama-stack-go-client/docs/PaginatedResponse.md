# PaginatedResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | The list of items for the current page | 
**HasMore** | **bool** | Whether there are more items available after this set | 

## Methods

### NewPaginatedResponse

`func NewPaginatedResponse(data []map[string]AppendRowsRequestRowsInnerValue, hasMore bool, ) *PaginatedResponse`

NewPaginatedResponse instantiates a new PaginatedResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPaginatedResponseWithDefaults

`func NewPaginatedResponseWithDefaults() *PaginatedResponse`

NewPaginatedResponseWithDefaults instantiates a new PaginatedResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetData

`func (o *PaginatedResponse) GetData() []map[string]AppendRowsRequestRowsInnerValue`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *PaginatedResponse) GetDataOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *PaginatedResponse) SetData(v []map[string]AppendRowsRequestRowsInnerValue)`

SetData sets Data field to given value.


### GetHasMore

`func (o *PaginatedResponse) GetHasMore() bool`

GetHasMore returns the HasMore field if non-nil, zero value otherwise.

### GetHasMoreOk

`func (o *PaginatedResponse) GetHasMoreOk() (*bool, bool)`

GetHasMoreOk returns a tuple with the HasMore field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMore

`func (o *PaginatedResponse) SetHasMore(v bool)`

SetHasMore sets HasMore field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


