# DataSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "uri"]
**Uri** | **string** | The dataset can be obtained from a URI. E.g. - \&quot;https://mywebsite.com/mydata.jsonl\&quot; - \&quot;lsfs://mydata.jsonl\&quot; - \&quot;data:csv;base64,{base64_content}\&quot; | 
**Rows** | [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | The dataset is stored in rows. E.g. - [ {\&quot;messages\&quot;: [{\&quot;role\&quot;: \&quot;user\&quot;, \&quot;content\&quot;: \&quot;Hello, world!\&quot;}, {\&quot;role\&quot;: \&quot;assistant\&quot;, \&quot;content\&quot;: \&quot;Hello, world!\&quot;}]} ] | 

## Methods

### NewDataSource

`func NewDataSource(type_ string, uri string, rows []map[string]AppendRowsRequestRowsInnerValue, ) *DataSource`

NewDataSource instantiates a new DataSource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDataSourceWithDefaults

`func NewDataSourceWithDefaults() *DataSource`

NewDataSourceWithDefaults instantiates a new DataSource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *DataSource) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DataSource) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *DataSource) SetType(v string)`

SetType sets Type field to given value.


### GetUri

`func (o *DataSource) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *DataSource) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *DataSource) SetUri(v string)`

SetUri sets Uri field to given value.


### GetRows

`func (o *DataSource) GetRows() []map[string]AppendRowsRequestRowsInnerValue`

GetRows returns the Rows field if non-nil, zero value otherwise.

### GetRowsOk

`func (o *DataSource) GetRowsOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetRowsOk returns a tuple with the Rows field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRows

`func (o *DataSource) SetRows(v []map[string]AppendRowsRequestRowsInnerValue)`

SetRows sets Rows field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


