# GetSpanTreeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AttributesToReturn** | Pointer to **[]string** |  | [optional] 
**MaxDepth** | Pointer to **int32** |  | [optional] 

## Methods

### NewGetSpanTreeRequest

`func NewGetSpanTreeRequest() *GetSpanTreeRequest`

NewGetSpanTreeRequest instantiates a new GetSpanTreeRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetSpanTreeRequestWithDefaults

`func NewGetSpanTreeRequestWithDefaults() *GetSpanTreeRequest`

NewGetSpanTreeRequestWithDefaults instantiates a new GetSpanTreeRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAttributesToReturn

`func (o *GetSpanTreeRequest) GetAttributesToReturn() []string`

GetAttributesToReturn returns the AttributesToReturn field if non-nil, zero value otherwise.

### GetAttributesToReturnOk

`func (o *GetSpanTreeRequest) GetAttributesToReturnOk() (*[]string, bool)`

GetAttributesToReturnOk returns a tuple with the AttributesToReturn field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributesToReturn

`func (o *GetSpanTreeRequest) SetAttributesToReturn(v []string)`

SetAttributesToReturn sets AttributesToReturn field to given value.

### HasAttributesToReturn

`func (o *GetSpanTreeRequest) HasAttributesToReturn() bool`

HasAttributesToReturn returns a boolean if a field has been set.

### GetMaxDepth

`func (o *GetSpanTreeRequest) GetMaxDepth() int32`

GetMaxDepth returns the MaxDepth field if non-nil, zero value otherwise.

### GetMaxDepthOk

`func (o *GetSpanTreeRequest) GetMaxDepthOk() (*int32, bool)`

GetMaxDepthOk returns a tuple with the MaxDepth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDepth

`func (o *GetSpanTreeRequest) SetMaxDepth(v int32)`

SetMaxDepth sets MaxDepth field to given value.

### HasMaxDepth

`func (o *GetSpanTreeRequest) HasMaxDepth() bool`

HasMaxDepth returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


