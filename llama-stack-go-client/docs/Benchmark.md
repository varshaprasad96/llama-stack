# Benchmark

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Identifier** | **string** |  | 
**ProviderResourceId** | **string** |  | 
**ProviderId** | **string** |  | 
**Type** | **string** |  | [default to "benchmark"]
**DatasetId** | **string** |  | 
**ScoringFunctions** | **[]string** |  | 
**Metadata** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewBenchmark

`func NewBenchmark(identifier string, providerResourceId string, providerId string, type_ string, datasetId string, scoringFunctions []string, metadata map[string]AppendRowsRequestRowsInnerValue, ) *Benchmark`

NewBenchmark instantiates a new Benchmark object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBenchmarkWithDefaults

`func NewBenchmarkWithDefaults() *Benchmark`

NewBenchmarkWithDefaults instantiates a new Benchmark object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdentifier

`func (o *Benchmark) GetIdentifier() string`

GetIdentifier returns the Identifier field if non-nil, zero value otherwise.

### GetIdentifierOk

`func (o *Benchmark) GetIdentifierOk() (*string, bool)`

GetIdentifierOk returns a tuple with the Identifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifier

`func (o *Benchmark) SetIdentifier(v string)`

SetIdentifier sets Identifier field to given value.


### GetProviderResourceId

`func (o *Benchmark) GetProviderResourceId() string`

GetProviderResourceId returns the ProviderResourceId field if non-nil, zero value otherwise.

### GetProviderResourceIdOk

`func (o *Benchmark) GetProviderResourceIdOk() (*string, bool)`

GetProviderResourceIdOk returns a tuple with the ProviderResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderResourceId

`func (o *Benchmark) SetProviderResourceId(v string)`

SetProviderResourceId sets ProviderResourceId field to given value.


### GetProviderId

`func (o *Benchmark) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *Benchmark) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *Benchmark) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetType

`func (o *Benchmark) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Benchmark) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Benchmark) SetType(v string)`

SetType sets Type field to given value.


### GetDatasetId

`func (o *Benchmark) GetDatasetId() string`

GetDatasetId returns the DatasetId field if non-nil, zero value otherwise.

### GetDatasetIdOk

`func (o *Benchmark) GetDatasetIdOk() (*string, bool)`

GetDatasetIdOk returns a tuple with the DatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetId

`func (o *Benchmark) SetDatasetId(v string)`

SetDatasetId sets DatasetId field to given value.


### GetScoringFunctions

`func (o *Benchmark) GetScoringFunctions() []string`

GetScoringFunctions returns the ScoringFunctions field if non-nil, zero value otherwise.

### GetScoringFunctionsOk

`func (o *Benchmark) GetScoringFunctionsOk() (*[]string, bool)`

GetScoringFunctionsOk returns a tuple with the ScoringFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringFunctions

`func (o *Benchmark) SetScoringFunctions(v []string)`

SetScoringFunctions sets ScoringFunctions field to given value.


### GetMetadata

`func (o *Benchmark) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Benchmark) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Benchmark) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


