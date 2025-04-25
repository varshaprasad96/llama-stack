# RegisterBenchmarkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BenchmarkId** | **string** |  | 
**DatasetId** | **string** |  | 
**ScoringFunctions** | **[]string** |  | 
**ProviderBenchmarkId** | Pointer to **string** |  | [optional] 
**ProviderId** | Pointer to **string** |  | [optional] 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewRegisterBenchmarkRequest

`func NewRegisterBenchmarkRequest(benchmarkId string, datasetId string, scoringFunctions []string, ) *RegisterBenchmarkRequest`

NewRegisterBenchmarkRequest instantiates a new RegisterBenchmarkRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegisterBenchmarkRequestWithDefaults

`func NewRegisterBenchmarkRequestWithDefaults() *RegisterBenchmarkRequest`

NewRegisterBenchmarkRequestWithDefaults instantiates a new RegisterBenchmarkRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBenchmarkId

`func (o *RegisterBenchmarkRequest) GetBenchmarkId() string`

GetBenchmarkId returns the BenchmarkId field if non-nil, zero value otherwise.

### GetBenchmarkIdOk

`func (o *RegisterBenchmarkRequest) GetBenchmarkIdOk() (*string, bool)`

GetBenchmarkIdOk returns a tuple with the BenchmarkId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBenchmarkId

`func (o *RegisterBenchmarkRequest) SetBenchmarkId(v string)`

SetBenchmarkId sets BenchmarkId field to given value.


### GetDatasetId

`func (o *RegisterBenchmarkRequest) GetDatasetId() string`

GetDatasetId returns the DatasetId field if non-nil, zero value otherwise.

### GetDatasetIdOk

`func (o *RegisterBenchmarkRequest) GetDatasetIdOk() (*string, bool)`

GetDatasetIdOk returns a tuple with the DatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetId

`func (o *RegisterBenchmarkRequest) SetDatasetId(v string)`

SetDatasetId sets DatasetId field to given value.


### GetScoringFunctions

`func (o *RegisterBenchmarkRequest) GetScoringFunctions() []string`

GetScoringFunctions returns the ScoringFunctions field if non-nil, zero value otherwise.

### GetScoringFunctionsOk

`func (o *RegisterBenchmarkRequest) GetScoringFunctionsOk() (*[]string, bool)`

GetScoringFunctionsOk returns a tuple with the ScoringFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringFunctions

`func (o *RegisterBenchmarkRequest) SetScoringFunctions(v []string)`

SetScoringFunctions sets ScoringFunctions field to given value.


### GetProviderBenchmarkId

`func (o *RegisterBenchmarkRequest) GetProviderBenchmarkId() string`

GetProviderBenchmarkId returns the ProviderBenchmarkId field if non-nil, zero value otherwise.

### GetProviderBenchmarkIdOk

`func (o *RegisterBenchmarkRequest) GetProviderBenchmarkIdOk() (*string, bool)`

GetProviderBenchmarkIdOk returns a tuple with the ProviderBenchmarkId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderBenchmarkId

`func (o *RegisterBenchmarkRequest) SetProviderBenchmarkId(v string)`

SetProviderBenchmarkId sets ProviderBenchmarkId field to given value.

### HasProviderBenchmarkId

`func (o *RegisterBenchmarkRequest) HasProviderBenchmarkId() bool`

HasProviderBenchmarkId returns a boolean if a field has been set.

### GetProviderId

`func (o *RegisterBenchmarkRequest) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *RegisterBenchmarkRequest) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *RegisterBenchmarkRequest) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.

### HasProviderId

`func (o *RegisterBenchmarkRequest) HasProviderId() bool`

HasProviderId returns a boolean if a field has been set.

### GetMetadata

`func (o *RegisterBenchmarkRequest) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *RegisterBenchmarkRequest) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *RegisterBenchmarkRequest) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *RegisterBenchmarkRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


