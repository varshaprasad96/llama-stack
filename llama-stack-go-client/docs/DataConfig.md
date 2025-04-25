# DataConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DatasetId** | **string** |  | 
**BatchSize** | **int32** |  | 
**Shuffle** | **bool** |  | 
**DataFormat** | [**DatasetFormat**](DatasetFormat.md) |  | 
**ValidationDatasetId** | Pointer to **string** |  | [optional] 
**Packed** | Pointer to **bool** |  | [optional] [default to false]
**TrainOnInput** | Pointer to **bool** |  | [optional] [default to false]

## Methods

### NewDataConfig

`func NewDataConfig(datasetId string, batchSize int32, shuffle bool, dataFormat DatasetFormat, ) *DataConfig`

NewDataConfig instantiates a new DataConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDataConfigWithDefaults

`func NewDataConfigWithDefaults() *DataConfig`

NewDataConfigWithDefaults instantiates a new DataConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDatasetId

`func (o *DataConfig) GetDatasetId() string`

GetDatasetId returns the DatasetId field if non-nil, zero value otherwise.

### GetDatasetIdOk

`func (o *DataConfig) GetDatasetIdOk() (*string, bool)`

GetDatasetIdOk returns a tuple with the DatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetId

`func (o *DataConfig) SetDatasetId(v string)`

SetDatasetId sets DatasetId field to given value.


### GetBatchSize

`func (o *DataConfig) GetBatchSize() int32`

GetBatchSize returns the BatchSize field if non-nil, zero value otherwise.

### GetBatchSizeOk

`func (o *DataConfig) GetBatchSizeOk() (*int32, bool)`

GetBatchSizeOk returns a tuple with the BatchSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBatchSize

`func (o *DataConfig) SetBatchSize(v int32)`

SetBatchSize sets BatchSize field to given value.


### GetShuffle

`func (o *DataConfig) GetShuffle() bool`

GetShuffle returns the Shuffle field if non-nil, zero value otherwise.

### GetShuffleOk

`func (o *DataConfig) GetShuffleOk() (*bool, bool)`

GetShuffleOk returns a tuple with the Shuffle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShuffle

`func (o *DataConfig) SetShuffle(v bool)`

SetShuffle sets Shuffle field to given value.


### GetDataFormat

`func (o *DataConfig) GetDataFormat() DatasetFormat`

GetDataFormat returns the DataFormat field if non-nil, zero value otherwise.

### GetDataFormatOk

`func (o *DataConfig) GetDataFormatOk() (*DatasetFormat, bool)`

GetDataFormatOk returns a tuple with the DataFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataFormat

`func (o *DataConfig) SetDataFormat(v DatasetFormat)`

SetDataFormat sets DataFormat field to given value.


### GetValidationDatasetId

`func (o *DataConfig) GetValidationDatasetId() string`

GetValidationDatasetId returns the ValidationDatasetId field if non-nil, zero value otherwise.

### GetValidationDatasetIdOk

`func (o *DataConfig) GetValidationDatasetIdOk() (*string, bool)`

GetValidationDatasetIdOk returns a tuple with the ValidationDatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValidationDatasetId

`func (o *DataConfig) SetValidationDatasetId(v string)`

SetValidationDatasetId sets ValidationDatasetId field to given value.

### HasValidationDatasetId

`func (o *DataConfig) HasValidationDatasetId() bool`

HasValidationDatasetId returns a boolean if a field has been set.

### GetPacked

`func (o *DataConfig) GetPacked() bool`

GetPacked returns the Packed field if non-nil, zero value otherwise.

### GetPackedOk

`func (o *DataConfig) GetPackedOk() (*bool, bool)`

GetPackedOk returns a tuple with the Packed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPacked

`func (o *DataConfig) SetPacked(v bool)`

SetPacked sets Packed field to given value.

### HasPacked

`func (o *DataConfig) HasPacked() bool`

HasPacked returns a boolean if a field has been set.

### GetTrainOnInput

`func (o *DataConfig) GetTrainOnInput() bool`

GetTrainOnInput returns the TrainOnInput field if non-nil, zero value otherwise.

### GetTrainOnInputOk

`func (o *DataConfig) GetTrainOnInputOk() (*bool, bool)`

GetTrainOnInputOk returns a tuple with the TrainOnInput field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrainOnInput

`func (o *DataConfig) SetTrainOnInput(v bool)`

SetTrainOnInput sets TrainOnInput field to given value.

### HasTrainOnInput

`func (o *DataConfig) HasTrainOnInput() bool`

HasTrainOnInput returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


