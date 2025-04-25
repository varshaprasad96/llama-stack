# SyntheticDataGenerationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SyntheticData** | [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) |  | 
**Statistics** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewSyntheticDataGenerationResponse

`func NewSyntheticDataGenerationResponse(syntheticData []map[string]AppendRowsRequestRowsInnerValue, ) *SyntheticDataGenerationResponse`

NewSyntheticDataGenerationResponse instantiates a new SyntheticDataGenerationResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSyntheticDataGenerationResponseWithDefaults

`func NewSyntheticDataGenerationResponseWithDefaults() *SyntheticDataGenerationResponse`

NewSyntheticDataGenerationResponseWithDefaults instantiates a new SyntheticDataGenerationResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSyntheticData

`func (o *SyntheticDataGenerationResponse) GetSyntheticData() []map[string]AppendRowsRequestRowsInnerValue`

GetSyntheticData returns the SyntheticData field if non-nil, zero value otherwise.

### GetSyntheticDataOk

`func (o *SyntheticDataGenerationResponse) GetSyntheticDataOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetSyntheticDataOk returns a tuple with the SyntheticData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSyntheticData

`func (o *SyntheticDataGenerationResponse) SetSyntheticData(v []map[string]AppendRowsRequestRowsInnerValue)`

SetSyntheticData sets SyntheticData field to given value.


### GetStatistics

`func (o *SyntheticDataGenerationResponse) GetStatistics() map[string]AppendRowsRequestRowsInnerValue`

GetStatistics returns the Statistics field if non-nil, zero value otherwise.

### GetStatisticsOk

`func (o *SyntheticDataGenerationResponse) GetStatisticsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetStatisticsOk returns a tuple with the Statistics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatistics

`func (o *SyntheticDataGenerationResponse) SetStatistics(v map[string]AppendRowsRequestRowsInnerValue)`

SetStatistics sets Statistics field to given value.

### HasStatistics

`func (o *SyntheticDataGenerationResponse) HasStatistics() bool`

HasStatistics returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


