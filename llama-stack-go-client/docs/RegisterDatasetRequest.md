# RegisterDatasetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Purpose** | **string** | The purpose of the dataset. One of - \&quot;post-training/messages\&quot;: The dataset contains a messages column with list of messages for post-training. { \&quot;messages\&quot;: [ {\&quot;role\&quot;: \&quot;user\&quot;, \&quot;content\&quot;: \&quot;Hello, world!\&quot;}, {\&quot;role\&quot;: \&quot;assistant\&quot;, \&quot;content\&quot;: \&quot;Hello, world!\&quot;}, ] } - \&quot;eval/question-answer\&quot;: The dataset contains a question column and an answer column for evaluation. { \&quot;question\&quot;: \&quot;What is the capital of France?\&quot;, \&quot;answer\&quot;: \&quot;Paris\&quot; } - \&quot;eval/messages-answer\&quot;: The dataset contains a messages column with list of messages and an answer column for evaluation. { \&quot;messages\&quot;: [ {\&quot;role\&quot;: \&quot;user\&quot;, \&quot;content\&quot;: \&quot;Hello, my name is John Doe.\&quot;}, {\&quot;role\&quot;: \&quot;assistant\&quot;, \&quot;content\&quot;: \&quot;Hello, John Doe. How can I help you today?\&quot;}, {\&quot;role\&quot;: \&quot;user\&quot;, \&quot;content\&quot;: \&quot;What&#39;s my name?\&quot;}, ], \&quot;answer\&quot;: \&quot;John Doe\&quot; } | 
**Source** | [**DataSource**](DataSource.md) | The data source of the dataset. Ensure that the data source schema is compatible with the purpose of the dataset. Examples: - { \&quot;type\&quot;: \&quot;uri\&quot;, \&quot;uri\&quot;: \&quot;https://mywebsite.com/mydata.jsonl\&quot; } - { \&quot;type\&quot;: \&quot;uri\&quot;, \&quot;uri\&quot;: \&quot;lsfs://mydata.jsonl\&quot; } - { \&quot;type\&quot;: \&quot;uri\&quot;, \&quot;uri\&quot;: \&quot;data:csv;base64,{base64_content}\&quot; } - { \&quot;type\&quot;: \&quot;uri\&quot;, \&quot;uri\&quot;: \&quot;huggingface://llamastack/simpleqa?split&#x3D;train\&quot; } - { \&quot;type\&quot;: \&quot;rows\&quot;, \&quot;rows\&quot;: [ { \&quot;messages\&quot;: [ {\&quot;role\&quot;: \&quot;user\&quot;, \&quot;content\&quot;: \&quot;Hello, world!\&quot;}, {\&quot;role\&quot;: \&quot;assistant\&quot;, \&quot;content\&quot;: \&quot;Hello, world!\&quot;}, ] } ] } | 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | The metadata for the dataset. - E.g. {\&quot;description\&quot;: \&quot;My dataset\&quot;} | [optional] 
**DatasetId** | Pointer to **string** | The ID of the dataset. If not provided, an ID will be generated. | [optional] 

## Methods

### NewRegisterDatasetRequest

`func NewRegisterDatasetRequest(purpose string, source DataSource, ) *RegisterDatasetRequest`

NewRegisterDatasetRequest instantiates a new RegisterDatasetRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegisterDatasetRequestWithDefaults

`func NewRegisterDatasetRequestWithDefaults() *RegisterDatasetRequest`

NewRegisterDatasetRequestWithDefaults instantiates a new RegisterDatasetRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPurpose

`func (o *RegisterDatasetRequest) GetPurpose() string`

GetPurpose returns the Purpose field if non-nil, zero value otherwise.

### GetPurposeOk

`func (o *RegisterDatasetRequest) GetPurposeOk() (*string, bool)`

GetPurposeOk returns a tuple with the Purpose field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPurpose

`func (o *RegisterDatasetRequest) SetPurpose(v string)`

SetPurpose sets Purpose field to given value.


### GetSource

`func (o *RegisterDatasetRequest) GetSource() DataSource`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *RegisterDatasetRequest) GetSourceOk() (*DataSource, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *RegisterDatasetRequest) SetSource(v DataSource)`

SetSource sets Source field to given value.


### GetMetadata

`func (o *RegisterDatasetRequest) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *RegisterDatasetRequest) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *RegisterDatasetRequest) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *RegisterDatasetRequest) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetDatasetId

`func (o *RegisterDatasetRequest) GetDatasetId() string`

GetDatasetId returns the DatasetId field if non-nil, zero value otherwise.

### GetDatasetIdOk

`func (o *RegisterDatasetRequest) GetDatasetIdOk() (*string, bool)`

GetDatasetIdOk returns a tuple with the DatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetId

`func (o *RegisterDatasetRequest) SetDatasetId(v string)`

SetDatasetId sets DatasetId field to given value.

### HasDatasetId

`func (o *RegisterDatasetRequest) HasDatasetId() bool`

HasDatasetId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


