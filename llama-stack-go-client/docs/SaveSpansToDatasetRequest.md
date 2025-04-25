# SaveSpansToDatasetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AttributeFilters** | [**[]QueryCondition**](QueryCondition.md) |  | 
**AttributesToSave** | **[]string** |  | 
**DatasetId** | **string** |  | 
**MaxDepth** | Pointer to **int32** |  | [optional] 

## Methods

### NewSaveSpansToDatasetRequest

`func NewSaveSpansToDatasetRequest(attributeFilters []QueryCondition, attributesToSave []string, datasetId string, ) *SaveSpansToDatasetRequest`

NewSaveSpansToDatasetRequest instantiates a new SaveSpansToDatasetRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSaveSpansToDatasetRequestWithDefaults

`func NewSaveSpansToDatasetRequestWithDefaults() *SaveSpansToDatasetRequest`

NewSaveSpansToDatasetRequestWithDefaults instantiates a new SaveSpansToDatasetRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAttributeFilters

`func (o *SaveSpansToDatasetRequest) GetAttributeFilters() []QueryCondition`

GetAttributeFilters returns the AttributeFilters field if non-nil, zero value otherwise.

### GetAttributeFiltersOk

`func (o *SaveSpansToDatasetRequest) GetAttributeFiltersOk() (*[]QueryCondition, bool)`

GetAttributeFiltersOk returns a tuple with the AttributeFilters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributeFilters

`func (o *SaveSpansToDatasetRequest) SetAttributeFilters(v []QueryCondition)`

SetAttributeFilters sets AttributeFilters field to given value.


### GetAttributesToSave

`func (o *SaveSpansToDatasetRequest) GetAttributesToSave() []string`

GetAttributesToSave returns the AttributesToSave field if non-nil, zero value otherwise.

### GetAttributesToSaveOk

`func (o *SaveSpansToDatasetRequest) GetAttributesToSaveOk() (*[]string, bool)`

GetAttributesToSaveOk returns a tuple with the AttributesToSave field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributesToSave

`func (o *SaveSpansToDatasetRequest) SetAttributesToSave(v []string)`

SetAttributesToSave sets AttributesToSave field to given value.


### GetDatasetId

`func (o *SaveSpansToDatasetRequest) GetDatasetId() string`

GetDatasetId returns the DatasetId field if non-nil, zero value otherwise.

### GetDatasetIdOk

`func (o *SaveSpansToDatasetRequest) GetDatasetIdOk() (*string, bool)`

GetDatasetIdOk returns a tuple with the DatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetId

`func (o *SaveSpansToDatasetRequest) SetDatasetId(v string)`

SetDatasetId sets DatasetId field to given value.


### GetMaxDepth

`func (o *SaveSpansToDatasetRequest) GetMaxDepth() int32`

GetMaxDepth returns the MaxDepth field if non-nil, zero value otherwise.

### GetMaxDepthOk

`func (o *SaveSpansToDatasetRequest) GetMaxDepthOk() (*int32, bool)`

GetMaxDepthOk returns a tuple with the MaxDepth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxDepth

`func (o *SaveSpansToDatasetRequest) SetMaxDepth(v int32)`

SetMaxDepth sets MaxDepth field to given value.

### HasMaxDepth

`func (o *SaveSpansToDatasetRequest) HasMaxDepth() bool`

HasMaxDepth returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


